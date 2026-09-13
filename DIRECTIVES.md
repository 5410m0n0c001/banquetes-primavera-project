# DIRECTIVES — Primavera Events Group
### Guia Maestra Permanente · Cotizaciones Web y PDF
Ultima actualizacion: Julio 2026 · Antigravity AI Agent

---

## 1. BRANDING OBLIGATORIO

| Token            | Valor     | Uso                                        |
|------------------|-----------|--------------------------------------------|
| --primary-pink   | #F65C7A   | Color principal, botones, iconos           |
| --gold-accent    | #C9A96E   | Lineas decorativas, badges premium         |
| --primary-dark   | #1F1F1F   | Texto principal, fondos oscuros            |
| --background-light | #F8F6F4 | Fondo general de pagina                  |
| --soft-pink      | #FADADD   | Fondos suaves, badges de evento            |
| --beige          | #EFE7E1   | Bordes, separadores                        |
| --gray-text      | #6D6D6D   | Texto secundario, notas                    |

PROHIBIDO: cafe/marron, rojo/azul/verde planos, cualquier paleta fuera de Primavera.
Tipografia: Titulos = Playfair Display | Cuerpo = Poppins (Google Fonts)

---

## 2. ESTRUCTURA OBLIGATORIA DE CADA COTIZACION WEB

1. PRELOADER    - Video precarga.mp4 + boton "Haz clic para continuar"
2. HERO         - Slideshow del salon con overlay oscuro
3. HEADER INFO  - Nombre cliente, tipo evento, cajas de resumen
4. LOGO SALON   - Imagen del logo como boton-link al sitio oficial
5. GALERIA      - 3-4 fotos del salon (grid)
6. DATOS SALON  - Capacidad, direccion, telefono
7. DESGLOSE     - Tarjetas de cada servicio con imagen propia del banco
8. PRECIO       - Seccion oscura con precio destacado
9. COMPLEMENTOS - Servicios opcionales (siempre, no decir "gratis")
10. PUBLICIDAD  - 4 imagenes promo (XV, Bodas, Graduados, Planning)
11. KIT PLANNER - Descarga Excel + PDF guia
12. PDF BUTTON  - Boton window.print()
13. FIRMA       - Video firma.mp4
14. NOTAS       - Condiciones de pago + frase de cierre
15. CTA         - Boton WhatsApp
16. FOOTER      - Logo Primavera, contacto, derechos

REGLA: El cliente NO debe ver que es adaptacion de otro paquete.
REGLA: Nunca colocar notas internas de coordinacion en el HTML.

---

## 3. REGLAS DE PRECIOS

- Precio por persona cuando aplica (banquetes): precio/p + tabla por num. invitados
- Precio total cuando es servicio unico (MC, DJ solo)
- NUNCA promediar locaciones — cada locacion tiene su propio precio
- IVA: "precio neto · IVA 16% solo en factura oficial"
- Validez: 15 dias desde emision
- Anticipo: 50% para reservar · 50% un dia antes del evento

---

## 4. LOGOS COMO BOTONES — URLs

Tabla verificada contra `base_de_datos_primavera.json` y `manual_cotizaciones.md` el 2026-07-27
(auditoria previa de Antigravity contenia errores/invenciones — no confiar en reportes sin verificar cada URL).

Salon                         | URL                                                              | Estado
-------------------------------|------------------------------------------------------------------|------------------
Centro de Convenciones Presidente | https://primaveraeventsgroup.com/centro-de-convenciones-presidente/ | Activo
Quinta Zarabanda               | https://primaveraeventsgroup.com/quinta-zarabanda/               | Activo
Finca Las Isabeles             | https://primaveraeventsgroup.com/finca-las-isabeles/             | Activo
Jardin La Flor                 | https://primaveraeventsgroup.com/jardin-la-flor/                 | Activo
Jardin Tsu Nuum                | https://primaveraeventsgroup.com/jardin-tsu-nuum/                | Activo
Salon Los Potrillos (a veces "Rancho Los Potrillos" en manual_cotizaciones.md — nombre sin estandarizar) | https://primaveraeventsgroup.com/salon-los-potrillos/ | Activo
Salon Jardin Yolomecatl        | https://primaveraeventsgroup.com/salon-jardin-yolomecatl/        | Activo
Salon & Jardin Solaire         | https://primaveraeventsgroup.com/venues/solaire/                 | Activo
Villa Di Fiori (Premium)       | https://primaveraeventsgroup.com/venues/villa-di-fiori/          | Activo
Salon Los Caballos             | https://primaveraeventsgroup.com/salon-los-caballos/ | Activo (confirmado por Salo 2026-07-27; salonloscaballos.com.mx queda descartada)
Jardin San Rafael              | (baja, ya no aparece en el sitemap del sitio web)                | INACTIVO — ya no usar
Jardin San Rafael Xochitepec   | (baja, ya no aparece en el sitemap del sitio web)                | INACTIVO — ya no usar

