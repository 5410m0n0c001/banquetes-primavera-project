$path = "C:\Users\quant\.gemini\antigravity\brain\44f2dd75-2dbb-4aa6-878f-6843102f25f7\task.md"
$content = @"
# Tareas de Extraccion de Datos y Creacion de RAG - Primavera Events Group

- [x] Extraccion de Contenidos del Sitio
    - [x] Filtrar URLs clave desde urls_to_scrape.json (paquetes, menus, locaciones, servicios)
    - [x] Descargar y extraer el contenido de cada pagina clave usando read_url_content
    - [x] Parsear informacion clave (inclusiones de paquetes, precios de menus, capacidades de locaciones)
- [x] Consolidacion de Datos (RAG & Base de Conocimiento)
    - [x] Crear archivo de base de datos estructurado base_de_datos_primavera.json
    - [x] Crear documento Markdown legible por humanos base_de_datos_primavera.md
- [x] Validacion e Informe
    - [x] Verificar consistencia de tablas de precios y paquetes
    - [x] Generar Walkthrough de cambios de la fase de ejecucion
"@
Set-Content -Path $path -Value $content -Encoding utf8
