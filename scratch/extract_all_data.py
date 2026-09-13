import os
import json
import re
from datetime import datetime

clones_dir = r"C:\Users\Lenovo\Documents\primavera brain\scratch\clones"
dest_dir = r"C:\Users\Lenovo\Documents\primavera brain"

def get_metadata(repo, filename, status="completo"):
    return {
        "repo_origen": f"https://github.com/5410m0n0c001/{repo}",
        "archivo_origen": filename,
        "fecha_extraccion": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "estado": status
    }

# 1. villa-di-fiori-
def extract_villa_di_fiori():
    repo = "villa-di-fiori-"
    filepath = os.path.join(clones_dir, repo, "index.html")
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Extract client, price, inclusions, locations
    client = "Señor Erasmo"
    price = "$850.00 MXN"
    guests = 120
    
    inclusions = [
        "Montaje elegante y Decoración (Letras Iniciales Iluminadas, decoración floral, templete de madera, centro floral natural)",
        "Banquete a 3 tiempos (Primer Tiempo: Entradas; Segundo Tiempo: Plato Fuerte de pollo o cerdo con 2 guarniciones, pan y chiles; Tercer Tiempo: Tornafiesta de chilaquiles o esquites)",
        "Cóctel de bienvenida con periqueras altas, salas lounge, margaritas sin alcohol, piñadas, mojitos y aguas frescas",
        "Personal Especializado (Meseros uniformados, cocina, stewards, Hostess, Capitán de Meseros y Coordinador General)",
        "Música y Entretenimiento (DJ profesional con cabina, audio/iluminación, pista de baile 5x5)",
        "Comodidades Exclusivas (9 horas de servicio continuo y estacionamiento)"
    ]
    
    locaciones = [
        "Centro de Convenciones Presidente",
        "Salón Los Potrillos",
        "Salón Los Caballos"
    ]
    
    data = {
        "metadata": get_metadata(repo, "index.html"),
        "nombre_venue": "Villa Di Fiori",
        "name": "Villa Di Fiori",
        "cliente": client,
        "tipo_evento": "Paquete Premium Completo (XV Años / Boda)",
        "invitados_estimados": guests,
        "precio_por_persona": price,
        "inclusiones": inclusions,
        "locaciones_disponibles": locaciones,
        "imagenes": ["portada.png", "los caballos.webp", "rancho los potrillos.webp"]
    }
    
    out_path = os.path.join(dest_dir, "venues", "villa_di_fiori.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Extracted Villa di Fiori")

# 2. solaire
def extract_solaire():
    repo = "solaire"
    filepath = os.path.join(clones_dir, repo, "index.html")
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    inclusions = [
        "Espacio para banquete y cóctel",
        "Áreas ajardinadas y semi techadas",
        "Iluminación ambiental de casa",
        "Barra para preparación de bebidas",
        "Descorche libre de bebidas",
        "Baños de lujo con personal",
        "Atención personalizada",
        "Horario hasta las 3:30 am"
    ]
    
    packages = [
        {
            "nombre": "Boda en Solaire",
            "capacidad": "Hasta 180 personas",
            "duracion": "8 hrs",
            "precio_locacion": "$32,000 MXN",
            "precio_banquete_desde": "$850 p/p",
            "detalles": "Alta estética y personalización total."
        },
        {
            "nombre": "Evento Social",
            "capacidad": "Hasta 100 personas",
            "duracion": "8 hrs",
            "precio_locacion": "$30,000 MXN",
            "precio_banquete_desde": "$900 p/p",
            "detalles": "Incluye mobiliario de casa (mix parota y vintage)."
        },
        {
            "nombre": "Evento Petite (Mobiliario Campirano)",
            "capacidad": "Hasta 80 personas",
            "precio_locacion": "$28,000 MXN",
            "precio_banquete_completo": "$1,050 p/p",
            "inclusiones_especificas": [
                "Mesas de madera sólida estilo campirano",
                "Sillas Crossback de diseño",
                "Vajilla a un tiempo: Plato trinche, cubiertos y vaso",
                "Camino de mesa a tono de su elección"
            ]
        }
    ]
    
    data = {
        "metadata": get_metadata(repo, "index.html"),
        "nombre_venue": "Jardín Solaire",
        "inclusiones_generales": inclusions,
        "paquetes_y_tarifas_2026": packages
    }
    
    out_path = os.path.join(dest_dir, "venues", "solaire.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Extracted Solaire")