### 4.1 Alias de nombres — MISMO venue, nombre distinto segun el contexto

El sitio web usa el nombre oficial, pero cotizaciones viejas, redes sociales y documentos de respaldo
a veces usan un nombre distinto para EL MISMO lugar (no son venues diferentes). Confirmado por Salo (2026-07-27):

- **Centro de Convenciones Presidente** (sitio web) = "Salon Presidente" (cotizaciones/redes sociales/carpeta "SALON PRESIDENTE") — mismo lugar.
- **Salon Los Caballos** = "Los Caballos" / "Jardin Cabalo" (variantes) — mismo lugar.
- **Salon Los Potrillos** = "Rancho Los Potrillos" = "Los Potrillos, Tezoyuca" = "Potrillos Acatlipa" — TODOS el mismo lugar. Confirmado por Salo: el municipio asociado puede variar entre documentos (Tezoyuca vs Acatlipa) por ambigüedad de límites administrativos/de gobierno, aunque el lugar físico sea el mismo.
- El resto de los venues (Zarabanda, Isabeles, La Flor, Tsu Nuum, Yolomecatl, Solaire, Villa Di Fiori) no tienen alias conocidos — su nombre es consistente en todas las fuentes.

**Regla general de identificacion**: el NOMBRE del venue es el identificador principal, no el municipio/ubicacion administrativa —
la misma locacion fisica puede aparecer etiquetada con distinto municipio segun el documento (limites de gobierno ambiguos).
Al consolidar datos de nuevas fuentes (respaldos, cotizaciones viejas, etc.), agrupar por nombre primero, y tratar
diferencias de municipio como posible variacion del mismo lugar antes de asumir que son venues distintos.

---

## 5. COMPLEMENTOS DISPONIBLES (SECCION OBLIGATORIA)

Siempre al final. NO decir "gratis". Son servicios opcionales pagados.

Complementos estandar (siempre):
- Fotografia y Video: https://primaveraeventsgroup.com/paquetes-de-fotografia-y-video/
- Invitacion Digital: https://5410m0n0c001.github.io/invitacion-demo/

Catalogo de complementos adicionales (segun evento):
- Maestro de Ceremonias / Animador
- Sala Lounge (si no incluido en paquete)
- Periqueras de coctel
- Maquillista y Peinadoras
- Servicio de Nineras
- Carritos de Snacks
- Cabina Inflable de Fotografia
- Magazine Photo Booth
- Decoracion con Globos
- Limusinas / Transporte
- Tienda de Merchandising
- Servicios Prehospitalarios
- Centros de Mesa Altos / Bajos (extra)

---

## 6. BANCO DE IMAGENES
Ruta: C:\Users\Lenovo\Documents\primavera brain\image_bank\

MENU Y ALIMENTOS:
  menu.png                  -> Menu / Banquete / Tiempos
  cristaleria.jpg           -> Cristaleria fina
  cuberteria_fina.jpg       -> Cuberteria / Plaque premium

MOBILIARIO:
  silla_carlota_luis_xv.jpg -> Silla Carlota / Luis XV
  mesa_campirana_1..6.jpg   -> Mesa campirana / madera rectangular
  mesa_marmol_1..12.jpg     -> Mesa tipo marmol
  centros_mesa_altos.jpg    -> Centros de mesa altos
  centros_mesa_bajos.jpg    -> Centros de mesa bajos

RECEPCION:
  sala_lounge_1.jpg         -> Sala Lounge (principal)
  sala_lounge_2.jpg         -> Sala Lounge (alternativa)
  periqueras_1.jpg          -> Periqueras de coctel
  periqueras_2.jpg          -> Periqueras (alt)
  periqueras_3.jpg          -> Periqueras (alt 2)

FOTOGRAFIA:
  fotografia_1..4.jpg       -> Servicio de fotografia y video
  cabina_inflable_foto.jpg  -> Cabina inflable de fotografia
  magazine_photo_booth.jpg  -> Magazine Photo Booth

BELLEZA Y BIENESTAR:
  maquillista_1..5.jpg      -> Maquillista y peinadoras
  nineras.jpg               -> Servicio de nineras
  prehospitalario.jpg       -> Servicios prehospitalarios

ENTRETENIMIENTO:
  maestro_ceremonias_1..3.jpg -> Maestro de ceremonias / Animador
  decoracion_globos.jpg       -> Decoracion con globos
  carritos_snacks_1.jpg       -> Carritos de snacks
  carritos_snacks_2.jpg       -> Carritos de snacks (alt)

EXTRAS:
  merchandising_1..10.jpg   -> Tienda de merchandising
  limusinas.jpg             -> Limusinas / transporte especial

