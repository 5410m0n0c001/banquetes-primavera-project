const fs = require('fs');
const path = require('path');

const srcDir = 'C:\\Users\\quant\\.gemini\\antigravity\\brain\\15c1b059-6909-48c0-82ee-fede74c0abd5\\.system_generated\\steps';
const destDir = 'C:\\Users\\quant\\.gemini\\antigravity\\brain\\15c1b059-6909-48c0-82ee-fede74c0abd5\\scraped_clean';

if (!fs.existsSync(destDir)) {
  fs.mkdirSync(destDir, { recursive: true });
}

const mapping = {
  26: { url: "https://primaveraeventsgroup.com/", name: "Inicio" },
  27: { url: "https://primaveraeventsgroup.com/paquetes-primavera/", name: "Paquetes Overview" },
  28: { url: "https://primaveraeventsgroup.com/venues/", name: "Venues Overview" },
  29: { url: "https://primaveraeventsgroup.com/paquete-gobernador/", name: "Paquete Gobernador" },
  30: { url: "https://primaveraeventsgroup.com/paquete-glow-graduation-elite/", name: "Paquete Glow Graduation Elite" },
  31: { url: "https://primaveraeventsgroup.com/paquete-presidente/", name: "Paquete Presidente" },
  32: { url: "https://primaveraeventsgroup.com/paquete-esencia-floral/", name: "Paquete Esencia Floral" },
  33: { url: "https://primaveraeventsgroup.com/paquetes-de-fotografia-y-video/", name: "Paquetes de Fotografia y Video" },
  35: { url: "https://primaveraeventsgroup.com/paquete-experiencia-deluxe/", name: "Paquete Experiencia Deluxe" },
  36: { url: "https://primaveraeventsgroup.com/paquete-cinematic-prestige/", name: "Paquete Cinematic Prestige" },
  37: { url: "https://primaveraeventsgroup.com/paquete-royal-cinematic/", name: "Paquete Royal Cinematic" },
  38: { url: "https://primaveraeventsgroup.com/paquete-eternal-promise/", name: "Paquete Eternal Promise" },
  39: { url: "https://primaveraeventsgroup.com/paquete-armonia/", name: "Paquete Armonia" },
  40: { url: "https://primaveraeventsgroup.com/paquete-memoria-clasica/", name: "Paquete Memoria Clasica" },
  41: { url: "https://primaveraeventsgroup.com/paquete-vuelo-esmeralda/", name: "Paquete Vuelo Esmeralda" },
  42: { url: "https://primaveraeventsgroup.com/paquete-imperial-ecuestre/", name: "Paquete Imperial Ecuestre" },
  44: { url: "https://primaveraeventsgroup.com/paquete-destino-yolomecatl/", name: "Paquete Destino Yolomecatl" },
  45: { url: "https://primaveraeventsgroup.com/paquete-linaje-pura-sangre/", name: "Paquete Linaje Pura Sangre" },
  46: { url: "https://primaveraeventsgroup.com/paquete-natures-majesty/", name: "Paquete Natures Majesty" },
  47: { url: "https://primaveraeventsgroup.com/quinta-san-francisco/", name: "Quinta San Francisco" },
  48: { url: "https://primaveraeventsgroup.com/centro-de-convenciones-presidente/", name: "Centro de Convenciones Presidente" },
  49: { url: "https://primaveraeventsgroup.com/jardin-la-flor/", name: "Jardin La Flor" },
  50: { url: "https://primaveraeventsgroup.com/quinta-zarabanda/", name: "Quinta Zarabanda" },
  51: { url: "https://primaveraeventsgroup.com/finca-las-isabeles/", name: "Finca Las Isabeles" },
  53: { url: "https://primaveraeventsgroup.com/salon-los-potrillos/", name: "Salon Los Potrillos" },
  54: { url: "https://primaveraeventsgroup.com/jardin-tsu-nuum/", name: "Jardin Tsu Nuum" },
  55: { url: "https://primaveraeventsgroup.com/salon-los-caballos/", name: "Salon Los Caballos" },
  56: { url: "https://primaveraeventsgroup.com/salon-jardin-yolomecatl/", name: "Salon Jardin Yolomecatl" },
  57: { url: "https://primaveraeventsgroup.com/menu-gourmet/menu-primavera-2026/", name: "Menu Gourmet Primavera 2026" },
  58: { url: "https://primaveraeventsgroup.com/menu-gourmet/menu-primavera-2026/buffet-mexicano/", name: "Menu Buffet Mexicano" },
  59: { url: "https://primaveraeventsgroup.com/menu-gourmet/", name: "Menu Gourmet Overview" },
  60: { url: "https://primaveraeventsgroup.com/nuestros-menus/", name: "Nuestros Menus" },
  62: { url: "https://primaveraeventsgroup.com/menu-gourmet/menu-primavera-2026/buffet-mexicano/buffet-pastas-y-pizzas/parrillada-de-cortes-de-carne-y-guarniciones-en-buffet/", name: "Menu Parrillada de Cortes" },
  63: { url: "https://primaveraeventsgroup.com/menu-gourmet/menu-primavera-2026/buffet-mexicano/buffet-pastas-y-pizzas/", name: "Menu Buffet Pastas y Pizzas" },
  64: { url: "https://primaveraeventsgroup.com/nuestros-postres/", name: "Nuestros Postres" },
  65: { url: "https://primaveraeventsgroup.com/transportacion/", name: "Servicio Transportacion" },
  66: { url: "https://primaveraeventsgroup.com/montajes-y-mobiliario/", name: "Servicio Montajes y Mobiliario" },
  67: { url: "https://primaveraeventsgroup.com/staffing/", name: "Servicio Staffing" },
  68: { url: "https://primaveraeventsgroup.com/fotografia-y-video/", name: "Servicio Fotografia y Video" },
  69: { url: "https://primaveraeventsgroup.com/quinceaneras-primavera/", name: "Servicio Quinceaneras" },
  70: { url: "https://primaveraeventsgroup.com/bodas/", name: "Servicio Bodas" },
  71: { url: "https://primaveraeventsgroup.com/graduaciones-primavera/", name: "Servicio Graduaciones" }
};