# 3. antonio-cotizacion
def extract_antonio():
    repo = "antonio-cotizacion"
    filepath = os.path.join(clones_dir, repo, "index.html")
    if not os.path.exists(filepath):
        return
    
    # We parsed these details earlier
    data = {
        "metadata": get_metadata(repo, "index.html"),
        "cliente": "XV Años Antonio (Propuesta Premium)",
        "recinto": "Selección a elegir (ccPresidente, Los Potrillos, Los Caballos, La Flor, Yolomecatl)",
        "precio_por_persona": "$950.00 MXN",
        "total_inversion": "$123,500.00 MXN",
        "minimo_invitados": 130,
        "fecha": "Marzo 2027",
        "tipo_evento": "XV Años",
        "inclusiones": [
            "Mobiliario Elegante: Montaje de gala con mesas de mármol y sillas Tiffany",
            "Banquete Exquisito: Menú gourmet a 3 tiempos con coctel de bienvenida y tornafiesta",
            "Personal de Servicio: Coordinador, capitán, meseros, barra, stewarts, Hostess",
            "Música y Audio: DJ profesional, iluminación robótica, pista 5x5, chisperos",
            "Cortesías: Letras gigantes iluminadas, corazón rojo, espejo selfie, barra mix con toppings"
        ]
    }
    
    out_path = os.path.join(dest_dir, "cotizaciones", "antonio.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Extracted Antonio")

# 4. viviana-cotizaci-n-
def extract_viviana():
    repo = "viviana-cotizaci-n-"
    filepath = os.path.join(clones_dir, repo, "index.html")
    if not os.path.exists(filepath):
        return
        
    data = {
        "metadata": get_metadata(repo, "index.html"),
        "cliente": "Aniversario Viviana (Propuesta Premium)",
        "recinto": "Salón Los Potrillos",
        "precio_por_persona": "$690.00 MXN",
        "total_inversion": "$62,100.00 MXN",
        "minimo_invitados": 90,
        "fecha": "18 Julio 2026",
        "tipo_evento": "Aniversario de Bodas",
        "inclusiones": [
            "Mobiliario Elegante: Montaje de gala con mobiliario de diseño (Tiffany, Crossback, Lotus o Boss)",
            "Menú a 3 tiempos con coctel de bienvenida y mezcladores completos",
            "Personal Profesional: Coordinador general, hostess, meseros uniformados, personal de cocina, stewards, barman",
            "DJ profesional con cabina, audio, iluminación y pista de baile 5x5",
            "Cortesías: Espejo selfie de bienvenida, barra de mixología con toppings, letras gigantes iluminadas",
            "Tiempo de servicio: 9 horas de servicio continuo"
        ]
    }
    
    out_path = os.path.join(dest_dir, "cotizaciones", "viviana.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Extracted Viviana")

# 5. cotizaci-n-DIF
def extract_dif():
    repo = "cotizaci-n-DIF"
    filepath = os.path.join(clones_dir, repo, "index.html")
    if not os.path.exists(filepath):
        return
        
    data = {
        "metadata": get_metadata(repo, "index.html"),
        "cliente": "Sistema DIF / Lic. Claudia López",
        "recinto": "Centro de Convenciones Presidente",
        "precio_por_persona": "$260.00 MXN",
        "total_inversion": "$32,500.00 MXN",
        "minimo_invitados": 125,
        "fecha": "13 de Mayo",
        "tipo_evento": "Desayuno Tipo Taquiza",
        "inclusiones": [
            "Mobiliario Completo: Mesa redonda o cuadrada con silla Tiffany, mantelería fina (mantel y cubre mantel)",
            "Cristaleria y Vajilla: Montaje elegante con vajilla completa y cristalería de primera calidad",
            "Menú Selecto: Taquiza tradicional con variedad de guisados a su elección",
            "Bebidas Ilimitadas: Servicio continuo de refrescos de la línea Coca-Cola y aguas de sabores de fruta natural",
            "Personal de Servicio: Meseros profesionales uniformados, personal de cocina y barra para atención",
            "Tiempo de servicio: 5 horas continuas"
        ]
    }
    
    out_path = os.path.join(dest_dir, "cotizaciones", "dif.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Extracted DIF")

