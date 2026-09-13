import os
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image, KeepTogether
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

pdf_dir        = r"C:\Users\Lenovo\Documents\primavera brain"
artifact_dir   = r"C:\Users\Lenovo\.gemini\antigravity\brain\ea456458-da0e-423d-83aa-e3df5e91c057"
logo_path      = r"C:\Users\Lenovo\Downloads\Sin título - 12 de marzo de 2026, 02.23.12 (2).png"

# ── Outputs ──────────────────────────────────────────────────
PDF_MARIANGEL_WS  = os.path.join(pdf_dir,       "cotizacion_mariangel_campos.pdf")
PDF_MARIANGEL_ART = os.path.join(artifact_dir,  "cotizacion_mariangel_campos.pdf")
PDF_CABALLOS_WS   = os.path.join(pdf_dir,       "cotizacion_caballos_carnitas.pdf")
PDF_CABALLOS_ART  = os.path.join(artifact_dir,  "cotizacion_caballos_carnitas.pdf")

# ── Branded canvas ────────────────────────────────────────────
class BrandedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self._draw_brand(total)
            super().showPage()
        super().save()

    def _draw_brand(self, total):
        self.saveState()
        # Top pink banner
        self.setFillColor(colors.HexColor('#F65C7A'))
        self.rect(36, 756, 540, 14, fill=True, stroke=False)
        self.setFillColor(colors.white)
        self.setFont("Helvetica-Bold", 7.5)
        self.drawString(46, 760, "PRIMAVERA EVENTS GROUP  |  EL ARTE DE SERVIR")
        # Gold bottom line
        self.setStrokeColor(colors.HexColor('#C9A96E'))
        self.setLineWidth(1)
        self.line(36, 54, 576, 54)
        # Footer text
        self.setFont("Helvetica", 7.5)
        self.setFillColor(colors.HexColor('#6D6D6D'))
        self.drawString(36, 40, "contacto@primaveraeventsgroup.com  |  +52 777 458 7923  |  Cuernavaca, Morelos")
        self.drawRightString(576, 40, f"Página {self._pageNumber} de {total}")
        self.restoreState()

# ── Shared styles ─────────────────────────────────────────────
def get_styles():
    base = getSampleStyleSheet()
    PINK  = colors.HexColor('#F65C7A')
    GOLD  = colors.HexColor('#C9A96E')
    DARK  = colors.HexColor('#1F1F1F')
    GRAY  = colors.HexColor('#6D6D6D')
    LGRAY = colors.HexColor('#F8F6F4')

    title = ParagraphStyle('title', parent=base['Normal'],
        fontName='Helvetica-Bold', fontSize=22, leading=26,
        textColor=PINK, spaceAfter=3)
    subtitle = ParagraphStyle('subtitle', parent=base['Normal'],
        fontName='Helvetica-Bold', fontSize=10, leading=13,
        textColor=GOLD, spaceAfter=5)
    heading = ParagraphStyle('heading', parent=base['Normal'],
        fontName='Helvetica-Bold', fontSize=13, leading=16,
        textColor=DARK, spaceBefore=14, spaceAfter=6)
    subheading = ParagraphStyle('subheading', parent=base['Normal'],
        fontName='Helvetica-Bold', fontSize=10, leading=13,
        textColor=PINK, spaceBefore=8, spaceAfter=4)
    body = ParagraphStyle('body', parent=base['Normal'],
        fontName='Helvetica', fontSize=9.5, leading=13, textColor=DARK)
    body_bold = ParagraphStyle('body_bold', parent=body, fontName='Helvetica-Bold')
    meta = ParagraphStyle('meta', parent=base['Normal'],
        fontName='Helvetica', fontSize=9, leading=12, textColor=GRAY)
    th = ParagraphStyle('th', parent=base['Normal'],
        fontName='Helvetica-Bold', fontSize=9, leading=11, textColor=colors.white)
    td = ParagraphStyle('td', parent=base['Normal'],
        fontName='Helvetica', fontSize=9, leading=12, textColor=DARK)
    td_bold = ParagraphStyle('td_bold', parent=td, fontName='Helvetica-Bold')
    small = ParagraphStyle('small', parent=base['Normal'],
        fontName='Helvetica', fontSize=8, leading=11, textColor=GRAY)
    phrase = ParagraphStyle('phrase', parent=base['Normal'],
        fontName='Helvetica-Oblique', fontSize=10, leading=14,
        textColor=PINK, alignment=1, spaceBefore=10)
    sig = ParagraphStyle('sig', parent=body, alignment=1)

    return dict(title=title, subtitle=subtitle, heading=heading,
                subheading=subheading, body=body, body_bold=body_bold,
                meta=meta, th=th, td=td, td_bold=td_bold,
                small=small, phrase=phrase, sig=sig,
                PINK=PINK, GOLD=GOLD, DARK=DARK, GRAY=GRAY, LGRAY=LGRAY)

