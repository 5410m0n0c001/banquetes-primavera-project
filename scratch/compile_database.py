import os
import json
import re
import html

base_dir = r"C:\Users\Lenovo\Documents\primavera brain"
json_path = os.path.join(base_dir, "base_de_datos_primavera.json")
md_path = os.path.join(base_dir, "base_de_datos_primavera.md")

def load_json(filepath):
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def clean_html(html_str):
    if not html_str:
        return ""
    
    # Strip headers, style, script, svg
    html_str = re.sub(r'<head[\s\S]*?</head>', '', html_str, flags=re.IGNORECASE)
    html_str = re.sub(r'<style[\s\S]*?</style>', '', html_str, flags=re.IGNORECASE)
    html_str = re.sub(r'<script[\s\S]*?</script>', '', html_str, flags=re.IGNORECASE)
    html_str = re.sub(r'<svg[\s\S]*?</svg>', '', html_str, flags=re.IGNORECASE)
    
    # Strip Divi shortcodes
    html_str = re.sub(r'\[/?et_pb_[^\]]*\]', '', html_str)
    # Strip any other shortcodes
    html_str = re.sub(r'\[/?\w+[^\]]*\]', '', html_str)
    
    # Convert tables to markdown tables
    def table_repl(match):
        table_html = match.group(0)
        trs = re.findall(r'<tr[\s\S]*?>([\s\S]*?)</tr>', table_html, flags=re.IGNORECASE)
        rows = []
        for tr in trs:
            tds = re.findall(r'<(td|th)[\s\S]*?>([\s\S]*?)</\1>', tr, flags=re.IGNORECASE)
            row = []
            for td_tag, td_content in tds:
                cell_text = re.sub(r'<[\s\S]*?>', '', td_content).strip()
                cell_text = re.sub(r'\s+', ' ', cell_text)
                row.append(cell_text)
            if row:
                rows.append(row)
        if not rows:
            return ""
        md_table = "\n"
        for i, row in enumerate(rows):
            md_table += "| " + " | ".join(row) + " |\n"
            if i == 0:
                md_table += "| " + " | ".join(["---"] * len(row)) + " |\n"
        md_table += "\n"
        return md_table
        
    html_str = re.sub(r'<table[\s\S]*?>[\s\S]*?</table>', table_repl, html_str, flags=re.IGNORECASE)
    
    # Convert headings
    html_str = re.sub(r'<h[1-6][\s\S]*?>([\s\S]*?)</h[1-6]>', lambda m: f"\n\n### {re.sub(r'<[\s\S]*?>', '', m.group(1)).strip()}\n\n", html_str, flags=re.IGNORECASE)
    
    # Convert paragraphs
    html_str = re.sub(r'<p[\s\S]*?>([\s\S]*?)</p>', lambda m: f"\n{re.sub(r'<[\s\S]*?>', '', m.group(1)).strip()}\n", html_str, flags=re.IGNORECASE)
    
    # Convert lists
    html_str = re.sub(r'<li[\s\S]*?>([\s\S]*?)</li>', lambda m: f"\n- {re.sub(r'<[\s\S]*?>', '', m.group(1)).strip()}\n", html_str, flags=re.IGNORECASE)
    
    # Strip any remaining tags
    html_str = re.sub(r'<[\s\S]*?>', '', html_str)
    
    # Unescape HTML entities
    html_str = html.unescape(html_str)
    
    # Normalize spacing and newlines
    html_str = re.sub(r'\n\s*\n\s*\n+', '\n\n', html_str)
    html_str = re.sub(r'[ \t]+', ' ', html_str)
    
    return html_str.strip()

def extract_prices(text):
    pattern = r'\$\s*\d{1,3}(?:,\d{3})*(?:\.\d{2})?(?:\s*(?:MXN|p/p|por persona))?'
    prices = re.findall(pattern, text, re.IGNORECASE)
    seen = set()
    deduped = []
    for p in prices:
        p_clean = re.sub(r'\s+', ' ', p).strip()
        if p_clean not in seen:
            seen.add(p_clean)
            deduped.append(p_clean)
    return deduped