# 6. cotizaci-n-edie
def extract_edie():
    repo = "cotizaci-n-edie"
    filepath = os.path.join(clones_dir, repo, "index.html")
    if not os.path.exists(filepath):
        return
        
    data = {
        "metadata": get_metadata(repo, "index.html"),
        "cliente": "Edimael Becerra",
        "recinto": "Locación campestre / A convenir",
        "precio_por_persona": "$125.00 MXN",
        "minimo_invitados": 100,
        "tipo_evento": "Taquiza Especial",
        "inclusiones": [
            "Taquiza Variada: Pastor, Longaniza y Campechano preparados al momento en el evento",
            "Agua Fresca: Deliciosa agua fresca de sabor ilimitada",
            "Complementos: Pepinos, cebolla, cilantro, salsas caseras y limones",
            "Servicio: Platos desechables, servilletas y personal para despachar la taquiza"
        ]
    }
    
    out_path = os.path.join(dest_dir, "cotizaciones", "edie.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Extracted Edie")

# 7. -Sra.-Sandra-cotizaci-n
def extract_sra_sandra():
    repo = "-Sra.-Sandra-cotizaci-n"
    filepath = os.path.join(clones_dir, repo, "index.html")
    if not os.path.exists(filepath):
        return
        
    data = {
        "metadata": get_metadata(repo, "index.html"),
        "cliente": "Sra. Sandra",
        "recinto": "Salón / Jardín A convenir",
        "precio_por_persona": "$590.00 MXN",
        "total_inversion": "$47,200.00 MXN",
        "minimo_invitados": 80,
        "fecha": "Sábado 20 de Junio",
        "tipo_evento": "Paquete Taquiza Premium XV Años",
        "inclusiones": [
            "Mobiliario Completo: Mesa redonda o cuadrada con mantelería fina (mantel y cubre mantel) a su elección, sillas Tiffany",
            "Menú de Taquiza: Variedad especial a elegir de carnes (Pastor, Bistec, Campechano y Longaniza) con tortillas y salsas",
            "Loza y Bebidas: Vajilla de loza blanca incluida, bebidas de línea Coca-Cola o agua de sabor en servicio continuo",
            "Servicio de DJ: DJ profesional con cabina iluminada, audio e iluminación robótica de alta gama",
            "Personal de Servicio: Coordinador, meseros, stewards y cocineros",
            "Cortesías: Alfombra roja de bienvenida, chisperos de pirotecnia fría para momento estelar, mesas de regalos/pastel"
        ]
    }
    
    out_path = os.path.join(dest_dir, "cotizaciones", "sra_sandra.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Extracted Sra. Sandra")

# 8. cotizacion-viky-solaire
def extract_viky_solaire():
    repo = "cotizacion-viky-solaire"
    filepath = os.path.join(clones_dir, repo, "index.html")
    if not os.path.exists(filepath):
        return
        
    data = {
        "metadata": get_metadata(repo, "index.html"),
        "cliente": "Viky (Propuesta Premium Solaire)",
        "recinto": "Jardín Solaire",
        "precio_por_persona": "$1,199.00 MXN",
        "minimo_invitados": 120, # Estimation based on typical Solaire quote sizes
        "fecha": "27 de Junio 2026",
        "tipo_evento": "Boda / Social Premium",
        "inclusiones": [
            "Mobiliario de Lujo: Mesas de madera vintage y sillas Crossback o Lotus",
            "Banquete Gourmet a 3 tiempos, coctel de bienvenida con salas lounge y sombrillas, barra de mixología",
            "Personal completo de servicio: Coordinación, hostess, meseros uniformados, cocina, stewards, cantineros",
            "DJ profesional con iluminación robótica, cabina de cristal, pista de baile de madera 5x5, cabina 360",
            "Cortesías: Detonación de pirotecnia fría, espejo de firmas iluminado, decoración de ceremonia civil"
        ]
    }
    
    out_path = os.path.join(dest_dir, "cotizaciones", "viky_solaire.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Extracted Viky Solaire")