# ── Shared header builder ─────────────────────────────────────
def build_header(story, s, client_name, event_type, location, notes=""):
    # Logo + title
    titles_col = [
        Paragraph("COTIZACIÓN DE SERVICIOS", s['title']),
        Paragraph("PRIMAVERA EVENTS GROUP  —  EL ARTE DE SERVIR", s['subtitle']),
    ]
    if os.path.exists(logo_path):
        logo_img = Image(logo_path, width=68, height=68)
        ht = Table([[logo_img, titles_col]], colWidths=[78, 462])
        ht.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING',  (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING',   (0,0), (-1,-1), 0),
            ('BOTTOMPADDING',(0,0), (-1,-1), 10),
        ]))
        story.append(ht)
    else:
        story += titles_col
        story.append(Spacer(1, 10))

    today = datetime.date.today()
    valid = today + datetime.timedelta(days=15)
    meta_l = [
        Paragraph(f"<b>Dirigido a:</b> {client_name}", s['body']),
        Paragraph(f"<b>Tipo de Evento:</b> {event_type}", s['body']),
        Paragraph(f"<b>Ubicación:</b> {location}", s['body']),
    ]
    if notes:
        meta_l.append(Paragraph(f"<b>Notas:</b> {notes}", s['body']))

    meta_r = [
        Paragraph(f"<b>Fecha de Emisión:</b> {today.strftime('%d / %m / %Y')}", s['body']),
        Paragraph(f"<b>Validez:</b> {valid.strftime('%d / %m / %Y')} (15 días)", s['body']),
        Paragraph("<b>Coordinadores:</b> Richard Hernández &amp; Jessy Sandoval", s['body']),
        Paragraph("<b>Tel.:</b> +52 777 458 7923", s['body']),
    ]
    rows = [[meta_l[i] if i < len(meta_l) else Paragraph("", s['body']),
             meta_r[i] if i < len(meta_r) else Paragraph("", s['body'])]
            for i in range(max(len(meta_l), len(meta_r)))]
    mt = Table(rows, colWidths=[270, 270])
    mt.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING',    (0,0), (-1,-1), 4),
        ('LEFTPADDING',   (0,0), (-1,-1), 0),
        ('RIGHTPADDING',  (0,0), (-1,-1), 0),
    ]))
    story.append(mt)
    story.append(Spacer(1, 14))

