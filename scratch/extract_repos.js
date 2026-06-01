const fs = require('fs');
const path = require('path');

const clonesPath = path.join(__dirname, 'clones');
const outputPath = path.join(__dirname, 'extracted_data.json');

const data = {
    cotizaciones: [],
    locaciones_adicionales: {},
    manual_marca: {},
    plan_marketing: {}
};

// Función para extraer metadatos básicos de un HTML
function parseQuoteHtml(dirName, filePath) {
    if (!fs.existsSync(filePath)) return null;
    const content = fs.readFileSync(filePath, 'utf8');

    // Regexes y búsquedas de texto
    const titleMatch = content.match(/<title>([^<]+)<\/title>/i);
    const descMatch = content.match(/<meta\s+name="description"\s+content="([^"]+)"/i) || 
                      content.match(/<meta\s+property="og:description"\s+content="([^"]+)"/i);
    
    const guestsMatch = content.match(/(\d+)\s*(personas|Pers\.|invitados)/i);
    
    // Buscar precios p/p (ej. $950, $850, $1,050)
    const pricePPMatches = [...content.matchAll(/\$(\d{3,4}(?:\.\d{2})?)\s*(?:p\/p|por persona|Costo p\/p)/ig)];
    const pricePP = pricePPMatches.length > 0 ? pricePPMatches[0][1] : null;

    // Buscar precios de locación (ej. $32,000, $30,000, $28,000)
    const venuePriceMatches = [...content.matchAll(/\$(\d{2,3},\d{3})/g)];
    const venuePrices = venuePriceMatches.map(m => m[1]);

    // Buscar activos (música, videos)
    const musicMatch = content.match(/src="([^"]+\.mp3)"/i) || content.match(/['"]assets\/([^'"]+\.mp3)['"]/i);
    const videos = [...content.matchAll(/src="([^"]+\.mp4)/g)].map(m => m[1]);
    const images = [...content.matchAll(/img\s+src="([^"]+\.(?:png|jpg|jpeg|webp))"/gi)].map(m => m[1]);

    // Buscar locaciones asociadas
    const locaciones = [];
    const ccPresidente = content.includes('centro-de-convenciones-presidente') || content.includes('Centro de Convenciones Presidente');
    const potrillos = content.includes('potrillos') || content.includes('Potrillos');
    const caballos = content.includes('los-caballos') || content.includes('Los Caballos');
    const laFlor = content.includes('la-flor') || content.includes('La Flor');
    const yolomecatl = content.includes('yolomecatl') || content.includes('Yolomecatl');
    const tsuNuum = content.includes('tsu-nuum') || content.includes('Tsu Nuum');
    const zarabanda = content.includes('zarabanda') || content.includes('Zarabanda');
    const isabeles = content.includes('isabeles') || content.includes('Isabeles');
    const villaFiori = content.includes('villa-di-fiori') || content.includes('Villa di Fiori') || content.includes('Villa Di Fiori');
    const solaire = content.includes('solaire') || content.includes('Solaire') || content.includes('Sol Aire');

    if (ccPresidente) locaciones.push('Centro de Convenciones Presidente');
    if (potrillos) locaciones.push('Rancho/Salón Los Potrillos');
    if (caballos) locaciones.push('Salón Los Caballos');
    if (laFlor) locaciones.push('Jardín La Flor');
    if (yolomecatl) locaciones.push('Salón Jardín Yolomecatl');
    if (tsuNuum) locaciones.push('Jardín Tsu Nuum');
    if (zarabanda) locaciones.push('Quinta Zarabanda');
    if (isabeles) locaciones.push('Finca Las Isabeles');
    if (villaFiori) locaciones.push('Villa Di Fiori');
    if (solaire) locaciones.push('Salón Solaire');

    return {
        repo: dirName,
        title: titleMatch ? titleMatch[1].trim() : dirName,
        description: descMatch ? descMatch[1].trim() : '',
        guests: guestsMatch ? parseInt(guestsMatch[1]) : null,
        price_per_person: pricePP ? parseFloat(pricePP.replace(',', '')) : null,
        venue_prices: venuePrices,
        music: musicMatch ? musicMatch[1] : null,
        videos: [...new Set(videos)],
        images: [...new Set(images)],
        locaciones_mencionadas: locaciones,
        size_bytes: fs.statSync(filePath).size
    };
}