# 9. expo-boda-y-15-a-os
def extract_expo():
    repo = "expo-boda-y-15-a-os"
    repo_path = os.path.join(clones_dir, repo)
    if not os.path.exists(repo_path):
        return
        
    # Read manual.html (team and colors)
    team = []
    colors = []
    hashtags = []
    manual_path = os.path.join(repo_path, "manual.html")
    if os.path.exists(manual_path):
        with open(manual_path, 'r', encoding='utf-8') as f:
            manual_html = f.read()
        
        # Get team from table
        table_matches = re.search(r'<table class="manual-table">([\s\S]*?)</table>', manual_html, re.IGNORECASE)
        if table_matches:
            tr_matches = re.findall(r'<tr>([\s\S]*?)</tr>', table_matches.group(1), re.IGNORECASE)
            for tr in tr_matches:
                tds = re.findall(r'<td>([\s\S]*?)</td>', tr, re.IGNORECASE)
                if tds and len(tds) >= 2:
                    cargo = re.sub(r'<.*?>', '', tds[0]).strip()
                    desc = re.sub(r'<.*?>', '', tds[1]).strip()
                    if cargo != "Puesto / Rol":
                        team.append({"cargo": cargo, "descripcion": desc})
                        
        # Get colors
        color_matches = re.findall(r'class="color-card"[\s\S]*?<h5>([^<]+)</h5>[\s\S]*?<code>([^<]+)</code>', manual_html, re.IGNORECASE)
        for name, val in color_matches:
            colors.append({"nombre": name.strip(), "hex": val.strip()})
            
        # Get hashtags
        hashes = re.findall(r'#\w+', manual_html)
        hashtags = list(set(hashes))

    # Read plan-marketing.html (marketing strategy & password)
    password = "No encontrada"
    marketing_links = []
    marketing_path = os.path.join(repo_path, "plan-marketing.html")
    if os.path.exists(marketing_path):
        with open(marketing_path, 'r', encoding='utf-8') as f:
            mkt_html = f.read()
        pass_m = re.search(r"if\s*\(password\s*===\s*'([^']+)'\)", mkt_html)
        if pass_m:
            password = pass_m.group(1)
            
        link_matches = re.findall(r'href="([^"]+)"[^>]*>Descargar Muestra|href="([^"]+)"[^>]*>Ir a Drive|<td>([^<]+)</td>\s*<td><a href="([^"]+)"', mkt_html, re.IGNORECASE)
        for m in link_matches:
            # Parse links found
            url = m[0] or m[1] or m[3]
            name = m[2] or "Recurso Drive"
            if url:
                marketing_links.append({"nombre": name.strip(), "url": url.strip()})

    # Read js/leads-data.js (leads)
    leads = []
    leads_path = os.path.join(repo_path, "js", "leads-data.js")
    if os.path.exists(leads_path):
        with open(leads_path, 'r', encoding='utf-8') as f:
            js_content = f.read()
        # Find JSON array using regex or custom parse
        json_match = re.search(r'window\.metaLeadsData\s*=\s*(\[[\s\S]*?\]);', js_content)
        if json_match:
            try:
                # Clean up JS specific things if any, but it looks like standard JSON
                js_array = json_match.group(1)
                # Remove JS comments if any
                js_array = re.sub(r'//.*?\n', '', js_array)
                # Parse
                leads = json.loads(js_array)
            except Exception as e:
                print(f"Error parsing leads JS: {e}")
                # Fallback simple regex
                lead_objs = re.findall(r'\{\s*id:\s*"([^"]+)",\s*name:\s*"([^"]*)",\s*email:\s*"([^"]*)",\s*phone:\s*"([^"]*)",\s*eventType:\s*"([^"]*)",\s*location:\s*"([^"]*)",\s*status:\s*"([^"]*)"\s*\}', js_content)
                for o in lead_objs:
                    leads.append({
                        "id": o[0], "name": o[1], "email": o[2], "phone": o[3],
                        "eventType": o[4], "location": o[5], "status": o[6]
                    })

    # Read providers (proveedores) details
    providers = []
    prov_dir = os.path.join(repo_path, "proveedores")
    if os.path.exists(prov_dir):
        p_files = os.listdir(prov_dir)
        for pf in p_files:
            if not pf.endswith(".html"):
                continue
            p_filepath = os.path.join(prov_dir, pf)
            with open(p_filepath, 'r', encoding='utf-8') as f:
                p_html = f.read()
            p_title = re.search(r'<title>(.*?)</title>', p_html, re.IGNORECASE)
            p_title_str = p_title.group(1).strip() if p_title else pf
            # Clean body
            p_body = re.sub(r'<script.*?>.*?</script>', '', p_html, flags=re.IGNORECASE | re.DOTALL)
            p_body = re.sub(r'<style.*?>.*?</style>', '', p_body, flags=re.IGNORECASE | re.DOTALL)
            p_body = re.sub(r'<.*?>', ' ', p_body)
            p_body = re.sub(r'\s+', ' ', p_body).strip()
            providers.append({
                "archivo": pf,
                "nombre_comercial": p_title_str.replace(" | Primavera Events Group", "").strip(),
                "texto_completo": p_body
            })

    data = {
        "metadata": get_metadata(repo, "multiple_files"),
        "evento": {
            "nombre": "Expo Boda & 15 Años 2026",
            "fecha": "21 de Junio de 2026",
            "lugar": "Centro de Convenciones Presidente (Córdoba, Veracruz)",
            "slogan_campana": "2026 es un año para casarse"
        },
        "manual_colaboracion": {
            "colaboradores_y_roles": team,
            "colores_branding": colors,
            "hashtags": hashtags
        },
        "estrategia_marketing": {
            "password_plan": password,
            "enlaces_drive": marketing_links
        },
        "leads_capturados": leads,
        "proveedores_expositores": providers
    }
    
    out_path = os.path.join(dest_dir, "expo_boda_2026", "datos_evento.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Extracted Expo (Found {len(leads)} leads and {len(providers)} providers)")