# ── Shared totals + signature ─────────────────────────────────
def build_totals_and_sig(story, s, rows_total, conditions_extra=""):
    total_neto = sum(r[3] for r in rows_total)
    iva        = total_neto * 0.16
    grand      = total_neto + iva

    conds = (
        "• 50% de anticipo para reservar la fecha del evento.<br/>"
        "• 50% restante a liquidar un día antes del evento.<br/>"
        "• Precios netos · IVA del 16% aplica sólo en caso de factura oficial.<br/>"
        "• Precios sujetos a cambios sin previo aviso."
    )
    if conditions_extra:
        conds += f"<br/>• {conditions_extra}"

    totals_right = Table([
        [Paragraph("<b>Subtotal:</b>",   s['td']), Paragraph(f"<b>${total_neto:,.2f} MXN</b>",  s['td'])],
        [Paragraph("<font color='#6D6D6D'>I.V.A. (16%):</font>",  s['td']), Paragraph(f"<font color='#6D6D6D'>${iva:,.2f} MXN</font>", s['td'])],
        [Paragraph("<b>Total Neto:</b>", s['td_bold']), Paragraph(f"<b>${grand:,.2f} MXN</b>",  s['td_bold'])],
    ], colWidths=[95, 105])
    totals_right.setStyle(TableStyle([
        ('ALIGN', (1,0), (1,-1), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING',    (0,0), (-1,-1), 5),
        ('LINEBELOW', (0,0), (-1,1), 0.5, colors.HexColor('#E5E5E5')),
    ]))
    tot_outer = Table([[Paragraph(conds, s['meta']), totals_right]], colWidths=[330, 210])
    tot_outer.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING',  (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(tot_outer)
    story.append(Spacer(1, 36))

    # Signatures
    sig_data = [[
        Paragraph("_______________________________<br/><b>Richard Hernández</b><br/><font color='#6D6D6D'>Director Creativo &amp; Planner</font>", s['sig']),
        Paragraph("_______________________________<br/><b>Jessy Sandoval</b><br/><font color='#6D6D6D'>Founder &amp; Lead Planner</font>", s['sig']),
    ]]
    sig_tbl = Table(sig_data, colWidths=[270, 270])
    sig_tbl.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('TOPPADDING', (0,0), (-1,-1), 10)]))
    story.append(sig_tbl)

    story.append(Spacer(1, 20))
    story.append(Paragraph("«Hacemos de tu celebración un recuerdo eterno. El arte de servir, hecho realidad.»", s['phrase']))

# ── Items table builder ───────────────────────────────────────
def build_items_table(story, s, rows):
    """
    rows = list of dicts: {concepto, descripcion, cant, unit, total}
    total as numeric for sum
    """
    headers = [
        Paragraph("Concepto",                      s['th']),
        Paragraph("Descripción y Especificaciones", s['th']),
        Paragraph("Cant.",                          s['th']),
        Paragraph("P. Unit.",                       s['th']),
        Paragraph("Total",                          s['th']),
    ]
    data = [headers]
    fill_colors = [colors.white, colors.HexColor('#FFF5F6')]
    for i, r in enumerate(rows):
        data.append([
            Paragraph(f"<b>{r['concepto']}</b>", s['td']),
            Paragraph(r['descripcion'],           s['td']),
            Paragraph(str(r['cant']),              s['td']),
            Paragraph(f"${r['unit']:,.2f}",        s['td']),
            Paragraph(f"${r['total']:,.2f}",       s['td']),
        ])
    tbl = Table(data, colWidths=[110, 232, 46, 70, 82])
    row_colors = []
    for i in range(1, len(data)):
        bg = fill_colors[(i-1) % 2]
        row_colors.append(('BACKGROUND', (0,i), (-1,i), bg))
    tbl.setStyle(TableStyle([
        ('BACKGROUND',   (0,0), (-1,0), s['PINK']),
        ('VALIGN',       (0,0), (-1,-1), 'TOP'),
        ('GRID',         (0,0), (-1,-1), 0.4, colors.HexColor('#E5E5E5')),
        ('BOTTOMPADDING',(0,0), (-1,-1), 7),
        ('TOPPADDING',   (0,0), (-1,-1), 7),
        ('ALIGN',        (2,0), (-1,-1), 'CENTER'),
    ] + row_colors))
    story.append(tbl)
    story.append(Spacer(1, 14))