for (const [step, info] of Object.entries(mapping)) {
  const filePath = path.join(srcDir, step, 'content.md');
  if (!fs.existsSync(filePath)) {
    console.log(`File not found: ${filePath}`);
    continue;
  }

  let html = fs.readFileSync(filePath, 'utf8');

  // Strip header meta info from cached file
  html = html.replace(/^Title:[\s\S]*?---/, '');

  // Strip CSS, head, script, and SVG tags
  html = html.replace(/<head[\s\S]*?<\/head>/gi, '');
  html = html.replace(/<style[\s\S]*?<\/style>/gi, '');
  html = html.replace(/<script[\s\S]*?<\/script>/gi, '');
  html = html.replace(/<svg[\s\S]*?<\/svg>/gi, '');

  // Custom table extractor to convert HTML tables to markdown tables before stripping other HTML tags!
  html = html.replace(/<table[\s\S]*?<\/table>/gi, (tableHtml) => {
    // Parse table rows
    const trs = tableHtml.match(/<tr[\s\S]*?<\/tr>/gi) || [];
    const rows = trs.map(tr => {
      const tds = tr.match(/<(td|th)[\s\S]*?<\/\2>/gi) || [];
      return tds.map(td => {
        // Strip inner html tags from cells
        let text = td.replace(/<[\s\S]*?>/g, '').trim();
        // Replace multiple spaces and newlines
        text = text.replace(/\s+/g, ' ');
        return text;
      });
    });

    if (rows.length === 0) return '';

    // Format as markdown table
    let md = '\n';
    rows.forEach((row, i) => {
      md += '| ' + row.join(' | ') + ' |\n';
      if (i === 0) {
        // Add separator
        md += '| ' + row.map(() => '---').join(' | ') + ' |\n';
      }
    });
    md += '\n';
    return md;
  });

  // Strip all other HTML tags except basic headings, paragraphs, and lists
  // But actually let's strip all HTML tags, converting <h1-6> to markdown headings, <p> to newlines, etc.
  html = html.replace(/<h[1-6][\s\S]*?>([\s\S]*?)<\/h[1-6]>/gi, (match, content) => {
    const text = content.replace(/<[\s\S]*?>/g, '').trim();
    return `\n\n### ${text}\n\n`;
  });

  html = html.replace(/<p[\s\S]*?>([\s\S]*?)<\/p>/gi, (match, content) => {
    const text = content.replace(/<[\s\S]*?>/g, '').trim();
    return `\n${text}\n`;
  });

  html = html.replace(/<li[\s\S]*?>([\s\S]*?)<\/li>/gi, (match, content) => {
    const text = content.replace(/<[\s\S]*?>/g, '').trim();
    return `\n- ${text}\n`;
  });

  // Strip any remaining html tags
  let textContent = html.replace(/<[\s\S]*?>/g, '');

  // Decode basic HTML entities
  textContent = textContent
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&middot;/g, '·')
    .replace(/&bull;/g, '•');

  // Collapse multiple empty lines
  textContent = textContent.replace(/\n\s*\n\s*\n+/g, '\n\n');
  textContent = textContent.replace(/[ \t]+/g, ' ');

  // Save the cleaned markdown/text file
  const destPath = path.join(destDir, `${step}_${info.name.replace(/\s+/g, '_')}.md`);
  fs.writeFileSync(destPath, `# ${info.name}\nSource: ${info.url}\n\n${textContent}`, 'utf8');
  console.log(`Cleaned: ${destPath}`);
}
