const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const repos = [
    { name: 'villa-di-fiori-', url: 'https://github.com/5410m0n0c001/villa-di-fiori-' },
    { name: 'solaire', url: 'https://github.com/5410m0n0c001/solaire' },
    { name: 'expo-boda-y-15-a-os', url: 'https://github.com/5410m0n0c001/expo-boda-y-15-a-os' },
    { name: 'antonio-cotizacion', url: 'https://github.com/5410m0n0c001/antonio-cotizacion' },
    { name: 'viviana-cotizaci-n-', url: 'https://github.com/5410m0n0c001/viviana-cotizaci-n-' },
    { name: 'cotizaci-n-DIF', url: 'https://github.com/5410m0n0c001/cotizaci-n-DIF' },
    { name: 'cotizaci-n-edie', url: 'https://github.com/5410m0n0c001/cotizaci-n-edie' },
    { name: '-Sra.-Sandra-cotizaci-n', url: 'https://github.com/5410m0n0c001/-Sra.-Sandra-cotizaci-n' },
    { name: 'cotizacion-viky-solaire', url: 'https://github.com/5410m0n0c001/cotizacion-viky-solaire' },
    { name: 'yolomecatl-croquis-', url: 'https://github.com/5410m0n0c001/yolomecatl-croquis-' },
    { name: 'centro-de-convenciones-presidente-croquis', url: 'https://github.com/5410m0n0c001/centro-de-convenciones-presidente-croquis' },
    { name: 'jardin-la-flor-plano', url: 'https://github.com/5410m0n0c001/jardin-la-flor-plano' },
    { name: 'primavera-events-group-agente-sofia-', url: 'https://github.com/5410m0n0c001/primavera-events-group-agente-sofia-' }
];

const clonesDir = path.join(__dirname, 'clones');
if (!fs.existsSync(clonesDir)) {
    fs.mkdirSync(clonesDir);
}

repos.forEach(repo => {
    const dest = path.join(clonesDir, repo.name);
    if (fs.existsSync(dest)) {
        console.log(`Repository ${repo.name} already exists. Skipping.`);
        return;
    }
    console.log(`Cloning ${repo.name} from ${repo.url}...`);
    try {
        execSync(`git clone ${repo.url} "${dest}"`, { stdio: 'inherit' });
    } catch (err) {
        console.error(`Failed to clone ${repo.name}:`, err.message);
    }
});

console.log('Cloning process completed!');