# ══════════════════════════════════════════════════════════════
#  PDF 1 — MARIANGEL CAMPOS (Boda)
# ══════════════════════════════════════════════════════════════
def build_mariangel(path):
    doc = SimpleDocTemplate(path, pagesize=letter,
        leftMargin=36, rightMargin=36, topMargin=62, bottomMargin=74)
    s = get_styles()
    story = []

    build_header(story, s,
        client_name = "Mariangel Campos",
        event_type  = "Boda Premium en Jardín",
        location    = "Jiutepec, Morelos",
        notes       = "200–250 invitados · Feb/Mar 2027 · Con jardín y agua natural")

    story.append(Paragraph("Detalle del Paquete — Esencia Floral", s['heading']))
    story.append(HRFlowable(width="100%", thickness=1,
        color=colors.HexColor('#C9A96E'), spaceAfter=10))

    rows = [
        dict(concepto="Sillería Luis XV y Carlota",
             descripcion="Sillas de gala estilo Luis XV y Carlota en combinación elegante. Mesas campiranas de madera, cuadradas y tipo mármol. Montaje de gala con alfombra roja de entrada.",
             cant="1 Serv.", unit=0, total=0),
        dict(concepto="Mesa Principal de Novios",
             descripcion="Templete de madera con mesa de honor. Sillones Rey & Reyna. Mantelería fina y centros de mesa florales altos y bajos con flor natural de temporada.",
             cant="1 Serv.", unit=0, total=0),
        dict(concepto="Vajilla Fina y Plaque Premium",
             descripcion="Loza blanca de alta calidad, plato base decorativo, cubertería premium plata/oro/gold rose, cristalería con copas de color y transparentes.",
             cant="1 Serv.", unit=0, total=0),
        dict(concepto="Cóctel de Bienvenida",
             descripcion="Recepción VIP con periqueras, salas lounge. Margaritas de sabores, piñada y mojito sin alcohol. Agua fresca natural, crudités con miguelito y chamoy.",
             cant="1 Serv.", unit=0, total=0),
        dict(concepto="Banquete 4 Tiempos",
             descripcion="Entrada (ensalada/crema) · Plato Fuerte (pollo o cerdo + 2 guarniciones) · Tornafiesta (esquites o chilaquiles 60%) · Menú infantil incluido.",
             cant="1 Serv.", unit=0, total=0),
        dict(concepto="Mezcladores Completos",
             descripcion="Hielo en cubo purificado · Refrescos Coca-Cola, manzanita, toronja, agua mineral · Limón, sal y desechables.",
             cant="1 Serv.", unit=0, total=0),
        dict(concepto="DJ y Producción Audio-Visual",
             descripcion="DJ profesional, cabina, audio premium, iluminación LED, cabezas robóticas, pantalla con proyector, micrófonos inalámbricos, máquina de humo y 2 chisperos a control remoto.",
             cant="1 Serv.", unit=0, total=0),
        dict(concepto="Coordinación General",
             descripcion="Coordinador del minuto a minuto, croquis de distribución, chat exclusivo WhatsApp y acompañamiento integral antes, durante y después del evento.",
             cant="1 Serv.", unit=0, total=0),
        dict(concepto="Staff Completo Uniformado",
             descripcion="Capitán de meseros, meseros, barman, personal de cocina, hostess de bienvenida y personal de sanitarios. Todo el equipo uniformado y capacitado.",
             cant="1 Serv.", unit=0, total=0),
        dict(concepto='Letras Gigantes "LOVE" iluminadas',
             descripcion="Letras LOVE iluminadas decorativas · Mesa especial para pastel y regalos · 2 chisperos de pirotecnia en frío para el primer vals.",
             cant="1 Serv.", unit=0, total=0),
    ]

    # Build items table without unit prices (package price shown below)
    headers = [
        Paragraph("Concepto",          s['th']),
        Paragraph("Descripción",       s['th']),
        Paragraph("Incluye",           s['th']),
    ]
    data = [headers]
    fill_colors = [colors.white, colors.HexColor('#FFF5F6')]
    checks = ["✓ Incluido"] * len(rows)
    for i, r in enumerate(rows):
        data.append([
            Paragraph(f"<b>{r['concepto']}</b>", s['td']),
            Paragraph(r['descripcion'],           s['td']),
            Paragraph("<b>✓ Incluido</b>",        s['td']),
        ])
    tbl = Table(data, colWidths=[150, 330, 60])
    row_colors = []
    for i in range(1, len(data)):
        bg = fill_colors[(i-1) % 2]
        row_colors.append(('BACKGROUND', (0,i), (-1,i), bg))
    tbl.setStyle(TableStyle([
        ('BACKGROUND',   (0,0), (-1,0), colors.HexColor('#F65C7A')),
        ('VALIGN',       (0,0), (-1,-1), 'TOP'),
        ('GRID',         (0,0), (-1,-1), 0.4, colors.HexColor('#E5E5E5')),
        ('BOTTOMPADDING',(0,0), (-1,-1), 7),
        ('TOPPADDING',   (0,0), (-1,-1), 7),
        ('ALIGN',        (2,0), (2,-1), 'CENTER'),
    ] + row_colors))
    story.append(tbl)
    story.append(Spacer(1, 18))

    # Price summary
    story.append(Paragraph("Resumen de Inversión", s['heading']))
    story.append(HRFlowable(width="100%", thickness=1,
        color=colors.HexColor('#C9A96E'), spaceAfter=10))

    price_data = [
        [Paragraph("<b>Opción</b>", s['th']),
         Paragraph("<b>Locación</b>", s['th']),
         Paragraph("<b>Precio p/p</b>", s['th']),
         Paragraph("<b>200 personas</b>", s['th']),
         Paragraph("<b>250 personas</b>", s['th'])],
        [Paragraph("⭐ Recomendada", s['td']),
         Paragraph("<b>Jardín La Flor</b><br/>Privada las Fuentes s/n, San Gaspar, Jiutepec", s['td']),
         Paragraph("<b>$899.00 MXN</b>", s['td']),
         Paragraph("<b>$179,800.00</b>", s['td']),
         Paragraph("<b>$224,750.00</b>", s['td'])],
        [Paragraph("Opción Premium", s['td']),
         Paragraph("<b>Jardín San Rafael</b><br/>Jiutepec, Morelos", s['td']),
         Paragraph("<b>$1,499.00 MXN</b>", s['td']),
         Paragraph("<b>$299,800.00</b>", s['td']),
         Paragraph("<b>$374,750.00</b>", s['td'])],
    ]
    price_tbl = Table(price_data, colWidths=[80, 170, 75, 90, 90])
    price_tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0), colors.HexColor('#F65C7A')),
        ('BACKGROUND',    (0,1), (-1,1), colors.HexColor('#FFF5F6')),
        ('BACKGROUND',    (0,2), (-1,2), colors.white),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
        ('GRID',          (0,0), (-1,-1), 0.4, colors.HexColor('#E5E5E5')),
        ('ALIGN',         (2,0), (-1,-1), 'CENTER'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING',    (0,0), (-1,-1), 8),
    ]))
    story.append(price_tbl)
    story.append(Spacer(1, 20))

    conds = (
        "• 50% de anticipo para reservar la fecha del evento.<br/>"
        "• 50% restante a liquidar un día antes del evento.<br/>"
        "• Precios netos · IVA 16% aplica sólo en caso de factura oficial.<br/>"
        "• Los precios varían según número final de invitados confirmados.<br/>"
        "• Incluye degustación exclusiva para 4 personas al formalizar contrato."
    )
    story.append(Paragraph(conds, s['meta']))
    story.append(Spacer(1, 36))

    sig_data = [[
        Paragraph("_______________________________<br/><b>Richard Hernández</b><br/><font color='#6D6D6D'>Director Creativo &amp; Planner</font>", s['sig']),
        Paragraph("_______________________________<br/><b>Jessy Sandoval</b><br/><font color='#6D6D6D'>Founder &amp; Lead Planner</font>", s['sig']),
    ]]
    sig_tbl = Table(sig_data, colWidths=[270, 270])
    sig_tbl.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('TOPPADDING', (0,0), (-1,-1), 10)]))
    story.append(sig_tbl)
    story.append(Spacer(1, 18))
    story.append(Paragraph("«Hacemos de tu boda un recuerdo eterno. El arte de servir, hecho realidad.»", s['phrase']))

    doc.build(story, canvasmaker=BrandedCanvas)
    print(f"[OK] Mariangel PDF generado: {path}")


