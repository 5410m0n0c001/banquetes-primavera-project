import os
import json

def compile_db():
    json_path = 'base_de_datos_primavera.json'
    md_path = 'base_de_datos_primavera.md'
    
    # 1. Read JSON database
    if not os.path.exists(json_path):
        print(f"Error: JSON database not found at {json_path}")
        return
        
    with open(json_path, 'r', encoding='utf-8') as f:
        database = json.load(f)
        
    # 2. Add the new creative directive if not present
    new_directive = "Buscar siempre en el sitio web e incluir la URL específica dedicada al tema de la publicación (por ejemplo: /graduaciones-primavera/ para graduaciones, /bodas/ para bodas, /quinceaneras-primavera/ para quinceañeras, /nuestros-menus/ para menús, /montajes-y-mobiliario/ para mobiliario, etc.) para redirigir el tráfico de manera segmentada, además de los enlaces globales requeridos."
    
    try:
        dc = database['plan_marketing']['campana_organica_post_evento']['manual_copywriting_aeo_seo']['directrices_creatividad']
        if new_directive not in dc:
            dc.append(new_directive)
    except KeyError as e:
        print("Warning: could not find directrices_creatividad in JSON, skipping update", e)
        
    # 3. Add the new graduation copy if not present
    post_grad_data = {
        "titulo": "Apertura de Agenda Julio - Eventos de Graduaciones Escolares y Universitarias",
        "meta_sin_enlaces": "¡El gran día está más cerca de lo que imaginas! 🎓✨ Sabemos que cada desvelada, cada examen y cada esfuerzo han valido la pena. ¡Es hora de celebrar tu graduación como te lo mereces! 🥂👑\n\nEn Primavera Events Group abrimos oficialmente la agenda de Julio para eventos de graduación. Queremos que tu gala sea una noche inolvidable, llena de elegancia, orden absoluto y la máxima diversión para ti, tus compañeros y tu familia.\n\nDesde espectaculares letras gigantes iluminadas, alfombras rojas con back fotográfico, pirotecnia fría para el brindis, hasta nuestro increíble carrito de shots y pistas Pixel LED de última tecnología... ¡Cuidamos cada detalle para crear una experiencia inolvidable! 📸💥\n\n🎁 ¡Y tenemos una sorpresa de graduación! Al reservar tu fecha con nosotros, te regalamos tu Invitación Digital Premium con confirmación de asistencia en tiempo real. Además, si quieres empezar a planificar desde hoy, tenemos de regalo nuestro Kit Planner de Excel para el control del presupuesto de tu generación.\n\n¿Listos para planear la mejor fiesta de su vida? Dejamos los enlaces de contacto y el demo de la invitación en el primer comentario de esta publicación. 👇\n\n#GraduacionesPrimavera #Graduacion2026 #EventosPremium #BanquetesPrimavera #InvitacionDigital #GalaDeGraduacion #MorelosEventos",
        "meta_comentarios": "¡Hola graduados! 🎓 Aquí tienes los accesos rápidos para planificar su gran noche:\n\n🎓 NUESTRA PÁGINA DE GRADUACIONES:\n🔗 https://primaveraeventsgroup.com/graduaciones-primavera/\n\n📦 PAQUETE GLOW GRADUATION ELITE:\n🔗 https://primaveraeventsgroup.com/paquete-glow-graduation-elite/\n\n🍽️ NUESTROS MENÚS GOURMET Y JUVENILES:\n🔗 https://primaveraeventsgroup.com/nuestros-menus/\n\n---\n\n🎁 PRUEBA LA DEMO DE NUESTRA INVITACIÓN DIGITAL PREMIUM (¡Gratis al contratar!):\n🔗 https://5410m0n0c001.github.io/invitacion-demo/\n\n---\n\n💬 ¡SOLICITA TU KIT PLANNER GRATUITO!\nComenta 'Yo lo quiero' o envíanos un mensaje privado para enviarte la plantilla de Excel para el control de gastos de tu graduación y la guía de organización por mensaje directo. 📈\n\n📲 AGENDA TU ASESORÍA PERSONALIZADA CON NUESTROS PLANNERS:\n🤵 Richard Hernández (Planner & Director Creativo):\n🔗 https://primaveraeventsgroup.com/richard-hernandez/\n👩💼 Jessy Sandoval (Planner & Fundadora):\n🔗 https://primaveraeventsgroup.com/jessy/",
        "tiktok": "🎓 ¡Abrimos agenda de Julio para graduaciones! 🥂 Celebra tu gran logro con producción premium y banquetes de lujo. Link en bio para paquetes e invitación digital premium gratis. 👑✨ #Graduaciones #FiestaDeGraduacion #Banquetes #Graduados #PrimaveraEvents",
        "twitter": "🎓 ¡Abrimos agenda de Julio para graduaciones! 🥂 Diseñamos galas espectaculares con producción premium, banquetes de gala y la mejor música. Agenda tu fecha y llévate tu invitación digital premium gratis. 👑✨ Info aquí: https://primaveraeventsgroup.com/graduaciones-primavera/ #Graduacion #Graduados"
    }
    
    try:
        cw = database['plan_marketing']['campana_organica_post_evento']['copywriting']
        cw['post_graduaciones_julio'] = post_grad_data
    except KeyError as e:
        print("Warning: could not find copywriting key in JSON", e)
        
    # Write updated database back to JSON
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(database, f, indent=2, ensure_ascii=False)
    print("Saved JSON Database successfully!")
    
    # 4. Generate Markdown
    md = []
    md.append("# 📂 Base de Conocimiento RAG - Primavera Events Group")
    md.append("> **Documento Consolidado de Paquetes, Locaciones, Servicios y Menús**")
    md.append("> *Generado de forma automatizada a partir de los datos públicos del sitio primaveraeventsgroup.com*")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 📋 Índice")
    md.append("1. [🏢 Perfil de la Empresa](#-perfil-de-la-empresa)")
    md.append("2. [📦 Paquetes de Eventos y Banquetes](#-paquetes-de-eventos-y-banquetes)")
    md.append("3. [📸 Paquetes de Fotografía y Video](#-paquetes-de-fotografía-y-video)")
    md.append("4. [🍽️ Menús y Propuestas Gastronómicas](#️-menús-y-propuestas-gastronómicas)")
    md.append("5. [🏰 Locaciones (Salones, Quintas y Jardines)](#-locaciones-salones-quintas-y-jardines)")
    md.append("6. [💡 Servicios Corporativos y Especiales](#-servicios-corporativos-y-especiales)")
    md.append("7. [📝 Ejemplos de Cotizaciones Reales y de Campo](#-ejemplos-de-cotizaciones-reales-y-de-campo)")
    md.append("8. [💬 Constantes de Interacción y Guías de Prospección Comercial](#-constantes-de-interacción-y-guías-de-prospección-comercial)")
    md.append("9. [📢 Políticas Comerciales y Promociones Especiales](#-políticas-comerciales-y-promociones-especiales)")
    md.append("10. [📰 Publicaciones del Blog y Entradas de WordPress](#-publicaciones-del-blog-y-entradas-de-wordpress)")
    md.append("11. [👥 Organigrama y Equipo de Colaboradores Reales](#-organigrama-y-equipo-de-colaboradores-reales)")
    md.append("12. [🎨 Manual de Branding e Identidad Visual y Sonora](#-manual-de-branding-e-identidad-visual-y-sonora)")
    md.append("13. [🚀 Plan Estratégico de Marketing (Campaña Mensual)](#-plan-estratégico-de-marketing-campaña-mensual)")
    md.append("14. [📈 Campaña Orgánica Post-Evento (Semana de Posicionamiento)](#-campaña-orgánica-post-evento-semana-de-posicionamiento)")
    md.append("15. [📐 Simulación, Croquis y Modelado 3D de Locaciones](#-simulación-croquis-y-modelado-3d-de-locaciones)")
    md.append("16. [📅 Estrategia e Historial de la Expo Boda y 15 Años 2026](#-estrategia-e-historial-de-la-expo-boda-y-15-años-2026)")
    md.append("17. [🤖 Historial de Agentes Conversacionales (Sofía Legacy)](#-historial-de-agentes-conversacionales-sofía-legacy)")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 🏢 Perfil de la Empresa")
    md.append("* **Nombre Comercial**: Primavera Events Group (Banquetes Primavera)")
    md.append("* **Oficina Central**: Av. Defensa Nacional #8, Col. Chamilpa, 62210 Cuernavaca, Morelos.")
    md.append("* **Directores y Planners**:")
    md.append("  * **Jessy** (Founder & Lead Planner) - Tel: `777 503 2733`")
    md.append("  * **Richard Hernández** (Creative Director & Planner) - Tel: `777 458 7923`")
    md.append("  * **Rubí Alvarado** (Gerente del Centro de Convenciones Presidente) - Tel: `271 114 8997`")
    md.append("* **Contacto**: contacto@primaveraeventsgroup.com | Tel. +52 777 458 7923")
    md.append("* **Horario**: Lunes a Viernes de 9:00 a 21:00 hrs. Domingos: Cerrado.")
    md.append("* **Lema**: *«Te cuidas tú, nos cuidas a todos»*")
    md.append("")
    md.append("---")
    md.append("")
    
    # 2. Packages
    md.append("## 📦 Paquetes de Eventos y Banquetes")
    md.append("")
    for pkg in database.get('packages', []):
        pricing = pkg.get('pricing')
        if pricing and isinstance(pricing, list):
            md.append(f"### 🌟 {pkg.get('name')}")
            md.append(f"* **Locación Predilecta / Principal**: {pkg.get('venue')}")
            md.append(f"* **Duración**: {pkg.get('duration')}")
            md.append(f"* **Página de Referencia**: [Enlace al sitio]({pkg.get('url')})")
            md.append("")
            md.append("#### 📋 Inclusiones Principales:")
            for inc in pkg.get('inclusions', []):
                md.append(f"- {inc}")
            
            menu_struct = pkg.get('menu_structure')
            if menu_struct:
                md.append("")
                md.append(f"#### 🍽️ Estructura del Menú ({menu_struct.get('type')}):")
                for det in menu_struct.get('details', []):
                    md.append(f"- {det}")
            
            md.append("")
            md.append("#### 💰 Tabla de Precios por Persona (Sujeta a escala de invitados):")
            if pricing and len(pricing) > 0 and 'venue' in pricing[0]:
                md.append("| Locación / Jardín | Rango de Invitados | Precio Standard / Especial (Costo por Persona) | Detalle |")
                md.append("| --- | --- | --- | --- |")
                for pr in pricing:
                    md.append(f"| **{pr.get('venue')}** | {pr.get('guests')} | **{pr.get('price_per_person')}** | {pr.get('details')} |")
            else:
                md.append("| Número de Invitados | Costo por Persona | Detalles y Cobertura |")
                md.append("| --- | --- | --- |")
                for pr in pricing:
                    md.append(f"| {pr.get('guests')} | **{pr.get('price_per_person')}** | {pr.get('details')} |")
            
            conditions = pkg.get('conditions')
            if conditions:
                md.append("")
                md.append("#### ⚠️ Condiciones del Paquete:")
                for cond in conditions:
                    md.append(f"- {cond}")
            md.append("")
            md.append("---")
            md.append("")

    # 3. Photography Packages
    md.append("## 📸 Paquetes de Fotografía y Video")
    md.append("")
    for pkg in database.get('packages', []):
        pricing = pkg.get('pricing')
        if pricing and isinstance(pricing, dict):
            md.append(f"### 📷 {pkg.get('name')}")
            md.append(f"* **Tipo**: {pkg.get('type')}")
            total_cost = pricing.get('total_cost') or pricing.get('option_1', {}).get('total', 'N/A')
            dep = pricing.get('booking_deposit') or pricing.get('option_1', {}).get('booking', 'N/A')
            bal = pricing.get('liquidation_balance') or pricing.get('option_1', {}).get('balance', 'N/A')
            md.append(f"* **Costo Total**: **{total_cost}**")
            md.append(f"* **Depósito de Apartado (10%)**: `{dep}`")
            md.append(f"* **Saldo a Liquidar en el Evento**: `{bal}`")
            md.append(f"* **Página de Referencia**: [Enlace al sitio]({pkg.get('url')})")
            md.append("")
            md.append("#### 💎 Inclusiones e Entregables:")
            for inc in pkg.get('inclusions', []):
                md.append(f"- {inc}")
            
            conditions = pkg.get('conditions')
            if conditions:
                md.append("")
                md.append("#### ⚠️ Sanciones y Términos:")
                for cond in conditions:
                    md.append(f"- {cond}")
            md.append("")
            md.append("---")
            md.append("")

    # 4. Menus
    md.append("## 🍽️ Menús y Propuestas Gastronómicas")
    md.append("")
    for menu in database.get('menus', []):
        md.append(f"### 🥗 {menu.get('name')}")
        md.append(f"* **Descripción**: {menu.get('description')}")
        md.append(f"* **Página de Referencia**: [Enlace al sitio]({menu.get('url')})")
        md.append("")
        
        categories = menu.get('categories')
        if categories:
            for cat_name, dishes in categories.items():
                md.append(f"#### 🔸 Seccional: {cat_name.upper().replace('_', ' ')}")
                if isinstance(dishes, list):
                    for dish in dishes:
                        if isinstance(dish, str):
                            md.append(f"- **{dish}**")
                        else:
                            md.append(f"- **{dish.get('name')}**: *{dish.get('description')}*")
                md.append("")
                
        guisados = menu.get('guisados')
        if guisados:
            for cat_name, dishes in guisados.items():
                md.append(f"#### 🔸 Guisados de {cat_name.upper()}:")
                for dish in dishes:
                    md.append(f"- **{dish}**")
                md.append("")
                
        inclusions = menu.get('inclusions')
        if inclusions:
            for cat_name, items in inclusions.items():
                md.append(f"#### 🔸 {cat_name.upper().replace('_', ' ')}:")
                for item in items:
                    md.append(f"- **{item}**")
                md.append("")
                
        options = menu.get('options')
        if options:
            md.append("#### 🔸 Opciones Disponibles:")
            for opt in options:
                md.append(f"- **{opt}**")
            md.append("")
            
        md.append("---")
        md.append("")

    # 5. Venues
    md.append("## 🏰 Locaciones (Salones, Quintas y Jardines)")
    md.append("")
    for venue in database.get('venues', []):
        md.append(f"### 🏛️ {venue.get('name')}")
        md.append(f"* **Ubicación**: {venue.get('location')}")
        md.append(f"* **Capacidad Máxima**: **{venue.get('capacity')}**")
        md.append(f"* **Estilo Arquitectónico**: {venue.get('style', 'Rústico Campestre Elegante')}")
        md.append(f"* **Página de Referencia**: [Enlace al sitio]({venue.get('url')})")
        md.append("")
        md.append("#### 🌳 Características y Facilidades del Recinto:")
        for feat in venue.get('features', []):
            md.append(f"- {feat}")
        md.append("")
        md.append("---")
        md.append("")

    # 6. Services
    md.append("## 💡 Servicios Corporativos y Especiales")
    md.append("")
    for service in database.get('services', []):
        md.append(f"### 🛠️ {service.get('name')}")
        md.append(f"* **Descripción**: {service.get('description')}")
        md.append(f"* **Página de Referencia**: [Enlace al sitio]({service.get('url')})")
        md.append("")
        md.append("#### ⚡ Características Destacadas:")
        for feat in service.get('features', []):
            md.append(f"- {feat}")
        md.append("")
        md.append("---")
        md.append("")

    # 7. Cotizaciones Reales
    md.append("## 📝 Ejemplos de Cotizaciones Reales y de Campo")
    md.append("")
    for cot in database.get('cotizaciones_reales', []):
        md.append(f"### 📄 Cotización: {cot.get('cliente')}")
        md.append(f"* **Recinto / Locación**: {cot.get('recinto')}")
        md.append(f"* **Costo por Persona**: **{cot.get('precio_por_persona')}** (Mínimo requerido: `{cot.get('minimo_invitados')} personas`)")
        if cot.get('coordinadores'):
            md.append(f"* **Coordinadores Responsables**: {cot.get('coordinadores')}")
        md.append("")
        md.append("#### 📋 Servicios e Inclusiones de la Cotización:")
        incs = cot.get('inclusiones') or cot.get('inclusions', [])
        for inc in incs:
            md.append(f"- {inc}")
        
        cortesias = cot.get('cortesias')
        if cortesias:
            md.append("")
            md.append("#### 🎁 Cortesías Especiales Incluidas:")
            for cort in cortesias:
                md.append(f"- {cort}")
                
        condiciones = cot.get('condiciones')
        if condiciones:
            md.append("")
            md.append("#### ⚠️ Condiciones Específicas:")
            for cond in condiciones:
                md.append(f"- {cond}")
        md.append("")
        md.append("---")
        md.append("")

    # 8. Constantes de Interacción
    md.append("## 💬 Constantes de Interacción y Guías de Prospección Comercial")
    md.append("> **Directrices y Guiones extraídos de la prospección activa en redes sociales (datos.txt)**")
    md.append("")
    md.append("### 📱 Guiones de Respuestas a Leads en Redes Sociales:")
    md.append("")
    for msg in database.get('constantes_interaccion', {}).get('mensajes_prospeccion', []):
        md.append(f"#### 🔹 Caso: {msg.get('tipo')}")
        md.append(f"```text\n{msg.get('guion')}\n```")
        md.append("")
        
    md.append("### 💡 Recomendación Estratégica del Wedding Planner:")
    md.append(f"* *{database.get('constantes_interaccion', {}).get('consejos_wedding_planner')}*")
    md.append("")
    md.append("---")
    md.append("")

    # 9. Politicas y Promociones
    md.append("## 📢 Políticas Comerciales y Promociones Especiales")
    md.append("")
    promo = database.get('politicas_y_promociones', {}).get('promocion_estrella', {})
    md.append(f"### 🌟 Promoción Estrella: {promo.get('nombre')}")
    md.append(f"* **Valor Comercial Estimado**: `{promo.get('valor_comercial')}`")
    md.append(f"* **Condition de Aplicación**: {promo.get('condicion')}")
    md.append("")
    md.append("#### 📋 Características Incluidas en la Invitación Digital:")
    for feat in promo.get('caracteristicas', []):
        md.append(f"- {feat}")
    md.append("")
    md.append("### 📹 Locaciones Principales con Video Publicitario Activo:")
    md.append("> Estas locaciones ya cuentan con material audiovisual propio para el impulso de campañas publicitarias pagadas y orgánicas:")
    md.append("")
    for vid in database.get('politicas_y_promociones', {}).get('locaciones_con_video', []):
        md.append(f"- **{vid}**")
    md.append("")
    md.append("### ⚠️ Políticas y Penalizaciones Críticas:")
    for pol in database.get('politicas_y_promociones', {}).get('politicas_pagos', []):
        md.append(f"- {pol}")
    md.append("")
    md.append("---")
    md.append("")

    # 10. Blog
    md.append("## 📰 Publicaciones del Blog y Entradas de WordPress")
    md.append("")
    for post in database.get('entradas_blog', []):
        md.append(f"### 🏷️ Entrada: {post.get('titulo')}")
        md.append(f"* **Página de Referencia**: [Enlace al sitio]({post.get('url')})")
        if post.get('fecha'):
            md.append(f"* **Fecha de Publicación**: {post.get('fecha')}")
        md.append(f"* **Autor**: {post.get('autor')}")
        md.append("")
        md.append("#### 📋 Resumen del Contenido:")
        md.append(f"{post.get('resumen')}")
        md.append("")
        
        inc = post.get('inclusiones')
        if inc and len(inc) > 0:
            md.append("#### ✨ Elementos Destacados:")
            for item in inc:
                md.append(f"- {item}")
            md.append("")
        md.append("---")
        md.append("")

    # 11. Colaboradores
    md.append("## 👥 Organigrama y Equipo de Colaboradores Reales")
    md.append("")
    for col in database.get('colaboradores', []):
        md.append(f"### 👤 {col.get('nombre')}")
        md.append(f"* **Cargo/Rol**: **{col.get('cargo')}**")
        md.append(f"* **Descripción**: {col.get('descripcion')}")
        md.append("")
    md.append("---")
    md.append("")

    # 12. Manual Marca
    md.append("## 🎨 Manual de Branding e Identidad Visual y Sonora")
    md.append("")
    md.append("### 🖌️ Colores Corporativos Oficiales:")
    md.append("")
    md.append("| Color | Hexadecimal | RGB | Uso Recomendado |")
    md.append("| --- | --- | --- | --- |")
    for c in database.get('manual_marca', {}).get('colores', []):
        md.append(f"| **{c.get('nombre')}** | `{c.get('hex')}` | `rgb({c.get('rgb')})` | {c.get('uso')} |")
    md.append("")
    md.append("### 🏷️ Hashtags Oficiales de Campaña:")
    for h in database.get('manual_marca', {}).get('hashtags', []):
        md.append(f"- `{h}`")
    md.append("")
    md.append("### 🎵 Pistas y Ecosistema de Identidad Sonora:")
    md.append("")
    for s in database.get('manual_marca', {}).get('identidad_sonora', []):
        md.append(f"- **Archivo**: `{s.get('pista')}` — *Uso*: {s.get('uso')}")
    md.append("")
    md.append("---")
    md.append("")

    # 13. Plan Estrategico
    md.append("## 🚀 Plan Estratégico de Marketing (Campaña Mensual)")
    md.append("")
    plan = database.get('plan_marketing', {})
    md.append(f"* **Eslogan de Campaña**: *«{plan.get('eslogan')}»*")
    md.append(f"* **Fecha Oficial del Gran Encuentro (Expo)**: **{plan.get('fecha_expo')}**")
    md.append(f"* **Contraseña Interna de Acceso al Plan**: `{plan.get('password_acceso')}`")
    md.append("")
    md.append("### 🔗 Enlaces y Utilidades Estratégicas (Google Drive):")
    md.append("")
    for lnk in plan.get('enlaces', []):
        md.append(f"- **[{lnk.get('nombre')}]({lnk.get('url')})**")
    md.append("")
    md.append("---")
    md.append("")

    # 14. Campaña Orgánica
    camp = plan.get('campana_organica_post_evento')
    if camp:
        md.append("## 📈 Campaña Orgánica Post-Evento (Semana de Posicionamiento)")
        md.append("")
        md.append(f"* **Estrategia**: {camp.get('estrategia')}")
        md.append(f"* **Regla de Publicaciones**: {camp.get('regla_enlaces_venues')}")
        md.append("")
        md.append("### 📦 Enlaces Oficiales de Primavera Events Group (Siempre Incluidos):")
        md.append("")
        eo = camp.get('enlaces_oficiales', {})
        md.append(f"- **Paquetes Integrales**: `{eo.get('paquetes')}`")
        md.append(f"- **Menús**: `{eo.get('menus')}`")
        md.append(f"- **Venues**: `{eo.get('venues')}`")
        md.append(f"- **Demo Invitación Digital**: `{eo.get('demo_invitacion')}`")
        md.append(f"- **Asesoría Richard Hernández**: `{eo.get('planner_richard')}`")
        md.append(f"- **Asesoría Jessy Sandoval**: `{eo.get('planner_jessy')}`")
        md.append(f"- **Enlace de Reseñas en Google**: `{eo.get('google_opiniones')}`")
        md.append("")
        md.append("### 📝 Copys y Guiones de Redes Sociales:")
        md.append("")
        
        for k, v in camp.get('copywriting', {}).items():
            title_prefix = "#### 🎓 Publicación: " if 'post' in k else "#### 🎬 Video: "
            md.append(f"{title_prefix}{v.get('titulo')}")
            md.append("")
            if v.get('meta_sin_enlaces'):
                md.append("##### 👥 Meta (Facebook & Instagram) - Texto Principal (Sin Enlaces):")
                md.append(f"```text\n{v.get('meta_sin_enlaces')}\n```")
                md.append("")
            if v.get('meta_comentarios'):
                md.append("##### 💬 Meta (Facebook & Instagram) - Enlace Primer Comentario:")
                md.append(f"```text\n{v.get('meta_comentarios')}\n```")
                md.append("")
            if v.get('tiktok'):
                md.append("##### 🎵 TikTok:")
                md.append(f"```text\n{v.get('tiktok')}\n```")
                md.append("")
            if v.get('twitter'):
                md.append("##### 🐦 Twitter / X:")
                md.append(f"```text\n{v.get('twitter')}\n```")
                md.append("")
            if v.get('youtube'):
                md.append("##### 🎥 YouTube (Descripción Oficial):")
                md.append(f"```text\n{v.get('youtube')}\n```")
                md.append("")
        md.append("---")
        md.append("")

    # 15. Croquis y Planos
    croq = database.get('croquis_y_planos')
    if croq:
        md.append("## 📐 Simulación, Croquis y Modelado 3D de Locaciones")
        md.append("")
        yolo = croq.get('yolomecatl')
        if yolo:
            md.append(f"### 🌿 Planificador y Modelado 3D: {yolo.get('nombre_recinto')}")
            md.append(f"* **Dimensiones del Terreno**: `{yolo.get('dimensiones_terreno')}`")
            md.append(f"* **Escala SVG**: {yolo.get('escala_SVG')}")
            md.append("")
            md.append("#### 🏢 Estructuras y Alturas (Z-axis):")
            for k, v in yolo.get('estructuras_y_elevaciones', {}).items():
                md.append(f"- **{k.replace('_', ' ').title()}**: {v}")
            md.append("")
            md.append("#### 🛋️ Especificaciones de Mobiliario:")
            for k, v in yolo.get('mobiliario', {}).items():
                md.append(f"- **{k.replace('_', ' ').title()}**: {v}")
            md.append("")
            md.append("#### 🎨 Propiedades de Materiales PBR:")
            md.append("| Elemento | Material Recomendado |")
            md.append("| --- | --- |")
            for mat in yolo.get('materiales_pbr', []):
                md.append(f"| {mat.get('elemento')} | {mat.get('material')} |")
            md.append("")
            md.append("#### 💡 Esquema de Iluminación de Gala y Render:")
            for k, v in yolo.get('iluminacion_y_render', {}).items():
                md.append(f"- **{k.replace('_', ' ').title()}**: {v}")
            md.append("")
            md.append("---")
            md.append("")
            
        flor = croq.get('jardin_la_flor')
        if flor:
            w = flor.get('canvas_dimensiones', {}).get('width')
            h = flor.get('canvas_dimensiones', {}).get('height')
            md.append(f"### 🌸 Planificador y Plano 2D/3D: {flor.get('nombre_recinto')}")
            md.append(f"* **Dimensiones del Lienzo**: `{w}m x {h}m`")
            sw = flor.get('salon_posicionamiento', {}).get('width')
            sh = flor.get('salon_posicionamiento', {}).get('height')
            md.append(f"* **Salón Posicionamiento**: Centro ({sw}m x {sh}m)")
            md.append("")
            md.append("#### 🛋️ Elementos de Distribución Inicial:")
            md.append("| ID | Elemento / Mueble | Coordenadas (X, Y) | Medidas (W x H) | Sillas | Color |")
            md.append("| --- | --- | --- | --- | --- | --- |")
            for el in flor.get('elementos_iniciales', []):
                md.append(f"| `{el.get('id')}` | {el.get('name')} ({el.get('type')}) | ({el.get('x')}, {el.get('y')}) | {el.get('w')}m x {el.get('h')}m | {el.get('chairs', 0)} | `{el.get('color')}` |")
            md.append("")
            md.append("---")
            md.append("")
            
        pres = croq.get('centro_presidente')
        if pres:
            md.append(f"### 🏛️ Planificador y Distribución: {pres.get('nombre_recinto')}")
            md.append("")
            md.append("#### 🛋️ Elementos y Layout de Stands / Expositores:")
            md.append("| ID | Nombre Elemento | Tipo | Coordenadas (X, Y) | Medidas (W x H) | Expositor |")
            md.append("| --- | --- | --- | --- | --- | --- |")
            for el in pres.get('elementos_iniciales', []):
                md.append(f"| `{el.get('id')}` | {el.get('name')} | {el.get('type')} | ({el.get('x')}, {el.get('y')}) | {el.get('w')}m x {el.get('h')}m | {el.get('exhibitor', 'N/A')} |")
            md.append("")
            md.append("---")
            md.append("")

    # 16. Expo Boda
    expo = database.get('expo_boda_2026')
    if expo:
        md.append("## 📅 Estrategia e Historial de la Expo Boda y 15 Años 2026")
        md.append("")
        md.append(f"* **Evento**: {expo.get('evento', {}).get('nombre')} ({expo.get('evento', {}).get('fecha')})")
        md.append(f"* **Locación**: {expo.get('evento', {}).get('lugar')}")
        md.append(f"* **Contraseña de Comunicación**: `{expo.get('estrategia_marketing', {}).get('password_plan')}`")
        md.append("")
        md.append("### 👥 Equipo Colaborador y Roles Oficiales:")
        for member in expo.get('manual_colaboracion', {}).get('colaboradores_y_roles', []):
            md.append(f"- **{member.get('cargo')}**: {member.get('descripcion')}")
        md.append("")
        md.append("### 🎨 Paleta de Colores de la Expo:")
        md.append("| Color | Hex |")
        md.append("| --- | --- |")
        for col in expo.get('manual_colaboracion', {}).get('colores_branding', []):
            md.append(f"| **{col.get('nombre')}** | `{col.get('hex')}` |")
        md.append("")
        hashtags = ", ".join([f"`{h}`" for h in expo.get('manual_colaboracion', {}).get('hashtags', [])])
        md.append(f"### 🏷️ Hashtags de Campaña: {hashtags}")
        md.append("")
        md.append("### 🔗 Enlaces y Descargas de Medios:")
        for lnk in expo.get('estrategia_marketing', {}).get('enlaces_drive', []):
            md.append(f"- **[{lnk.get('nombre')}]({lnk.get('url')})**")
        md.append("")
        md.append(f"### 📈 Prospectos y Leads Capturados (Total: {len(expo.get('leads_capturados', []))} leads):")
        md.append("| ID | Nombre Completo | Teléfono | Correo Electrónico | Evento | Ubicación | Estado |")
        md.append("| --- | --- | --- | --- | --- | --- | --- |")
        for lead in expo.get('leads_capturados', []):
            md.append(f"| `{lead.get('id')}` | {lead.get('name')} | {lead.get('phone')} | {lead.get('email')} | {lead.get('eventType')} | {lead.get('location')} | {lead.get('status')} |")
        md.append("")
        md.append("### 🏬 Directorio Detallado de Proveedores Expositores:")
        for prov in expo.get('proveedores_expositores', []):
            md.append(f"#### 🏢 Proveedor: {prov.get('nombre_comercial')} (Archivo: `{prov.get('archivo')}`)")
            md.append(f"{prov.get('texto_completo')}")
            md.append("")
        md.append("---")
        md.append("")

    # 17. Sofia Legacy
    sofia = database.get('agentes_conversacionales')
    if sofia:
        md.append("## 🤖 Historial de Agentes Conversacionales (Sofía Legacy)")
        md.append("")
        md.append(f"* **Agente**: {sofia.get('agente')}")
        md.append(f"* **Repositorio de Origen**: {sofia.get('metadata', {}).get('repo_origen')}")
        md.append(f"* **Estado**: {sofia.get('metadata', {}).get('estado')}")
        md.append(f"* **Comentario**: {sofia.get('comentario')}")
        md.append("")
        
    # Write MD file
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(md))
    print("Saved Markdown Database successfully!")

if __name__ == '__main__':
    compile_db()
