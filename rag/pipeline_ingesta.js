/**
 * pipeline_ingesta.js
 * Pipeline de Ingesta, Chunking y Vectorización del "cerebro" RAG de Primavera Events Group.
 * Stack: Node.js, Gemini Embeddings (gemini-embedding-001, truncado a 1536 dims), Supabase (Postgres + pgvector)
 *
 * Uso:
 *   GEMINI_API_KEY=... SUPABASE_URL=... SUPABASE_SERVICE_ROLE_KEY=... node pipeline_ingesta.js
 *
 * Requiere: npm install (ver package.json en esta misma carpeta)
 */

const fs = require('fs');
const path = require('path');
const { createClient } = require('@supabase/supabase-js');

const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_SERVICE_ROLE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
const GEMINI_API_KEY = process.env.GEMINI_API_KEY;
const EMBEDDING_MODEL = 'gemini-embedding-001';
const EMBEDDING_DIMENSIONS = 1536; // debe coincidir con VECTOR(1536) en conocimiento_rag_chunks

if (!SUPABASE_URL || !SUPABASE_SERVICE_ROLE_KEY || !GEMINI_API_KEY) {
    console.error('Faltan variables de entorno: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, GEMINI_API_KEY son obligatorias.');
    process.exit(1);
}

const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY);

const ROOT = path.join(__dirname, '..');
const database = JSON.parse(fs.readFileSync(path.join(ROOT, 'base_de_datos_primavera.json'), 'utf8'));

let totalChunks = 0;
let totalInsertados = 0;
let totalFallos = 0;

function chunkText(text, size = 2000, overlap = 250) {
    const clean = (text || '').trim();
    if (!clean) return [];
    const chunks = [];
    let start = 0;
    while (start < clean.length) {
        const end = Math.min(start + size, clean.length);
        chunks.push(clean.slice(start, end));
        if (end >= clean.length) break;
        start += (size - overlap);
    }
    return chunks;
}

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function getEmbedding(text, retries = 3) {
    const url = `https://generativelanguage.googleapis.com/v1beta/models/${EMBEDDING_MODEL}:embedContent`;
    for (let attempt = 1; attempt <= retries; attempt++) {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'x-goog-api-key': GEMINI_API_KEY,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                model: `models/${EMBEDDING_MODEL}`,
                content: { parts: [{ text }] },
                outputDimensionality: EMBEDDING_DIMENSIONS
            })
        });
        if (response.status === 429 && attempt < retries) {
            await sleep(2000 * attempt);
            continue;
        }
        if (!response.ok) {
            const errText = await response.text();
            throw new Error(`Gemini API ${response.status}: ${errText}`);
        }
        const result = await response.json();
        return result.embedding.values;
    }
}

/**
 * Trocea `contenido` y sube cada chunk a conocimiento_rag_chunks.
 * @param {string} fuenteDocumento - nombre del archivo/sección de origen
 * @param {string} categoria - etiqueta de categoría (paquete, venue, cotizacion, ...)
 * @param {string} contenido - texto completo del registro/documento
 * @param {object} metadataExtra - metadata adicional específica del registro
 */
async function ingestarBloque(fuenteDocumento, categoria, contenido, metadataExtra = {}) {
    const chunks = chunkText(contenido);
    for (let i = 0; i < chunks.length; i++) {
        totalChunks++;
        const chunk = chunks[i];
        try {
            const embedding = await getEmbedding(chunk);
            const { error } = await supabase.from('conocimiento_rag_chunks').insert([{
                fuente_documento: fuenteDocumento,
                categoria: categoria,
                contenido_chunk: chunk,
                embedding: embedding,
                metadata: { ...metadataExtra, chunk_index: i, total_chunks: chunks.length }
            }]);
            if (error) throw new Error(error.message);
            totalInsertados++;
        } catch (e) {
            totalFallos++;
            console.error(`  Fallo [${fuenteDocumento} / ${categoria} / chunk ${i}]:`, e.message);
        }
        await sleep(700); // capa gratuita de Gemini: límite de 100 req/min, con margen
    }
}

// ---------- Secciones de base_de_datos_primavera.json ----------

async function procesarPaquetes() {
    for (const pkg of database.packages || []) {
        const text = `Paquete: ${pkg.name}\nVenue: ${pkg.venue}\nDuración: ${pkg.duration}\nInclusiones:\n${(pkg.inclusions || []).join('\n')}\nEstructura de menú: ${JSON.stringify(pkg.menu_structure || {})}\nPrecios: ${JSON.stringify(pkg.pricing || {})}\nCondiciones: ${JSON.stringify(pkg.conditions || {})}`;
        await ingestarBloque('base_de_datos_primavera.json#packages', 'paquete', text, { paquete_id: pkg.id, paquete_nombre: pkg.name, venue: pkg.venue, url: pkg.url });
    }
}

