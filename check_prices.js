const fs = require('fs');
const path = require('path');

const cleanDir = 'C:\\Users\\quant\\.gemini\\antigravity\\brain\\15c1b059-6909-48c0-82ee-fede74c0abd5\\scraped_clean';
const files = fs.readdirSync(cleanDir);

files.forEach(file => {
  if (file.toLowerCase().includes('paquete')) {
    const filePath = path.join(cleanDir, file);
    const content = fs.readFileSync(filePath, 'utf8');
    const lines = content.split('\n');
    console.log(`\n========================================\nFILE: ${file}`);
    
    // Find lines with pricing info
    lines.forEach((line, index) => {
      if (line.includes('$') || line.toLowerCase().includes('precio') || line.toLowerCase().includes('costo') || line.toLowerCase().includes('ps')) {
        console.log(`L${index + 1}: ${line.trim()}`);
      }
    });
  }
});
