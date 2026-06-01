const fs = require('fs');
const text = fs.readFileSync('c:\\Users\\quant\\OneDrive\\Desktop\\Banqutes primavera web\\assets\\datos.txt', 'utf8');

// Split by lines and search for prices or numbers
const lines = text.split('\n');
console.log('--- Buscando lineas con precios, locaciones o numeros en datos.txt ---');
lines.forEach((line, index) => {
  if (line.includes('$') || line.includes('pesos') || line.includes('precio') || line.includes('costo') || line.includes('Persona') || line.includes('persona') || line.includes('menú') || line.includes('Gobernador') || line.includes('Presidente') || line.includes('Zarabanda')) {
    console.log(`Línea ${index + 1}: ${line.trim()}`);
  }
});