async function procesarMenus() {
    for (const m of database.menus || []) {
        const text = `Menú: ${m.name}\nDescripción: ${m.description || ''}\nCategorías: ${JSON.stringify(m.categories || [])}`;
        await ingestarBloque('base_de_datos_primavera.json#menus', 'menu', text, { menu_id: m.id, menu_nombre: m.name, url: m.url });
    }
}

async function procesarVenues() {
    for (const v of database.venues || []) {
        const text = `Venue: ${v.name}\nUbicación: ${v.location}\nCapacidad: ${v.capacity}\nEstilo: ${v.style}\nCaracterísticas:\n${(v.features || []).join('\n')}`;
        await ingestarBloque('base_de_datos_primavera.json#venues', 'venue', text, { venue_id: v.id, venue_nombre: v.name, url: v.url });
    }
}

async function procesarServicios() {
    for (const s of database.services || []) {
        const text = `Servicio: ${s.name}\nDescripción: ${s.description || ''}\nCaracterísticas:\n${(s.features || []).join('\n')}`;
        await ingestarBloque('base_de_datos_primavera.json#services', 'servicio', text, { servicio_id: s.id, servicio_nombre: s.name, url: s.url });
    }
}

async function procesarCotizacionesReales() {
    for (const cot of database.cotizaciones_reales || []) {
        const text = `Cotización real — Cliente: ${cot.cliente}\nRecinto: ${cot.recinto}\nPrecio por persona: ${cot.precio_por_persona}\nMínimo de invitados: ${cot.minimo_invitados}\nInclusiones:\n${(cot.inclusiones || []).join('\n')}\nCortesías:\n${(cot.cortesias || []).join('\n')}`;
        await ingestarBloque('base_de_datos_primavera.json#cotizaciones_reales', 'cotizacion', text, { cliente: cot.cliente, recinto: cot.recinto });
    }
}

async function procesarEntradasBlog() {
    for (const post of database.entradas_blog || []) {
        const text = `Entrada de blog: ${post.titulo}\nAutor: ${post.autor}\nFecha: ${post.fecha}\nResumen: ${post.resumen}\nInclusiones mencionadas:\n${(post.inclusiones || []).join('\n')}`;
        await ingestarBloque('base_de_datos_primavera.json#entradas_blog', 'blog', text, { titulo: post.titulo, url: post.url });
    }
}

async function procesarColaboradores() {
    for (const c of database.colaboradores || []) {
        const text = `Colaborador: ${c.nombre}\nCargo: ${c.cargo}\nDescripción: ${c.descripcion}`;
        await ingestarBloque('base_de_datos_primavera.json#colaboradores', 'colaborador', text, { nombre: c.nombre, cargo: c.cargo });
    }
}

async function procesarAgentesConversacionales() {
    const a = database.agentes_conversacionales;
    if (!a) return;
    const text = `Agente conversacional: ${JSON.stringify(a.agente || {})}\nComentario: ${a.comentario || ''}`;
    await ingestarBloque('base_de_datos_primavera.json#agentes_conversacionales', 'agente', text, {});
}

async function procesarExpoBoda2026() {
    const expo = database.expo_boda_2026;
    if (!expo) return;
    const evento = expo.evento || {};
    const textEvento = `Evento: ${evento.nombre}\nFecha: ${evento.fecha}\nLugar: ${evento.lugar}\nManual de colaboración: ${JSON.stringify(expo.manual_colaboracion || {})}\nEstrategia de marketing: ${JSON.stringify(expo.estrategia_marketing || {})}`;
    await ingestarBloque('base_de_datos_primavera.json#expo_boda_2026', 'expo', textEvento, { evento: evento.nombre });

    for (const p of expo.proveedores_expositores || []) {
        const text = `Proveedor expositor Expo Boda 2026: ${p.nombre_comercial}\n${p.texto_completo || ''}`;
        await ingestarBloque('base_de_datos_primavera.json#expo_boda_2026.proveedores_expositores', 'expo_proveedor', text, { proveedor: p.nombre_comercial });
    }
    // Nota: leads_capturados se omite intencionalmente (datos personales de prospectos, no es
    // conocimiento operativo de negocio — si se necesita en el RAG, ingestar aparte con criterio de PII).
}

