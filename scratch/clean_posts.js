const fs = require('fs');
const path = require('path');

const srcDir = 'C:\\Users\\quant\\.gemini\\antigravity\\brain\\15c1b059-6909-48c0-82ee-fede74c0abd5\\.system_generated\\steps';
const destDir = 'C:\\Users\\quant\\.gemini\\antigravity\\brain\\15c1b059-6909-48c0-82ee-fede74c0abd5\\scraped_clean';

const postsMapping = {
  212: { url: "https://primaveraeventsgroup.com/expo-boda-y-quince-anos-centro-de-convenciones-presidente/", name: "Expo Boda y Quince Anos C.C Presidente" },
  228: { url: "https://primaveraeventsgroup.com/expo-boda-y-15-anos/", name: "Expo Boda y 15 Anos Temixco" },
  232: { url: "https://primaveraeventsgroup.com/primavera-haute-runway/", name: "Pasarela Primavera Haute Runway" },
  298: { url: "https://primaveraeventsgroup.com/wedding-bridesmaids-groomsmen/", name: "Damas y Caballeros de Honor" },
  300: { url: "https://primaveraeventsgroup.com/wedding-event-location/", name: "Locacion del Evento" },
  302: { url: "https://primaveraeventsgroup.com/wedding-final-preparation/", name: "Preparativos Finales de Boda" }
};

for (const [step, info] of Object.entries(postsMapping)) {
  const filePath = path.join(srcDir, step, 'content.md');
  if (!fs.existsSync(filePath)) {
    console.log(`File not found: ${filePath}`);
    continue;
  }

  let html = fs.readFileSync(filePath, 'utf8');

  // Strip headers, css, scripts
  html = html.replace(/^Title:[\s\S]*?---/, '');
  html = html.replace(/<head[\s\S]*?<\/head>/gi, '');
  html = html.replace(/<style[\s\S]*?<\/style>/gi, '');
  html = html.replace(/<script[\s\S]*?<\/script>/gi, '');
  html = html.replace(/<svg[\s\S]*?<\/svg>/gi, '');

  // Strip tables and simple html formatting
  html = html.replace(/<h[1-6][\s\S]*?>([\s\S]*?)<\/h[1-6]>/gi, (match, content) => {
    return `\n\n### ${content.replace(/<[\s\S]*?>/g, '').trim()}\n\n`;
  });
  html = html.replace(/<p[\s\S]*?>([\s\S]*?)<\/p>/gi, (match, content) => {
    return `\n${content.replace(/<[\s\S]*?>/g, '').trim()}\n`;
  });
  html = html.replace(/<li[\s\S]*?>([\s\S]*?)<\/li>/gi, (match, content) => {
    return `\n- ${content.replace(/<[\s\S]*?>/g, '').trim()}\n`;
  });

  let textContent = html.replace(/<[\s\S]*?>/g, '');
  textContent = textContent
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&middot;/g, '·')
    .replace(/&bull;/g, '•');

  textContent = textContent.replace(/\n\s*\n\s*\n+/g, '\n\n');
  textContent = textContent.replace(/[ \t]+/g, ' ');

  const destPath = path.join(destDir, `post_${step}_${info.name.replace(/\s+/g, '_')}.md`);
  fs.writeFileSync(destPath, `# ${info.name}\nSource: ${info.url}\n\n${textContent}`, 'utf8');
  console.log(`Cleaned Post: ${destPath}`);
}
