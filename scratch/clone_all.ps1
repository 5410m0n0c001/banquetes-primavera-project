$repos = @(
    @{ name = "villa-di-fiori-"; url = "https://github.com/5410m0n0c001/villa-di-fiori-" },
    @{ name = "solaire"; url = "https://github.com/5410m0n0c001/solaire" },
    @{ name = "expo-boda-y-15-a-os"; url = "https://github.com/5410m0n0c001/expo-boda-y-15-a-os" },
    @{ name = "antonio-cotizacion"; url = "https://github.com/5410m0n0c001/antonio-cotizacion" },
    @{ name = "viviana-cotizaci-n-"; url = "https://github.com/5410m0n0c001/viviana-cotizaci-n-" },
    @{ name = "cotizaci-n-DIF"; url = "https://github.com/5410m0n0c001/cotizaci-n-DIF" },
    @{ name = "cotizaci-n-edie"; url = "https://github.com/5410m0n0c001/cotizaci-n-edie" },
    @{ name = "-Sra.-Sandra-cotizaci-n"; url = "https://github.com/5410m0n0c001/-Sra.-Sandra-cotizaci-n" },
    @{ name = "cotizacion-viky-solaire"; url = "https://github.com/5410m0n0c001/cotizacion-viky-solaire" },
    @{ name = "yolomecatl-croquis-"; url = "https://github.com/5410m0n0c001/yolomecatl-croquis-" },
    @{ name = "centro-de-convenciones-presidente-croquis"; url = "https://github.com/5410m0n0c001/centro-de-convenciones-presidente-croquis" },
    @{ name = "jardin-la-flor-plano"; url = "https://github.com/5410m0n0c001/jardin-la-flor-plano" },
    @{ name = "primavera-events-group-agente-sofia-"; url = "https://github.com/5410m0n0c001/primavera-events-group-agente-sofia-" }
)

$clonesDir = Join-Path $PSScriptRoot "clones"
if (!(Test-Path $clonesDir)) {
    New-Item -ItemType Directory -Path $clonesDir | Out-Null
}

foreach ($repo in $repos) {
    $dest = Join-Path $clonesDir $repo.name
    if (Test-Path $dest) {
        Write-Host "Repository $($repo.name) already exists. Skipping."
        continue
    }
    Write-Host "Cloning $($repo.name) from $($repo.url)..."
    git clone $repo.url $dest
}

Write-Host "Cloning process completed!"
