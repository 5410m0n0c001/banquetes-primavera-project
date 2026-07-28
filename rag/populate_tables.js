/**
 * populate_tables.js
 * Llena las tablas relacionales (venues, paquetes_servicios, complementos_catalogo)
 * de Supabase a partir de base_de_datos_primavera.json — para que el cotizador web
 * pueda consultarlas directo, sin depender del RAG semantico.
 *
 * Uso: SUPABASE_URL=... SUPABASE_SERVICE_ROLE_KEY=... node populate_tables.js
 */
const fs = require('fs');
const path = require('path');
const { createClient } = require('@supabase/supabase-js');

const SUPABASE_URL = process.env.SUPABASE_URL;
const SUPABASE_SERVICE_ROLE_KEY = process.env.SUPABASE_SERVICE_ROLE_KEY;
if (!SUPABASE_URL || !SUPABASE_SERVICE_ROLE_KEY) {
    console.error('Faltan SUPABASE_URL / SUPABASE_SERVICE_ROLE_KEY');
    process.exit(1);
}
const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY);

const db = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'base_de_datos_primavera.json'), 'utf8'));

function slugify(s) {
    return s.toLowerCase()
        .replace(/[áàä]/g, 'a').replace(/[éèë]/g, 'e').replace(/[íìï]/g, 'i')
        .replace(/[óòö]/g, 'o').replace(/[úùü]/g, 'u').replace(/ñ/g, 'n')
        .replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '');
}

async function poblarVenues() {
    const seen = new Set();
    const rows = db.venues.map(v => {
        const name = v.name || v.nombre_venue || 'Sin nombre';
        let slug = slugify(v.id || name);
        while (seen.has(slug)) slug += '-2';
        seen.add(slug);
        const { name: _n, nombre_venue: _nv, id: _id, location, capacity, style, url, features, inclusiones_generales, ...metadata } = v;
        return {
            slug,
            nombre: name,
            ubicacion: location || 'No especificada',
            capacidad_max: typeof capacity === 'number' ? capacity : null,
            estilo: style || null,
            url_oficial: url || null,
            inclusiones_generales: features || inclusiones_generales || [],
            metadata
        };
    });
    const { error, data } = await supabase.from('venues').upsert(rows, { onConflict: 'slug' }).select('id');
    if (error) throw new Error('venues: ' + error.message);
    console.log(`venues: ${data.length} filas`);
}

async function poblarPaquetes() {
    const rows = db.packages.map(p => ({
        nombre: p.name,
        segmento: /xv|15/i.test(p.name) ? 'xv_anos' : 'bodas_general',
        tipo_precio: 'por_persona',
        precios_escala: p.pricing || [],
        inclusiones: p.inclusions || [],
        validez_dias: 15,
        metadata: { url: p.url, venue: p.venue, duration: p.duration, menu_structure: p.menu_structure, conditions: p.conditions, id_original: p.id }
    }));
    const { error, data } = await supabase.from('paquetes_servicios').insert(rows).select('id');
    if (error) throw new Error('paquetes_servicios: ' + error.message);
    console.log(`paquetes_servicios: ${data.length} filas`);
}

async function poblarComplementos() {
    const rows = [];
    for (const s of db.services || []) {
        rows.push({
            nombre: s.name,
            categoria: 'servicio_terceros',
            precio_sugerido: null,
            activo: true,
            metadata: { url: s.url, id_original: s.id, features: s.features }
        });
    }
    const inv = (db.inventario_mobiliario_2026 || {}).items || [];
    for (const item of inv) {
        rows.push({
            nombre: item.nombre,
            categoria: 'mobiliario_' + item.categoria.toLowerCase(),
            precio_sugerido: item.precioRenta,
            activo: true,
            metadata: { fuente: 'inventario_mobiliario_2026' }
        });
    }
    // Insertar en lotes de 50 para evitar payloads gigantes
    for (let i = 0; i < rows.length; i += 50) {
        const batch = rows.slice(i, i + 50);
        const { error, data } = await supabase.from('complementos_catalogo').insert(batch).select('id');
        if (error) throw new Error('complementos_catalogo: ' + error.message);
        console.log(`complementos_catalogo: +${data.length} (lote ${i / 50 + 1})`);
    }
}

async function main() {
    await poblarVenues();
    await poblarPaquetes();
    await poblarComplementos();
    console.log('Listo.');
}

main().catch(e => { console.error(e); process.exit(1); });
