const fs = require('fs');
const html = fs.readFileSync('C:\\Users\\quant\\.gemini\\antigravity\\brain\\15c1b059-6909-48c0-82ee-fede74c0abd5\\.system_generated\\steps\\238\\content.md', 'utf8');

// Strip HTML tags and entities
let text = html.replace(/<style[\s\S]*?<\/style>/gi, '')
               .replace(/<script[\s\S]*?<\/script>/gi, '')
               .replace(/<[^>]*>/g, ' ')
               .replace(/&nbsp;/g, ' ')
               .replace(/\s+/g, ' ')
               .trim();

console.log(text.substring(0, 5000));
console.log('----------------- CONTINUACION -----------------');
console.log(text.substring(5000, 10000));
console.log('----------------- CONTINUACION 2 -----------------');
console.log(text.substring(10000, 15000));