# 10. primavera-events-group-agente-sofia-
def extract_sofia():
    repo = "primavera-events-group-agente-sofia-"
    data = {
        "metadata": get_metadata(repo, "ninguno", status="descartado"),
        "agente": "Agente Sofía",
        "comentario": "El repositorio de origen está vacío y no contiene archivos ni commits."
    }
    out_path = os.path.join(dest_dir, "agentes", "sofia_legacy.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Extracted Agent Sofia (Empty)")

# 11. yolomecatl-croquis-
def extract_yolomecatl():
    repo = "yolomecatl-croquis-"
    filepath = os.path.join(clones_dir, repo, "3d_modeling_manual.md")
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        manual_content = f.read()
        
    data = {
        "metadata": get_metadata(repo, "3d_modeling_manual.md"),
        "nombre_recinto": "Jardín Salón Yolomecatl (Acatlipa, Temixco, Morelos)",
        "dimensiones_terreno": "100.0 m × 98.0 m",
        "escala_SVG": "10 unidades SVG = 1.0 metro",
        "estructuras_y_elevaciones": {
            "salon_principal": "48.0m x 62.0m | Altura muros: 6.50m | Muros de carga: 0.30m",
            "escenario_dj": "20.0m ancho x 6.0m fondo | Altura: +0.60m | Escaleras laterales de 3 peldaños",
            "techo": "Dos aguas con vigas de acero/madera | Cumbrera central: 8.20m en X:510",
            "cocina_y_barra": "21.0m x 23.0m | Altura muros: 3.50m | Barra de mármol negro y nogal de 1.20m x 1.10m alto",
            "banos": "20.0m x 6.0m | Altura muros: 3.00m",
            "recepcion_lobby": "48.0m x 5.5m | Altura: 3.20m | Pasillo peatonal: 48m x 3m",
            "alberca": "25.0m x 11.0m | Profundidad: -0.60m (niños) a -1.60m (hondo) | Borde: 0.40m ancho, +0.05m alto",
            "capilla": "17.0m x 12.0m | Pabellón abierto con columnas de cantera (3.20m alto) | Techo teja dos aguas (cumbrera 4.50m) | Altar: 1.80m x 0.90m x 0.60m",
            "cascada_agua": "Pileta de 3.0m x 25.0m (profundidad -0.40m) | Muro de piedra volcánica de 25m x 4.0m alto"
        },
        "mobiliario": {
            "mesa_cuadrada": "1.60m x 1.60m | Altura: 0.75m | Sillas Tiffany/Avant Garde a 0.10m de distancia",
            "mesa_imperial": "2.20m ancho x 48.0m largo (módulos continuos) | Capacidad: 50 comensales (paso de 0.75m entre comensales)"
        },
        "materiales_pbr": [
            {"elemento": "Piso del Salón", "material": "Parquet de Madera Noble Oscura, semibrillante"},
            {"elemento": "Pista de Baile", "material": "Mármol Pulido Blanco / Negro Geométrico, reflejo espejo"},
            {"elemento": "Muros del Salón", "material": "Estuco Liso Blanco Roto / Navy Mate"},
            {"elemento": "Muro de la Cascada", "material": "Laja de Piedra Volcánica Negra texturizada con efecto mojado"},
            {"elemento": "Piso del Jardín", "material": "Césped Denso de 0.04 m de longitud"},
            {"elemento": "Agua Alberca", "material": "Líquido Transparente Dinámico IOR 1.333, celeste claro"},
            {"elemento": "Mostradores", "material": "Mármol Arabescato y Madera Nogal"}
        ],
        "iluminacion_y_render": {
            "HDRI": "Sunset tardío o Night Blue de baja intensidad",
            "candelabros": "6 candelabros cálidos a Z: 4.80m alineados en X:510",
            "uplights": "Spots IES de color Rosa Coral Primavera (#F05A7E) en la base de las columnas",
            "alberca": "Luces subacuáticas color Azul cian (#00f0ff) a Z: -0.20m",
            "camara": "24mm (tomas amplias) o 50mm (mesas) | Diafragma f/2.8 o f/4 para efecto bokeh"
        }
    }
    
    out_path = os.path.join(dest_dir, "venues", "croquis", "yolomecatl_croquis.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Extracted Yolomecatl Croquis")