ASSETS DEL SISTEMA (copiar a cada repo nuevo):
  logo_primavera.png        -> Logo Primavera Events Group
  firma.mp4                 -> Firma animada Jessy & Richard
  precarga.mp4              -> Video preloader
  marcasonora.mp3           -> Musica de fondo
  pub_boda_ensueno.png      -> Publicidad Bodas
  pub_xv_anos.png           -> Publicidad XV Anos
  pub_graduados.png         -> Publicidad Graduaciones
  pub_jessy_richard.png     -> Publicidad Wedding Planning
  smart_event_planner_pro.xlsx -> Kit Planner Excel
  guia_maestra_primavera.pdf   -> Guia Maestra PDF
  aguas_frescas.webp        -> Aguas frescas
  margaritas.webp           -> Margaritas sin alcohol
  dj.webp                   -> DJ profesional
  capitan.webp              -> Capitan de servicio (usar object-position:top)
  meseros.webp              -> Meseros uniformados
  coordinador.webp          -> Coordinacion general
  letras_gigantes.webp      -> Letras iluminadas XV/LOVE
  pista.jpg                 -> Pista de baile
  tiempo_servicio.webp      -> Tiempo de servicio / Coordinacion (reloj)
  mezcladores.png           -> Mezcladores y refrescos
  hostess.webp              -> Hostess de bienvenida
  bartender.webp            -> Barman

---

## 7. REPOS ACTIVOS

Repo                  | GitHub                                                        | Pages
----------------------|---------------------------------------------------------------|------
mariangel-cotizacion  | github.com/5410m0n0c001/cotizaci-n-Mari-ngel-campos-          | 5410m0n0c001.github.io/cotizaci-n-Mari-ngel-campos-/
caballos-cotizacion   | github.com/5410m0n0c001/cotizaci-n-carnitas-los-caballos-...  | 5410m0n0c001.github.io/cotizaci-n-carnitas-los-caballos-a-qui-n-corresponda-/
antonio-cotizacion    | github.com/5410m0n0c001/antonio-cotizacion                    | Referencia base
plantilla-base        | C:\Users\Lenovo\Documents\primavera brain\plantilla_base\     | Local

---

## 8. CONTACTO OFICIAL

Empresa:   Primavera Events Group
Web:       https://primaveraeventsgroup.com
Email:     contacto@primaveraeventsgroup.com
WhatsApp:  +52 777 458 7923
Ciudad:    Cuernavaca, Morelos, Mexico
Planners:  Jessy Sandoval (Founder & Lead Planner)
           Richard Hernandez (Director Creativo & Planner)

---

## 9. CSS PRINT — OBLIGATORIO EN TODO HTML

@media print {
  #preloader, .floating-actions-container, .pdf-section,
  .kit-buttons, .cta-container .btn-wa, audio { display:none!important; }
  .include-item, .complemento-card, .venue-info-card,
  .notes-section, .pricing-section, .kit-section {
    page-break-inside: avoid!important; break-inside: avoid!important;
  }
  h2, h3, h4, .section-title {
    page-break-after: avoid!important; break-after: avoid!important;
  }
  .include-img-container { height: 90px!important; }
  .includes-grid, .complementos-grid { display: block!important; }
  @page { margin: 1.5cm 1.2cm; }
}

---

## 10. FLUJO PARA NUEVA COTIZACION

1. Identificar salon -> obtener logo y URL oficial
2. Identificar paquete -> mapear cada servicio a imagen del banco
3. Definir precio (por persona o total, por locacion, por num. invitados)
4. Datos del cliente: nombre, tipo evento, fecha tentativa
5. Copiar plantilla_base -> renombrar repo -> personalizar
6. Servicios NO incluidos -> agregar en Complementos Disponibles
7. git push -> GitHub Pages -> compartir URL
8. PDF opcional -> generar con reportlab si se pide

---

## 11. ESTRUCTURA OBLIGATORIA ANTI-SPAM (WHATSAPP & MENSAJERÍA AUTOMÁTICA)

Para proteger la reputación de la cuenta en Meta y evitar bloqueos por marcado de SPAM, **toda respuesta automática, plantilla o mensaje de cotización/seguimiento enviado por WhatsApp a clientes o prospectos nuevos** DEBE seguir esta estructura de 4 partes:

1. **Claridad e Identificación**: Nombre del negocio/equipo desde el inicio.
2. **Atención de Valor / Información**: Entrega de la cotización o respuesta solicitada.
3. **Consentimiento (Opt-in)**: Pregunta de validación para recibir promociones/fechas por ese medio.
4. **Opción de Salida Clara (Opt-out BAJA)**: Cláusula final explícita indicando la palabra clave **BAJA** para cancelar suscripción (evitando el botón de reporte de Meta).

---

Este archivo es referencia PERMANENTE. No modificar sin instruccion explicita.