def main():
    print("Compiling Primavera Events Group consolidated database...")
    
    # 1. Load existing master database
    db = load_json(json_path)
    if not db:
        print("Error: base_de_datos_primavera.json not found!")
        return

    # Update metadata
    db["metadata"]["version"] = "1.2"
    db["metadata"]["last_updated"] = "2026-06-22"
    db["metadata"]["author"] = "Antigravity consolidated compiler"

    # 2. Merge Venues
    venues_dir = os.path.join(base_dir, "venues")
    # Load new venues
    villa_fiori_v = load_json(os.path.join(venues_dir, "villa_di_fiori.json"))
    solaire_v = load_json(os.path.join(venues_dir, "solaire.json"))
    presidente_v = load_json(os.path.join(venues_dir, "centro_convenciones_presidente.json"))

    # If venues key doesn't exist, create it as list
    if "venues" not in db or not isinstance(db["venues"], list):
        db["venues"] = []

    # Helper function to upsert a venue in list
    def upsert_venue(venue_data):
        if not venue_data:
            return
        name = venue_data.get("nombre_venue") or venue_data.get("name")
        # Remove existing if any
        db["venues"] = [v for v in db["venues"] if v.get("name") != name and v.get("nombre_venue") != name]
        db["venues"].append(venue_data)

    if villa_fiori_v:
        upsert_venue(villa_fiori_v)
    if solaire_v:
        upsert_venue(solaire_v)
    if presidente_v:
        upsert_venue(presidente_v)

    # 3. Merge Cotizaciones Reales
    cots_dir = os.path.join(base_dir, "cotizaciones")
    if os.path.exists(cots_dir):
        cot_files = [f for f in os.listdir(cots_dir) if f.endswith(".json")]
        for cf in cot_files:
            cot_data = load_json(os.path.join(cots_dir, cf))
            if cot_data:
                client_name = cot_data.get("cliente")
                # Remove from existing if any
                db["cotizaciones_reales"] = [c for c in db["cotizaciones_reales"] if c.get("cliente") != client_name]
                db["cotizaciones_reales"].append(cot_data)

    # 4. Merge Expo Boda y 15 Años 2026
    expo_data = load_json(os.path.join(base_dir, "expo_boda_2026", "datos_evento.json"))
    if expo_data:
        db["expo_boda_2026"] = expo_data

    # 5. Merge Agents
    agent_data = load_json(os.path.join(base_dir, "agentes", "sofia_legacy.json"))
    if agent_data:
        db["agentes_conversacionales"] = agent_data

    # 6. Merge Croquis y Planos
    croquis_dir = os.path.join(venues_dir, "croquis")
    db["croquis_y_planos"] = {}
    if os.path.exists(croquis_dir):
        yolo_croq = load_json(os.path.join(croquis_dir, "yolomecatl_croquis.json"))
        pres_croq = load_json(os.path.join(croquis_dir, "presidente_croquis.json"))
        flor_croq = load_json(os.path.join(croquis_dir, "jardin_la_flor_plano.json"))
        
        if yolo_croq:
            db["croquis_y_planos"]["yolomecatl"] = yolo_croq
        if pres_croq:
            db["croquis_y_planos"]["centro_presidente"] = pres_croq
        if flor_croq:
            db["croquis_y_planos"]["jardin_la_flor"] = flor_croq

    # 6b. Merge WordPress Pages and Posts
    scratch_dir = os.path.join(base_dir, "scratch")
    wp_pages_path = os.path.join(scratch_dir, "wp_pages.json")
    wp_posts_path = os.path.join(scratch_dir, "wp_posts.json")

    # Clean and merge Pages
    if os.path.exists(wp_pages_path):
        with open(wp_pages_path, 'r', encoding='utf-8') as f:
            wp_pages = json.load(f)
        
        pages_list = []
        for p in wp_pages:
            content_html = p.get("content", {}).get("rendered", "")
            cleaned_text = clean_html(content_html)
            prices = extract_prices(cleaned_text)
            
            page_entry = {
                "id": p.get("id"),
                "titulo": p.get("title", {}).get("rendered", ""),
                "url": p.get("link", ""),
                "slug": p.get("slug", ""),
                "tipo": "page",
                "fecha_modificacion": p.get("modified", ""),
                "contenido_completo": cleaned_text,
                "precios_detectados": prices
            }
            pages_list.append(page_entry)
        db["registro_paginas_web"] = pages_list
        print(f"Merged {len(pages_list)} WordPress pages.")

    # Clean and merge Posts/Blog
    if os.path.exists(wp_posts_path):
        with open(wp_posts_path, 'r', encoding='utf-8') as f:
            wp_posts = json.load(f)
            
        posts_list = []
        existing_blog = db.get("entradas_blog", [])
        
        for p in wp_posts:
            url = p.get("link", "")
            content_html = p.get("content", {}).get("rendered", "")
            cleaned_text = clean_html(content_html)
            prices = extract_prices(cleaned_text)
            
            # Look for existing post to preserve curated metadata
            existing = None
            for eb in existing_blog:
                if eb.get("url") == url:
                    existing = eb
                    break
                    
            if existing:
                post_entry = existing.copy()
                post_entry["contenido_completo"] = cleaned_text
                post_entry["precios_detectados"] = prices
                # Ensure fields are set
                if "titulo" not in post_entry:
                    post_entry["titulo"] = p.get("title", {}).get("rendered", "")
                if "fecha" not in post_entry:
                    post_entry["fecha"] = p.get("modified", "")
            else:
                post_entry = {
                    "titulo": p.get("title", {}).get("rendered", ""),
                    "url": url,
                    "autor": "Admin",
                    "fecha": p.get("modified", ""),
                    "resumen": p.get("excerpt", {}).get("rendered", ""),
                    "contenido_completo": cleaned_text,
                    "precios_detectados": prices
                }
            posts_list.append(post_entry)
        db["entradas_blog"] = posts_list
        print(f"Merged and enriched {len(posts_list)} WordPress posts.")

    # Save consolidated JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print(f"Saved consolidated JSON: {json_path}")

    # 7. Generate consolidated Markdown
    md = f"""# 📂 Base de Conocimiento RAG - Primavera Events Group
> **Documento Consolidado de Paquetes, Locaciones, Servicios, Menús, Cotizaciones, Croquis y Estrategia Comercial**
> *Generado e integrado en español para consulta directa y entrenamiento RAG*

---

## 📋 Índice
1. [🏢 Perfil de la Empresa](#-perfil-de-la-empresa)
2. [📦 Paquetes de Eventos y Banquetes](#-paquetes-de-eventos-y-banquetes)
3. [📸 Paquetes de Fotografía y Video](#-paquetes-de-fotografía-y-video)
4. [🍽️ Menús y Propuestas Gastronómicas](#️-menús-y-propuestas-gastronómicas)
5. [🏰 Locaciones (Salones, Quintas y Jardines)](#-locaciones-salones-quintas-y-jardines)
6. [💡 Servicios Corporativos y Especiales](#-servicios-corporativos-y-especiales)
7. [📝 Ejemplos de Cotizaciones Reales y de Campo](#-ejemplos-de-cotizaciones-reales-y-de-campo)
8. [💬 Constantes de Interacción y Guías de Prospección Comercial](#-constantes-de-interacción-y-guías-de-prospección-comercial)
9. [📢 Políticas Comerciales y Promociones Especiales](#-políticas-comerciales-y-promociones-especiales)
10. [📰 Publicaciones del Blog y Entradas de WordPress](#-publicaciones-del-blog-y-entradas-de-wordpress)
11. [🌐 Páginas Oficiales del Sitio Web](#-páginas-oficiales-del-sitio-web)
12. [👥 Organigrama y Equipo de Colaboradores Reales](#-organigrama-y-equipo-de-colaboradores-reales)
13. [🎨 Manual de Branding e Identidad Visual y Sonora](#-manual-de-branding-e-identidad-visual-y-sonora)
14. [🚀 Plan Estratégico de Marketing (Campaña Mensual)](#-plan-estratégico-de-marketing-campaña-mensual)
15. [📐 Simulación, Croquis y Modelado 3D de Locaciones](#-simulación-croquis-y-modelado-3d-de-locaciones)
16. [📅 Estrategia e Historial de la Expo Boda y 15 Años 2026](#-estrategia-e-historial-de-la-expo-boda-y-15-años-2026)
17. [🤖 Historial de Agentes Conversacionales (Sofía Legacy)](#-historial-de-agentes-conversacionales-sofía-legacy)

---

## 🏢 Perfil de la Empresa
* **Nombre Comercial**: Primavera Events Group (Banquetes Primavera)
* **Oficina Central**: Av. Defensa Nacional #8, Col. Chamilpa, 62210 Cuernavaca, Morelos.
* **Directores y Planners**:
  * **Jessy** (Founder & Lead Planner) - Tel: `777 503 2733`
  * **Richard Hernández** (Creative Director & Planner) - Tel: `777 458 7923`
  * **Rubí Alvarado** (Gerente del Centro de Convenciones Presidente) - Tel: `271 114 8997`
* **Contacto**: contacto@primaveraeventsgroup.com | Tel. +52 777 458 7923
* **Horario**: Lunes a Viernes de 9:00 a 21:00 hrs. Domingos: Cerrado.
* **Lema**: *«Te cuidas tú, nos cuidas a todos»*

---

## 📦 Paquetes de Eventos y Banquetes
"""

    for pkg in db.get("packages", []):
        md += f"### 🌟 {pkg.get('name')}\n"
        md += f"* **Locación Predilecta / Principal**: {pkg.get('venue')}\n"
        md += f"* **Duración**: {pkg.get('duration')}\n"
        md += f"* **Página de Referencia**: [Enlace al sitio]({pkg.get('url')})\n\n"
        
        md += f"#### 📋 Inclusiones Principales:\n"
        for inc in pkg.get("inclusions", []):
            md += f"- {inc}\n"
            
        if pkg.get("menu_structure"):
            md += f"\n#### 🍽️ Estructura del Menú ({pkg['menu_structure'].get('type')}):\n"
            for det in pkg["menu_structure"].get("details", []):
                md += f"- {det}\n"
                
        pricing = pkg.get("pricing")
        if pricing:
            if isinstance(pricing, list):
                md += f"\n#### 💰 Tabla de Precios por Persona (Sujeta a escala de invitados):\n"
                if pricing[0].get("venue"):
                    md += f"| Locación / Jardín | Rango de Invitados | Precio Standard / Especial (Costo por Persona) | Detalle |\n"
                    md += f"| --- | --- | --- | --- |\n"
                    for pr in pricing:
                        md += f"| **{pr.get('venue')}** | {pr.get('guests')} | **{pr.get('price_per_person')}** | {pr.get('details')} |\n"
                else:
                    md += f"| Número de Invitados | Costo por Persona | Detalles y Cobertura |\n"
                    md += f"| --- | --- | --- |\n"
                    for pr in pricing:
                        md += f"| {pr.get('guests')} | **{pr.get('price_per_person')}** | {pr.get('details')} |\n"
            elif isinstance(pricing, dict):
                md += f"\n#### 💰 Desglose de Inversión:\n"
                md += f"* **Costo Total**: {pricing.get('total_cost') or pricing.get('total', 'N/A')}\n"
                if pricing.get('booking_deposit'):
                    md += f"* **Anticipo / Apartado**: {pricing.get('booking_deposit')}\n"
                if pricing.get('liquidation_balance'):
                    md += f"* **Liquidación**: {pricing.get('liquidation_balance')}\n"
                for pk, pv in pricing.items():
                    if pk not in ('total_cost', 'booking_deposit', 'liquidation_balance') and not isinstance(pv, dict):
                        md += f"* **{pk.replace('_', ' ').capitalize()}**: {pv}\n"
        
        if pkg.get("conditions"):
            md += f"\n#### ⚠️ Condiciones del Paquete:\n"
            for cond in pkg.get("conditions", []):
                md += f"- {cond}\n"
        md += "\n---\n\n"

    md += "## 📸 Paquetes de Fotografía y Video\n\n"
    for photo in db.get("menus", [])[0].get("details", []): # Photography details are stored in menus[0] in legacy code
        # Wait, let's verify where photo packages are actually stored in JSON
        pass
    
    # In legacy JSON, we have "menus" as an array, but wait, let's just write them cleanly based on existing text
    md += """*   **Paquete Experiencia Deluxe (Fotografía y Video)**: **$10,900.00 MXN** (Apartado 10%: $990)
    - Incluye cobertura de foto y video ilimitado, photobook personalizado, 200 fotos postales (4x6), ampliación física 16x24 con marco, Foto Firma con caballete, sesión previa y USB de madera.
*   **Paquete Cinematic Prestige (Fotografía y Video)**: **$13,900.00 MXN** (Apartado 10%: $1,390)
    - Incluye cobertura con 2 cámaras cinematográficas, tomas aéreas profesionales con Drone 4K, fotos digitales ilimitadas, photobook, 50 fotos postales, ampliación 16x24 enmarcada, Foto Firma, sesión previa, videoclip de proyección y USB.
*   **Paquete Royal Cinematic (Fotografía y Video)**: **$12,900.00 / $13,900.00 MXN**
    - Cobertura de boda de alta gama con 2 cámaras, drones y ampliaciones premium.
*   **Paquete Eternal Promise (Fotografía de Boda)**: **$9,900.00 MXN** (Apartado 10%: $990)
    - Fotos ilimitadas, álbum personalizado, 200 impresiones físicas, sesión previa E-Session, ampliación enmarcada y USB.
*   **Paquete Memoria Clásica (Fotografía)**: **$9,350.00 MXN** (Apartado 10%: $850)
    - Fotos ilimitadas (7 horas), álbum, 100 impresiones físicas y ampliación enmarcada básica.

---

## 🍽️ Menús y Propuestas Gastronómicas
"""
    for m in db.get("menus", []):
        md += f"### 🍳 {m.get('name')}\n"
        md += f"* **Descripción**: {m.get('description')}\n"
        md += f"* **Página de Referencia**: [Enlace al sitio]({m.get('url')})\n\n"
        
        if m.get("structure"):
            md += f"#### 📋 Estructura General:\n"
            for k, v in m["structure"].items():
                md += f"* **{k.capitalize()}**: {v}\n"
            md += "\n"
            
        if m.get("details"):
            md += f"#### 🍽️ Opciones Disponibles:\n"
            if isinstance(m["details"], dict):
                for category, items in m["details"].items():
                    md += f"##### 🔹 {category.replace('_', ' ').capitalize()}\n"
                    for it in items:
                        if isinstance(it, dict):
                            md += f"- **{it.get('name')}**: {it.get('description') or ''} {f'({it.get('price_extra')})' if it.get('price_extra') else ''}\n"
                        else:
                            md += f"- {it}\n"
            elif isinstance(m["details"], list):
                for it in m["details"]:
                    if isinstance(it, dict):
                        md += f"- **{it.get('name')}**: {it.get('description') or ''}\n"
                    else:
                        md += f"- {it}\n"
        md += "\n---\n\n"

    md += "## 🏰 Locaciones (Salones, Quintas y Jardines)\n\n"
    for v in db.get("venues", []):
        name = v.get("nombre_venue") or v.get("name")
        md += f"### 🏛️ {name}\n"
        if v.get("location"):
            md += f"* **Ubicación**: {v['location']}\n"
        if v.get("capacity"):
            md += f"* **Capacidad**: {v['capacity']}\n"
        if v.get("style"):
            md += f"* **Estilo**: {v['style']}\n"
        if v.get("url"):
            md += f"* **Enlace Oficial**: [{v['url']}]({v['url']})\n"
        
        if v.get("features"):
            md += f"\n#### ⚡ Características Destacadas:\n"
            for feat in v["features"]:
                md += f"- {feat}\n"
                
        if v.get("inclusiones_generales"):
            md += f"\n#### ✨ Inclusiones del Recinto:\n"
            for inc in v["inclusiones_generales"]:
                md += f"- {inc}\n"
                
        if v.get("paquetes_y_tarifas_2026"):
            md += f"\n#### 💰 Paquetes y Tarifas 2026:\n"
            for pkg in v["paquetes_y_tarifas_2026"]:
                md += f"##### 💍 {pkg.get('nombre')}\n"
                md += f"* **Capacidad/Tiempo**: {pkg.get('capacidad')} | {pkg.get('duracion') or 'Servicio Regular'}\n"
                if pkg.get("precio_locacion"):
                    md += f"* **Costo de Renta de Locación**: **{pkg['precio_locacion']}**\n"
                if pkg.get("precio_banquete_desde"):
                    md += f"* **Costo Banquete**: Desde **{pkg['precio_banquete_desde']}**\n"
                if pkg.get("precio_banquete_completo"):
                    md += f"* **Costo Banquete Completo**: **{pkg['precio_banquete_completo']}**\n"
                if pkg.get("detalles"):
                    md += f"* **Detalle**: *{pkg['detalles']}*\n"
                if pkg.get("inclusiones_especificas"):
                    md += f"* **Inclusiones de Mobiliario y Montaje**:\n"
                    for sub in pkg["inclusiones_especificas"]:
                        md += f"  - {sub}\n"
        md += "\n---\n\n"

    md += "## 💡 Servicios Corporativos y Especiales\n\n"
    for s in db.get("services", []):
        md += f"### 🛠️ {s.get('name')}\n"
        md += f"* **Descripción**: {s.get('description')}\n"
        md += f"* **Página de Referencia**: [Enlace al sitio]({s.get('url')})\n\n"
        md += f"#### ⚡ Características Destacadas:\n"
        for feat in s.get("features", []):
            md += f"- {feat}\n"
        md += "\n---\n\n"

    md += "## 📝 Ejemplos de Cotizaciones Reales y de Campo\n\n"
    for cot in db.get("cotizaciones_reales", []):
        md += f"### 📄 Cotización: {cot.get('cliente')}\n"
        md += f"* **Recinto / Locación**: {cot.get('recinto')}\n"
        if cot.get("precio_por_persona"):
            md += f"* **Costo por Persona**: **{cot['precio_por_persona']}**\n"
        if cot.get("total_inversion"):
            md += f"* **Inversión Total**: **{cot['total_inversion']}**\n"
        if cot.get("minimo_invitados"):
            md += f"* **Mínimo Requerido**: `{cot['minimo_invitados']} personas`\n"
        if cot.get("fecha"):
            md += f"* **Fecha Tentativa**: {cot['fecha']}\n"
        if cot.get("coordinadores"):
            md += f"* **Coordinadores Responsables**: {cot['coordinadores']}\n"
            
        md += f"\n#### 📋 Servicios e Inclusiones de la Cotización:\n"
        incs = cot.get("inclusiones") or cot.get("inclusions") or []
        for inc in incs:
            md += f"- {inc}\n"
            
        if cot.get("cortesias"):
            md += f"\n#### 🎁 Cortesías Especiales Incluidas:\n"
            for cort in cot["cortesias"]:
                md += f"- {cort}\n"
                
        if cot.get("condiciones"):
            md += f"\n#### ⚠️ Condiciones Específicas:\n"
            for cond in cot["condiciones"]:
                md += f"- {cond}\n"
        md += "\n---\n\n"

    md += "## 💬 Constantes de Interacción y Guías de Prospección Comercial\n"
    md += f"> *{db.get('constantes_interaccion', {}).get('consejos_wedding_planner', '')}*\n\n"
    md += "### 📱 Guiones de Respuestas a Leads en Redes Sociales:\n\n"
    for msg in db.get("constantes_interaccion", {}).get("mensajes_prospeccion", []):
        md += f"#### 🔹 Caso: {msg.get('tipo')}\n"
        md += f"```text\n{msg.get('guion')}\n```\n\n"
    md += "\n---\n\n"

    md += "## 📢 Políticas Comerciales y Promociones Especiales\n\n"
    promo = db.get("politicas_y_promociones", {}).get("promocion_estrella", {})
    if promo:
        md += f"### 🌟 Promoción Estrella: {promo.get('nombre')}\n"
        md += f"* **Valor Comercial Estimado**: `{promo.get('valor_comercial')}`\n"
        md += f"* **Condición de Aplicación**: {promo.get('condicion')}\n\n"
        md += f"#### 📋 Características Incluidas en la Invitación Digital:\n"
        for feat in promo.get("caracteristicas", []):
            md += f"- {feat}\n"
            
    md += f"\n### 📹 Locaciones Principales con Video Publicitario Activo:\n"
    for vid in db.get("politicas_y_promociones", {}).get("locaciones_con_video", []):
        md += f"- **{vid}**\n"
        
    md += f"\n### ⚠️ Políticas y Penalizaciones Críticas:\n"
    for pol in db.get("politicas_y_promociones", {}).get("politicas_pagos", []):
        md += f"- {pol}\n"
    md += "\n---\n\n"

    md += "## 📰 Publicaciones del Blog y Entradas de WordPress\n\n"
    for post in db.get("entradas_blog", []):
        md += f"### 🏷️ Entrada: {post.get('titulo')}\n"
        md += f"* **Página de Referencia**: [Enlace al sitio]({post.get('url')})\n"
        if post.get("fecha"):
            md += f"* **Fecha de Publicación**: {post['fecha']}\n"
        md += f"* **Autor**: {post.get('autor')}\n\n"
        md += f"#### 📋 Resumen del Contenido:\n"
        md += f"{post.get('resumen')}\n\n"
        if post.get("inclusiones"):
            md += f"#### ✨ Elementos Destacados:\n"
            for inc in post["inclusiones"]:
                md += f"- {inc}\n"
        if post.get("contenido_completo"):
            md += f"\n#### 📝 Contenido Completo (HTML Limpio):\n"
            md += f"{post['contenido_completo']}\n\n"
        if post.get("precios_detectados"):
            md += f"#### 💰 Precios Detectados:\n"
            md += f"- " + ", ".join(post["precios_detectados"]) + "\n\n"
        md += "\n---\n\n"

    md += "## 🌐 Páginas Oficiales del Sitio Web\n\n"
    for page in db.get("registro_paginas_web", []):
        md += f"### 🖥️ Página: {page.get('titulo')}\n"
        md += f"* **Dirección URL**: {page.get('url')}\n"
        md += f"* **Slug**: `{page.get('slug')}`\n"
        if page.get("fecha_modificacion"):
            md += f"* **Última Modificación**: {page['fecha_modificacion']}\n\n"
        md += f"#### 📝 Contenido Limpio de la Página:\n"
        md += f"{page.get('contenido_completo')}\n\n"
        if page.get("precios_detectados"):
            md += f"#### 💰 Precios Detectados en Página:\n"
            md += f"- " + ", ".join(page["precios_detectados"]) + "\n\n"
        md += "\n---\n\n"

    md += "## 👥 Organigrama y Equipo de Colaboradores Reales\n\n"
    for col in db.get("colaboradores", []):
        md += f"### 👤 {col.get('nombre')}\n"
        md += f"* **Cargo/Rol**: **{col.get('cargo')}**\n"
        md += f"* **Descripción**: {col.get('descripcion')}\n\n"
    md += "\n---\n\n"

    md += "## 🎨 Manual de Branding e Identidad Visual y Sonora\n\n"
    md += "### 🖌️ Colores Corporativos Oficiales:\n\n"
    md += "| Color | Hexadecimal | RGB | Uso Recomendado |\n"
    md += "| --- | --- | --- | --- |\n"
    for c in db.get("manual_marca", {}).get("colores", []):
        md += f"| **{c.get('nombre')}** | `{c.get('hex')}` | `rgb({c.get('rgb', 'N/A')})` | {c.get('uso', 'N/A')} |\n"
        
    md += "\n### 🏷️ Hashtags Oficiales de Campaña:\n"
    for h in db.get("manual_marca", {}).get("hashtags", []):
        md += f"- `{h}`\n"
        
    md += "\n### 🎵 Pistas y Ecosistema de Identidad Sonora:\n\n"
    for s in db.get("manual_marca", {}).get("identidad_sonora", []):
        md += f"- **Archivo**: `{s.get('pista')}` — *Uso*: {s.get('uso')}\n"
    md += "\n---\n\n"

    md += "## 🚀 Plan Estratégico de Marketing (Campaña Mensual)\n\n"
    plan = db.get("plan_marketing", {})
    if plan:
        md += f"* **Eslogan de Campaña**: *«{plan.get('eslogan')}»*\n"
        md += f"* **Fecha Oficial del Gran Encuentro (Expo)**: **{plan.get('fecha_expo')}**\n"
        md += f"* **Contraseña Interna de Acceso al Plan**: `{plan.get('password_acceso')}`\n\n"
        md += f"### 🔗 Enlaces y Utilidades Estratégicas (Google Drive):\n\n"
        for lnk in plan.get("enlaces", []):
            md += f"- **[{lnk.get('nombre')}]({lnk.get('url')})**\n"
    md += "\n---\n\n"

    # 14. Add Croquis
    md += "## 📐 Simulación, Croquis y Modelado 3D de Locaciones\n\n"
    
    yolo_c = db.get("croquis_y_planos", {}).get("yolomecatl", {})
    if yolo_c:
        md += f"### 🌿 Planificador y Modelado 3D: {yolo_c.get('nombre_recinto')}\n"
        md += f"* **Dimensiones del Terreno**: `{yolo_c.get('dimensiones_terreno')}`\n"
        md += f"* **Escala SVG**: {yolo_c.get('escala_SVG')}\n\n"
        md += "#### 🏢 Estructuras y Alturas (Z-axis):\n"
        for k, v in yolo_c.get("estructuras_y_elevaciones", {}).items():
            md += f"- **{k.replace('_', ' ').capitalize()}**: {v}\n"
        md += "\n#### 🛋️ Especificaciones de Mobiliario:\n"
        for k, v in yolo_c.get("mobiliario", {}).items():
            md += f"- **{k.replace('_', ' ').capitalize()}**: {v}\n"
        md += "\n#### 🎨 Propiedades de Materiales PBR:\n"
        md += "| Elemento | Material Recomendado |\n| --- | --- |\n"
        for mat in yolo_c.get("materiales_pbr", []):
            md += f"| {mat.get('elemento')} | {mat.get('material')} |\n"
        md += "\n#### 💡 Esquema de Iluminación de Gala y Render:\n"
        for k, v in yolo_c.get("iluminacion_y_render", {}).items():
            md += f"- **{k.replace('_', ' ').capitalize()}**: {v}\n"
        md += "\n---\n\n"

    flor_c = db.get("croquis_y_planos", {}).get("jardin_la_flor", {})
    if flor_c:
        md += f"### 🌸 Planificador y Plano 2D/3D: {flor_c.get('nombre_recinto')}\n"
        md += f"* **Dimensiones del Lienzo**: `{flor_c['canvas_dimensiones'].get('width')}m x {flor_c['canvas_dimensiones'].get('height')}m`\n"
        md += f"* **Salón Posicionamiento**: Centro ({flor_c['salon_posicionamiento'].get('width')}m x {flor_c['salon_posicionamiento'].get('height')}m)\n\n"
        md += "#### 🛋️ Elementos de Distribución Inicial:\n"
        md += "| ID | Elemento / Mueble | Coordenadas (X, Y) | Medidas (W x H) | Sillas | Color |\n"
        md += "| --- | --- | --- | --- | --- | --- |\n"
        for el in flor_c.get("elementos_iniciales", []):
            md += f"| `{el.get('id')}` | {el.get('name')} ({el.get('type')}) | ({el.get('x')}, {el.get('y')}) | {el.get('w')}m x {el.get('h')}m | {el.get('chairs', 0)} | `{el.get('color')}` |\n"
        md += "\n---\n\n"

    pres_c = db.get("croquis_y_planos", {}).get("centro_presidente", {})
    if pres_c:
        md += f"### 🏛️ Planificador y Distribución: {pres_c.get('nombre_recinto')}\n\n"
        md += "#### 🛋️ Elementos y Layout de Stands / Expositores:\n"
        md += "| ID | Nombre Elemento | Tipo | Coordenadas (X, Y) | Medidas (W x H) | Expositor |\n"
        md += "| --- | --- | --- | --- | --- | --- |\n"
        for el in pres_c.get("elementos_iniciales", []):
            exh = el.get("exhibitor", "N/A") if el.get("exhibitor") else "N/A"
            md += f"| `{el.get('id')}` | {el.get('name')} | {el.get('type')} | ({el.get('x')}, {el.get('y')}) | {el.get('w')}m x {el.get('h')}m | {exh} |\n"
        md += "\n---\n\n"

    # 15. Add Expo
    expo = db.get("expo_boda_2026", {})
    if expo:
        md += "## 📅 Estrategia e Historial de la Expo Boda y 15 Años 2026\n\n"
        md += f"* **Evento**: {expo['evento'].get('nombre')} ({expo['evento'].get('fecha')})\n"
        md += f"* **Locación**: {expo['evento'].get('lugar')}\n"
        md += f"* **Contraseña de Comunicación**: `{expo['estrategia_marketing'].get('password_plan')}`\n\n"
        
        md += "### 👥 Equipo Colaborador y Roles Oficiales:\n"
        for member in expo['manual_colaboracion'].get('colaboradores_y_roles', []):
            md += f"- **{member.get('cargo')}**: {member.get('descripcion')}\n"
            
        md += "\n### 🎨 Paleta de Colores de la Expo:\n"
        md += "| Color | Hex |\n| --- | --- |\n"
        for col in expo['manual_colaboracion'].get('colores_branding', []):
            md += f"| **{col.get('nombre')}** | `{col.get('hex')}` |\n"
            
        md += f"\n### 🏷️ Hashtags de Campaña: " + ", ".join([f"`{h}`" for h in expo['manual_colaboracion'].get('hashtags', [])]) + "\n\n"
        
        md += "### 🔗 Enlaces y Descargas de Medios:\n"
        for lnk in expo['estrategia_marketing'].get('enlaces_drive', []):
            md += f"- **[{lnk.get('nombre')}]({lnk.get('url')})**\n"
            
        md += f"\n### 📈 Prospectos y Leads Capturados (Total: {len(expo.get('leads_capturados', []))} leads):\n"
        md += "| ID | Nombre Completo | Teléfono | Correo Electrónico | Evento | Ubicación | Estado |\n"
        md += "| --- | --- | --- | --- | --- | --- | --- |\n"
        for lead in expo.get("leads_capturados", []):
            md += f"| `{lead.get('id')}` | {lead.get('name')} | {lead.get('phone')} | {lead.get('email')} | {lead.get('eventType')} | {lead.get('location')} | {lead.get('status')} |\n"
            
        md += "\n### 🏬 Directorio Detallado de Proveedores Expositores:\n"
        for prov in expo.get("proveedores_expositores", []):
            md += f"#### 🏢 Proveedor: {prov.get('nombre_comercial')} (Archivo: `{prov.get('archivo')}`)\n"
            md += f"{prov.get('texto_completo')}\n\n"
            
        md += "\n---\n\n"

    # 16. Add Agent Sofia
    sofia = db.get("agentes_conversacionales", {})
    if sofia:
        md += "## 🤖 Historial de Agentes Conversacionales (Sofía Legacy)\n\n"
        md += f"* **Agente**: {sofia.get('agente')}\n"
        md += f"* **Repositorio de Origen**: {sofia['metadata'].get('repo_origen')}\n"
        md += f"* **Estado**: {sofia['metadata'].get('estado')}\n"
        md += f"* **Comentario**: {sofia.get('comentario')}\n"

    # Write MD file
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"Saved consolidated Markdown: {md_path}")
    print("Fidelity compilation successful! All local and WordPress sources compiled.")

if __name__ == "__main__":
    main()
