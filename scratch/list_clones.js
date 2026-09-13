const fs = require('fs');
const path = require('path');

const clonesPath = path.join(__dirname, 'clones');
const dirs = fs.readdirSync(clonesPath);

dirs.forEach(dir => {
    const dirPath = path.join(clonesPath, dir);
    if (!fs.statSync(dirPath).isDirectory()) return;
    
    console.log(`\n========================================`);
    console.log(`REPO: ${dir}`);
    console.log(`========================================`);
    
    const files = [];
    function walk(currentPath) {
        const list = fs.readdirSync(currentPath);
        list.forEach(file => {
            const filePath = path.join(currentPath, file);
            const stat = fs.statSync(filePath);
            if (stat.isDirectory()) {
                if (file !== '.git') {
                    walk(filePath);
                }
            } else {
                files.push({
                    rel: path.relative(dirPath, filePath),
                    size: stat.size
                });
            }
        });
    }
    
    try {
        walk(dirPath);
        files.forEach(f => {
            console.log(`- ${f.rel} (${(f.size/1024).toFixed(2)} KB)`);
        });
    } catch (e) {
        console.log(`Error walking: ${e.message}`);
    }
});