# ══════════════════════════════════════════════════════════════
#  PDF 2 — A QUIEN CORRESPONDA (Carnitas / Caballos)
# ══════════════════════════════════════════════════════════════
def build_caballos(path):
    doc = SimpleDocTemplate(path, pagesize=letter,
        leftMargin=36, rightMargin=36, topMargin=62, bottomMargin=74)
    s = get_styles()
    story = []

    build_header(story, s,
        client_name = "A Quien Corresponda",
        event_type  = "Evento Social · XV Años / Boda / Fiesta",
        location    = "Salón Jardín Los Caballos · Ignacio Zaragoza #21, Col. Ocotepec, Cuernavaca, Morelos",
        notes       = "Tel. Salón: (777) 261 5433 · Capacidad: 300 personas")

    story.append(Paragraph("Paquete Todo Incluido — Desglose Completo", s['heading']))
    story.append(HRFlowable(width="100%", thickness=1,
        color=colors.HexColor('#C9A96E'), spaceAfter=10))

    headers = [
        Paragraph("Concepto",          s['th']),
        Paragraph("Descripción",       s['th']),
        Paragraph("Incluye",           s['th']),
    ]
    rows_data = [
        ("Bienvenida — Aguas Frescas",
         "Aguas frescas naturales de temporada servidas a la llegada de los invitados."),
        ("Recepción — Margaritas sin Alcohol",
         "Margaritas de sabores sin alcohol preparadas al momento para los invitados durante la recepción."),
        ("Recepción — Piña Piñadas",
         "Piña piñadas frescas sin alcohol, refrescante bebida de bienvenida servida a los invitados en la recepción."),
        ("Sala Lounge",
         "Área lounge elegante habilitada para recibir a los invitados: espacio decorado y acondicionado para la recepción del evento."),
        ("Carnitas Surtidas",
         "Servicio completo de carnitas: surtida de cerdo, tortillas calientes, salsas, cebolla, cilantro, limones y guacamole."),
        ("Audio Profesional y Pista de Baile",
         "Sistema de audio de alta potencia. Pista de baile iluminada de 5×5 metros. Micrófonos inalámbricos para brindis y ceremonias."),
        ("Letras Iluminadas",
         'Letras gigantes iluminadas "XV", "LOVE" o iniciales personalizadas según el tipo de celebración.'),
        ("Pantallas",
         "Pantallas para presentaciones, videos de recuerdo o transmisión durante el evento."),
        ("DJ Profesional",
         "DJ con amplia experiencia en XV años, bodas y fiestas. Repertorio amplio adaptable al gusto de los festejados."),
        ("Meseros y Capitán",
         "Equipo de meseros uniformados y capitán de servicio supervisando todo el montaje y atención durante el evento."),
        ("Coordinación General",
         "Coordinador del minuto a minuto del evento. Programa, croquis y supervisión completa del evento."),
        ("Decoración del Salón",
         "Decoración del salón acorde al tipo de evento (XV, boda, graduación, etc.). Centros de mesa y ambientación completa."),
        ("Refrescos para Todos los Invitados",
         "Refrescos línea Coca-Cola disponibles para todos los invitados durante todo el evento. Hielo, vasos y desechables incluidos."),
    ]

    data = [headers]
    fill_colors = [colors.white, colors.HexColor('#FFF5F6')]
    for i, (concepto, desc) in enumerate(rows_data):
        data.append([
            Paragraph(f"<b>{concepto}</b>", s['td']),
            Paragraph(desc,                  s['td']),
            Paragraph("<b>✓ Incluido</b>",   s['td']),
        ])
    tbl = Table(data, colWidths=[155, 325, 60])
    row_colors = [('BACKGROUND', (0,i), (-1,i), fill_colors[(i-1)%2]) for i in range(1, len(data))]
    tbl.setStyle(TableStyle([
        ('BACKGROUND',   (0,0), (-1,0), colors.HexColor('#F65C7A')),
        ('VALIGN',       (0,0), (-1,-1), 'TOP'),
        ('GRID',         (0,0), (-1,-1), 0.4, colors.HexColor('#E5E5E5')),
        ('BOTTOMPADDING',(0,0), (-1,-1), 7),
        ('TOPPADDING',   (0,0), (-1,-1), 7),
        ('ALIGN',        (2,0), (2,-1), 'CENTER'),
    ] + row_colors))
    story.append(tbl)
    story.append(Spacer(1, 18))

    # Price box
    story.append(Paragraph("Inversión", s['heading']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#C9A96E'), spaceAfter=10))

    price_box_data = [
        [Paragraph("<b>Precio por Persona</b>", s['th']),
         Paragraph("<b>Salón</b>", s['th']),
         Paragraph("<b>Capacidad</b>", s['th']),
         Paragraph("<b>Teléfono</b>", s['th'])],
        [Paragraph("<b>$399.00 MXN</b>", ParagraphStyle('big', parent=s['td_bold'], fontSize=14, textColor=colors.HexColor('#F65C7A'))),
         Paragraph("<b>Salón Jardín Los Caballos</b><br/>Ignacio Zaragoza #21, Col. Ocotepec, Cuernavaca, Morelos", s['td']),
         Paragraph("Hasta 300 personas", s['td']),
         Paragraph("(777) 261 5433", s['td'])],
    ]
    price_tbl = Table(price_box_data, colWidths=[100, 240, 110, 90])
    price_tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0), colors.HexColor('#F65C7A')),
        ('BACKGROUND',    (0,1), (-1,1), colors.HexColor('#FFF5F6')),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
        ('GRID',          (0,0), (-1,-1), 0.4, colors.HexColor('#E5E5E5')),
        ('ALIGN',         (0,1), (0,1), 'CENTER'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING',    (0,0), (-1,-1), 10),
    ]))
    story.append(price_tbl)
    story.append(Spacer(1, 20))

    conds = (
        "• 50% de anticipo para reservar la fecha del evento.<br/>"
        "• 50% restante a liquidar un día antes del evento.<br/>"
        "• Precios netos · IVA 16% aplica sólo en caso de factura oficial.<br/>"
        "• El tipo de letras (XV, LOVE o iniciales) se define al formalizar el contrato."
    )
    story.append(Paragraph(conds, s['meta']))
    story.append(Spacer(1, 36))

    sig_data = [[
        Paragraph("_______________________________<br/><b>Richard Hernández</b><br/><font color='#6D6D6D'>Director Creativo &amp; Planner</font>", s['sig']),
        Paragraph("_______________________________<br/><b>Jessy Sandoval</b><br/><font color='#6D6D6D'>Founder &amp; Lead Planner</font>", s['sig']),
    ]]
    sig_tbl = Table(sig_data, colWidths=[270, 270])
    sig_tbl.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP'), ('TOPPADDING', (0,0), (-1,-1), 10)]))
    story.append(sig_tbl)
    story.append(Spacer(1, 18))
    story.append(Paragraph("«Cada evento es único. El arte de servir, hecho realidad.»", s['phrase']))

    doc.build(story, canvasmaker=BrandedCanvas)
    print(f"[OK] Caballos PDF generado: {path}")


# ══════════════════════════════════════════════════════════════
if __name__ == '__main__':
    os.makedirs(artifact_dir, exist_ok=True)
    build_mariangel(PDF_MARIANGEL_WS)
    build_mariangel(PDF_MARIANGEL_ART)
    build_caballos(PDF_CABALLOS_WS)
    build_caballos(PDF_CABALLOS_ART)
    print("\n[OK] Ambos PDFs generados correctamente.")