async function procesarSeccionesDict() {
    const secciones = [
        ['constantes_interaccion', database.constantes_interaccion],
        ['politicas_y_promociones', database.politicas_y_promociones],
        ['manual_marca', database.manual_marca],
        ['croquis_y_planos', database.croquis_y_planos],
    ];
    for (const [nombre, valor] of secciones) {
        if (!valor) continue;
        await ingestarBloque('base_de_datos_primavera.json#' + nombre, nombre, JSON.stringify(valor, null, 2), {});
    }

    // plan_marketing: se ingesta SIN el campo password_acceso (no debe vivir en chunks de texto libre)
    if (database.plan_marketing) {
        const { password_acceso, ...planMarketingSinPassword } = database.plan_marketing;
        await ingestarBloque('base_de_datos_primavera.json#plan_marketing', 'plan_marketing', JSON.stringify(planMarketingSinPassword, null, 2), {});
    }
}

async function procesarPreciosAndreaLozano() {
    const fullPath = path.join(ROOT, 'andrea lozano precios', 'precios_extraidos.json');
    if (!fs.existsSync(fullPath)) {
        console.warn('  Aviso: no existe precios_extraidos.json (proveedor Andrea Lozano), se omite.');
        return;
    }
    const items = JSON.parse(fs.readFileSync(fullPath, 'utf8'));
    for (const item of items) {
        if (item.tipo_contenido !== 'lista_precios') continue;
        const text = `Proveedor: Andrea Lozano Beauty Salón (maquillaje/peinado)\n${item.texto_crudo}`;
        await ingestarBloque('andrea lozano precios/precios_extraidos.json', 'proveedor_precios', text, {
            proveedor: 'Andrea Lozano',
            archivo_origen: item.archivo,
            servicios: item.servicios
        });
    }
}

async function procesarInventarioMobiliario() {
    const inv = database.inventario_mobiliario_2026;
    if (!inv) return;
    // Agrupar por categoria para no generar 189 chunks de 1 renglon cada uno
    const porCategoria = {};
    for (const item of inv.items || []) {
        const cat = item.categoria || 'Sin categoria';
        (porCategoria[cat] = porCategoria[cat] || []).push(`${item.nombre}: $${item.precioRenta} MXN`);
    }
    for (const [categoria, lineas] of Object.entries(porCategoria)) {
        const text = `Inventario de mobiliario/renta — categoria "${categoria}"\nRegla de consolidacion: ${inv.metadata.regla_consolidacion}\n${lineas.join('\n')}`;
        await ingestarBloque('base_de_datos_primavera.json#inventario_mobiliario_2026', 'inventario', text, { categoria });
    }
}

// ---------- Documentos maestros sueltos (Markdown) ----------

async function procesarDocumentosMaestros() {
    const docs = [
        ['DIRECTIVES.md', 'directriz_maestra'],
        ['.agents/AGENTS.md', 'reglas_agente'],
        ['playbook_comercial_manual_ventas.md', 'manual_ventas'],
        ['manual_cotizaciones.md', 'manual_cotizaciones'],
        ['rag/prompts/sistema_bot_madre.md', 'prompt_sistema'],
        ['rag/prompts/calificacion_leads.md', 'scoring_leads'],
        ['redes_sociales_directrices.md', 'directrices_redes_sociales'],
    ];
    for (const [rel, categoria] of docs) {
        const fullPath = path.join(ROOT, rel);
        if (!fs.existsSync(fullPath)) {
            console.warn(`  Aviso: no existe ${rel}, se omite.`);
            continue;
        }
        const contenido = fs.readFileSync(fullPath, 'utf8');
        await ingestarBloque(rel, categoria, contenido, {});
    }
}

// ---------- Ejecutor principal ----------

async function runPipeline() {
    console.log('Iniciando ingesta RAG de Primavera Events Group...\n');

    const pasos = [
        ['Paquetes', procesarPaquetes],
        ['Menús', procesarMenus],
        ['Venues', procesarVenues],
        ['Servicios', procesarServicios],
        ['Cotizaciones reales', procesarCotizacionesReales],
        ['Entradas de blog', procesarEntradasBlog],
        ['Colaboradores', procesarColaboradores],
        ['Agentes conversacionales', procesarAgentesConversacionales],
        ['Expo Boda 2026', procesarExpoBoda2026],
        ['Secciones dict (políticas, marca, etc.)', procesarSeccionesDict],
        ['Documentos maestros (.md)', procesarDocumentosMaestros],
        ['Precios Andrea Lozano (proveedora)', procesarPreciosAndreaLozano],
        ['Inventario de mobiliario 2026', procesarInventarioMobiliario],
    ];

    for (const [nombre, fn] of pasos) {
        console.log(`→ ${nombre}...`);
        await fn();
    }

    console.log(`\nFinalizado. Chunks generados: ${totalChunks} | Insertados: ${totalInsertados} | Fallidos: ${totalFallos}`);
    if (totalFallos > 0) process.exitCode = 1;
}

runPipeline().catch((e) => {
    console.error('Error fatal en el pipeline:', e);
    process.exit(1);
});