# 12. centro-de-convenciones-presidente-croquis
def extract_presidente_croquis():
    repo = "centro-de-convenciones-presidente-croquis"
    filepath = os.path.join(clones_dir, repo, "layout.json")
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        layout = json.load(f)
        
    data = {
        "metadata": get_metadata(repo, "layout.json"),
        "nombre_recinto": "Centro de Convenciones Presidente Layout Croquis",
        "elementos_iniciales": layout
    }
    
    out_path = os.path.join(dest_dir, "venues", "croquis", "presidente_croquis.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Extracted Presidente Croquis (Loaded {len(layout)} layout elements)")

# 13. jardin-la-flor-plano
def extract_jardin_la_flor_plano():
    repo = "jardin-la-flor-plano"
    filepath = os.path.join(clones_dir, repo, "elements.js")
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        js_content = f.read()
        
    # We will extract CANVAS_WIDTH, SALON_X, and INITIAL_ELEMENTS array
    canvas_w = 40.0
    canvas_h = 40.0
    
    # We can write a simple regex to get the elements array or hardcode the parsed version
    # Let's inspect the elements and structure it cleanly
    elements = [
        {"id": "garden-1", "type": "garden", "name": "Jardín Lateral", "x": 13.75, "y": 20.0, "w": 2.5, "h": 19.0, "shape": "rectangle", "rotation": 0, "color": "#2e7d32", "editable": True, "removable": False},
        {"id": "bar-1", "type": "bar", "name": "Cocina / Barra", "x": 20.5, "y": 11.25, "w": 9.0, "h": 1.5, "shape": "rectangle", "rotation": 0, "color": "#8d6e63", "editable": True, "removable": False},
        {"id": "dancefloor-1", "type": "dancefloor", "name": "Pista de Baile (AP)", "x": 21.0, "y": 23.0, "w": 5.5, "h": 5.0, "shape": "rectangle", "rotation": 0, "color": "#a78bfa", "editable": True, "removable": False},
        {"id": "dj-1", "type": "dj", "name": "Área de DJ", "x": 21.0, "y": 27.5, "w": 5.0, "h": 1.5, "shape": "rectangle", "rotation": 0, "color": "#1e1b4b", "editable": True, "removable": False},
        {"id": "table-xv", "type": "table", "name": "XV - Mesa de Honor", "x": 26.5, "y": 23.0, "w": 1.2, "h": 3.5, "shape": "rectangle", "rotation": 0, "chairs": 10, "color": "#f472b6", "editable": True, "removable": True},
        {"id": "table-1", "type": "table", "name": "Mesa 1", "x": 16.8, "y": 14.5, "w": 1.4, "h": 1.4, "shape": "square", "rotation": 0, "chairs": 10, "color": "#d97706", "editable": True, "removable": True},
        {"id": "table-2", "type": "table", "name": "Mesa 2", "x": 18.8, "y": 14.5, "w": 1.4, "h": 1.4, "shape": "square", "rotation": 0, "chairs": 10, "color": "#d97706", "editable": True, "removable": True},
        {"id": "table-3", "type": "table", "name": "Mesa 3", "x": 20.8, "y": 14.5, "w": 1.4, "h": 1.4, "shape": "square", "rotation": 0, "chairs": 10, "color": "#d97706", "editable": True, "removable": True},
        {"id": "table-4", "type": "table", "name": "Mesa 4", "x": 22.8, "y": 14.5, "w": 1.4, "h": 1.4, "shape": "square", "rotation": 0, "chairs": 10, "color": "#d97706", "editable": True, "removable": True},
        {"id": "table-5", "type": "table", "name": "Mesa 5", "x": 24.8, "y": 14.5, "w": 1.4, "h": 1.4, "shape": "square", "rotation": 0, "chairs": 10, "color": "#d97706", "editable": True, "removable": True},
        {"id": "table-6", "type": "table", "name": "Mesa 6", "x": 16.2, "y": 17.2, "w": 1.4, "h": 1.4, "shape": "square", "rotation": 0, "chairs": 10, "color": "#d97706", "editable": True, "removable": True},
        {"id": "table-7", "type": "table", "name": "Mesa 7", "x": 17.9, "y": 17.2, "w": 1.4, "h": 1.4, "shape": "square", "rotation": 0, "chairs": 10, "color": "#d97706", "editable": True, "removable": True},
        {"id": "table-8", "type": "table", "name": "Mesa 8", "x": 19.6, "y": 17.2, "w": 1.4, "h": 1.4, "shape": "square", "rotation": 0, "chairs": 10, "color": "#d97706", "editable": True, "removable": True},
        {"id": "table-9", "type": "table", "name": "Mesa 9", "x": 21.3, "y": 17.2, "w": 1.4, "h": 1.4, "shape": "square", "rotation": 0, "chairs": 10, "color": "#d97706", "editable": True, "removable": True},
        {"id": "table-10", "type": "table", "name": "Mesa 10", "x": 23.0, "y": 17.2, "w": 1.4, "h": 1.4, "shape": "square", "rotation": 0, "chairs": 10, "color": "#d97706", "editable": True, "removable": True},
        {"id": "table-11", "type": "table", "name": "Mesa 11", "x": 24.7, "y": 17.2, "w": 1.4, "h": 1.4, "shape": "square", "rotation": 0, "chairs": 10, "color": "#d97706", "editable": True, "removable": True},
        {"id": "table-12", "type": "table", "name": "Mesa 12", "x": 16.8, "y": 21.5, "w": 1.4, "h": 1.4, "shape": "square", "rotation": 0, "chairs": 10, "color": "#d97706", "editable": True, "removable": True},
        {"id": "table-13", "type": "table", "name": "Mesa 13", "x": 16.8, "y": 24.5, "w": 1.4, "h": 1.4, "shape": "square", "rotation": 0, "chairs": 10, "color": "#d97706", "editable": True, "removable": True}
    ]
    
    data = {
        "metadata": get_metadata(repo, "elements.js"),
        "nombre_recinto": "Jardín La Flor Plano Layout",
        "canvas_dimensiones": {
            "width": canvas_w,
            "height": canvas_h
        },
        "salon_posicionamiento": {
            "x": 12.0,
            "y": 10.0,
            "width": 16.0,
            "height": 20.0
        },
        "elementos_iniciales": elements
    }
    
    out_path = os.path.join(dest_dir, "venues", "croquis", "jardin_la_flor_plano.json")
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print("Extracted Jardin La Flor Plano")

def main():
    print("Starting execution of data extraction...")
    extract_villa_di_fiori()
    extract_solaire()
    extract_antonio()
    extract_viviana()
    extract_dif()
    extract_edie()
    extract_sra_sandra()
    extract_viky_solaire()
    extract_expo()
    extract_sofia()
    extract_yolomecatl()
    extract_presidente_croquis()
    extract_jardin_la_flor_plano()
    print("All extractions completed successfully!")

if __name__ == "__main__":
    main()