// Escanear todas las carpetas en clones/
if (fs.existsSync(clonesPath)) {
    const dirs = fs.readdirSync(clonesPath);
    for (const dir of dirs) {
        const dirFullPath = path.join(clonesPath, dir);
        if (fs.statSync(dirFullPath).isDirectory()) {
            if (dir === 'expo-boda-y-15-anos') {
                // Parsear manual y plan de marketing
                const manualFile = path.join(dirFullPath, 'manual.html');
                if (fs.existsSync(manualFile)) {
                    const manualContent = fs.readFileSync(manualFile, 'utf8');
                    // Extraer los colaboradores de la tabla
                    const collabTableMatch = manualContent.match(/<table[^>]*manual-table[^>]*>([\s\S]*?)<\/table>/i);
                    const team = [];
                    if (collabTableMatch) {
                        const trs = [...collabTableMatch[1].matchAll(/<tr>([\s\S]*?)<\/tr>/g)];
                        trs.forEach(tr => {
                            const tds = [...tr[1].matchAll(/<td>([\s\S]*?)<\/td>/g)].map(td => td[1].replace(/<[^>]+>/g, '').trim());
                            if (tds.length >= 2) {
                                team.push({ cargo: tds[0], descripcion: tds[1] });
                            }
                        });
                    }
                    data.manual_marca.team = team;
                    
                    // Extraer colores
                    const colors = [];
                    const colorCards = [...manualContent.matchAll(/class="color-card"[\s\S]*?<h5>([^<]+)<\/h5>[\s\S]*?<code>([^<]+)<\/code>/g)];
                    colorCards.forEach(card => {
                        colors.push({ nombre: card[1].trim(), hex: card[2].trim() });
                    });
                    data.manual_marca.colores = colors;

                    // Extraer hashtags
                    const hashtags = [];
                    const hashMatches = [...manualContent.matchAll(/#\w+/g)];
                    hashMatches.forEach(hm => hashtags.push(hm[0]));
                    data.manual_marca.hashtags = [...new Set(hashtags)];
                }

                const marketingFile = path.join(dirFullPath, 'plan-marketing.html');
                if (fs.existsSync(marketingFile)) {
                    const marketingContent = fs.readFileSync(marketingFile, 'utf8');
                    // Extraer contraseña de acceso
                    const passMatch = marketingContent.match(/const\s+PASSWORD\s*=\s*['"]([^'"]+)['"]/i) || 
                                      marketingContent.match(/if\s*\(.*===\s*['"]([^'"]+)['"]\)/i) ||
                                      marketingContent.match(/['"](primavera2026|primavera2026expos|expos2026|admin2026)['"]/i);
                    data.plan_marketing.password = passMatch ? passMatch[1] || passMatch[0].replace(/['"]/g, '') : 'No encontrada';

                    // Extraer enlaces del plan
                    const links = [];
                    const linkMatches = [...marketingContent.matchAll(/<tr[^>]*>[\s\S]*?<td>([^<]+)<\/td>[\s\S]*?href="([^"]+)"/g)];
                    linkMatches.forEach(m => {
                        links.push({ nombre: m[1].trim(), url: m[2].trim() });
                    });
                    data.plan_marketing.enlaces_utilidades = links;
                }
            } else {
                // Es una cotización o local específico
                const indexPath = path.join(dirFullPath, 'index.html');
                const parsed = parseQuoteHtml(dir, indexPath);
                if (parsed) {
                    data.cotizaciones.push(parsed);
                }
            }
        }
    }
}

// Escribir los datos extraídos
fs.writeFileSync(outputPath, JSON.stringify(data, null, 4), 'utf8');
console.log('¡Extracción completada con éxito!');
