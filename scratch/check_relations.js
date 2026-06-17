const fs = require('fs');

const db = JSON.parse(fs.readFileSync('base_de_datos_primavera.json', 'utf8'));

db.venues.forEach(v => {
  console.log(`\n========================================`);
  console.log(`VENUE: ${v.name} (${v.location || 'No location'})`);
  console.log(`Capacity: ${v.capacity}`);
  console.log(`Style: ${v.style}`);
  
  // Find matching packages
  const matchedPackages = db.packages.filter(p => {
    const venueText = p.venue || p.location || '';
    return venueText.toLowerCase().includes(v.name.toLowerCase()) || 
           v.name.toLowerCase().includes(p.name.toLowerCase());
  });
  
  if (matchedPackages.length > 0) {
    console.log(`  Packages:`);
    matchedPackages.forEach(p => {
      console.log(`    - [Package] ${p.name} (Duration: ${p.duration || 'N/A'})`);
      if (p.pricing) {
        console.log(`      Pricing:`, JSON.stringify(p.pricing));
      }
    });
  } else {
    console.log(`  No direct packages matched.`);
  }
  
  // Find matching cotizaciones
  const matchedCotizaciones = db.cotizaciones_reales.filter(c => {
    const recintoText = c.recinto || '';
    return recintoText.toLowerCase().includes(v.name.toLowerCase());
  });
  
  if (matchedCotizaciones.length > 0) {
    console.log(`  Cotizaciones Reales:`);
    matchedCotizaciones.forEach(c => {
      console.log(`    - [Cotizacion] ${c.cliente} (Cost: ${c.precio_por_persona || 'N/A'}, Min: ${c.minimo_invitados || 'N/A'})`);
    });
  }
});
