import os
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

# ── Configuraciones de Ruta ──────────────────────────────────
ws_dir = r"C:\Users\Lenovo\Documents\primavera brain"
project_dir = os.path.join(ws_dir, "cotizacion_yolomecatl_xv_50px")
logo_path = os.path.join(ws_dir, "assets", "images", "primaveralogo.jpg")

# ── Canvas Corporativo Primavera ─────────────────────────────
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
        self.setFillColor(colors.HexColor('#F65C7A'))
        self.rect(36, 756, 540, 14, fill=True, stroke=False)
        self.setFillColor(colors.white)
        self.setFont("Helvetica-Bold", 7.5)
        self.drawString(46, 760, "PRIMAVERA EVENTS GROUP  |  EL ARTE DE SERVIR")

        self.setStrokeColor(colors.HexColor('#C9A96E'))
        self.setLineWidth(1)
        self.line(36, 54, 576, 54)

        self.setFont("Helvetica", 7.5)
        self.setFillColor(colors.HexColor('#6D6D6D'))
        self.drawString(36, 40, "contacto@primaveraeventsgroup.com  |  +52 777 458 7923  |  Cuernavaca, Morelos")
        self.drawRightString(576, 40, f"Página {self._pageNumber} de {total}")
        self.restoreState()

# ── Estilos de Documento ──────────────────────────────────────
def get_styles():
    base = getSampleStyleSheet()
    PINK  = colors.HexColor('#F65C7A')
    GOLD  = colors.HexColor('#C9A96E')
    DARK  = colors.HexColor('#1F1F1F')
    GRAY  = colors.HexColor('#6D6D6D')

    title = ParagraphStyle('title', parent=base['Normal'],
        fontName='Helvetica-Bold', fontSize=18, leading=22,
        textColor=PINK, spaceAfter=2)
    subtitle = ParagraphStyle('subtitle', parent=base['Normal'],
        fontName='Helvetica-Bold', fontSize=9.5, leading=11,
        textColor=GOLD, spaceAfter=4)
    heading = ParagraphStyle('heading', parent=base['Normal'],
        fontName='Helvetica-Bold', fontSize=12, leading=15,
        textColor=DARK, spaceBefore=10, spaceAfter=6)
    body = ParagraphStyle('body', parent=base['Normal'],
        fontName='Helvetica', fontSize=9, leading=12.5, textColor=DARK)
    body_bold = ParagraphStyle('body_bold', parent=body, fontName='Helvetica-Bold')
    meta = ParagraphStyle('meta', parent=base['Normal'],
        fontName='Helvetica', fontSize=8, leading=11, textColor=GRAY)
    td = ParagraphStyle('td', parent=base['Normal'],
        fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=DARK)
    td_bold = ParagraphStyle('td_bold', parent=td, fontName='Helvetica-Bold')
    phrase = ParagraphStyle('phrase', parent=base['Normal'],
        fontName='Helvetica-Oblique', fontSize=9.5, leading=13,
        textColor=PINK, alignment=1, spaceBefore=8)
    sig = ParagraphStyle('sig', parent=body, alignment=1)
    bonus_title = ParagraphStyle('bonus_title', parent=body_bold, textColor=GOLD, fontSize=10)

    return dict(title=title, subtitle=subtitle, heading=heading,
                body=body, body_bold=body_bold, meta=meta,
                td=td, td_bold=td_bold, phrase=phrase, sig=sig,
                bonus_title=bonus_title,
                PINK=PINK, GOLD=GOLD, DARK=DARK, GRAY=GRAY)

# ── Encabezado ─────────────────────────────────────────────────
def build_header(story, s):
    titles_col = [
        Paragraph("COTIZACIÓN DE SERVICIOS", s['title']),
        Paragraph("PRIMAVERA EVENTS GROUP  —  EL ARTE DE SERVIR", s['subtitle']),
    ]
    if os.path.exists(logo_path):
        logo_img = Image(logo_path, width=65, height=65)
        ht = Table([[logo_img, titles_col]], colWidths=[75, 465])
        ht.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING',  (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING',   (0,0), (-1,-1), 0),
            ('BOTTOMPADDING',(0,0), (-1,-1), 8),
        ]))
        story.append(ht)
    else:
        story += titles_col
        story.append(Spacer(1, 10))

    today = datetime.date.today()
    valid = today + datetime.timedelta(days=15)

    meta_l = [
        Paragraph("<b>Evento:</b> XV Años", s['body']),
        Paragraph("<b>Ubicación:</b> Jardín, Temixco, Morelos", s['body']),
        Paragraph("<b>Presentación:</b> Paquete Todo Incluido", s['body_bold']),
    ]

    meta_r = [
        Paragraph(f"<b>Fecha de Emisión:</b> {today.strftime('%d / %m / %Y')}", s['body']),
        Paragraph(f"<b>Validez de Cotización:</b> {valid.strftime('%d / %m / %Y')} (15 días)", s['body']),
        Paragraph("<b>Capacidad:</b> 50 Px", s['body_bold']),
    ]

    rows = [[meta_l[i] if i < len(meta_l) else Paragraph("", s['body']),
             meta_r[i] if i < len(meta_r) else Paragraph("", s['body'])]
            for i in range(max(len(meta_l), len(meta_r)))]

    mt = Table(rows, colWidths=[330, 210])
    mt.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING',    (0,0), (-1,-1), 3),
        ('LEFTPADDING',   (0,0), (-1,-1), 0),
        ('RIGHTPADDING',  (0,0), (-1,-1), 0),
    ]))
    story.append(mt)
    story.append(Spacer(1, 8))

# ── Descripción del Paquete ────────────────────────────────────
def build_package_desc(story, s):
    desc_style = ParagraphStyle('desc', parent=s['body'], fontSize=9, leading=13.5, spaceAfter=2)

    package_elements = [
        ("Recepción y Banquete", "Cóctel de recepción de bienvenida y menú de 2 tiempos servido por nuestro equipo de meseros y capitán de meseros durante las 8 horas de servicio."),
        ("Barra y Servicio", "Mezcladores profesionales para preparación y despacho de bebidas durante todo el evento."),
        ("Montaje y Ambientación", "Centros de mesa a tono con la paleta elegida, vajilla completa por invitado, y mesa de honor especial para la festejada de XV años."),
        ("Pista y Música", "Pista de baile iluminada de 5×5 metros y DJ profesional durante todo el evento."),
        ("Duración", "8 horas continuas de servicio."),
    ]

    cells = []
    for title, text in package_elements:
        inner = Table(
            [[Paragraph(f"<b>{title}</b>", s['body_bold'])],
             [Paragraph(text, desc_style)]],
            colWidths=[254]
        )
        inner.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFF5F6')),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('LEFTPADDING', (0,0), (-1,-1), 9),
            ('RIGHTPADDING', (0,0), (-1,-1), 9),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#EFE7E1')),
        ]))
        cells.append(inner)

    while len(cells) % 2 != 0:
        cells.append(Paragraph("", s['body']))

    grid_rows = [[cells[i], cells[i+1]] for i in range(0, len(cells), 2)]
    grid = Table(grid_rows, colWidths=[268, 268])
    grid.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING',  (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING',   (0,0), (-1,-1), 0),
        ('BOTTOMPADDING',(0,0), (-1,-1), 5),
    ]))
    story.append(grid)
    story.append(Spacer(1, 4))

# ── Bono por Apartado Esta Semana ──────────────────────────────
def build_bonus_box(story, s):
    p_title = Paragraph("🎁 Bono exclusivo por apartar tu fecha esta semana", s['bonus_title'])
    p_text = Paragraph(
        "Mobiliario de mesa redonda con sombrilla, y silla plegable vestida — a tono de tu elección, "
        "de cortesía al formalizar tu reservación dentro de los próximos días.",
        ParagraphStyle('bonus_text', parent=s['body'], fontSize=9, leading=13)
    )
    tbl = Table([[p_title], [p_text]], colWidths=[540])
    tbl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FBF6EC')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('BOX', (0,0), (-1,-1), 0.75, s['GOLD']),
    ]))
    story.append(tbl)
    story.append(Spacer(1, 6))

# ── Totales y Firmas ────────────────────────────────────────────
def build_totals_and_sig(story, s, total_val):
    conds = (
        "<b>Condiciones y Notas Comerciales:</b><br/>"
        "• 50% de anticipo para formalizar la reservación de la fecha.<br/>"
        "• 50% restante a liquidar un día antes de la realización del evento.<br/>"
        "• Precios netos · IVA del 16% aplica sólo en caso de requerir factura oficial.<br/>"
        "• Cotización garantizada y válida por un periodo de 15 días a partir de su emisión.<br/>"
        "• Bono de mobiliario aplica únicamente si el apartado se formaliza esta semana."
    )

    totals_right = Table([
        [Paragraph("<b>Inversión Total:</b>", s['td_bold']), Paragraph(f"<b>${total_val:,.2f} MXN</b>", s['td_bold'])],
    ], colWidths=[110, 110])

    totals_right.setStyle(TableStyle([
        ('ALIGN', (1,0), (1,-1), 'RIGHT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING',    (0,0), (-1,-1), 4),
    ]))

    tot_outer = Table([[Paragraph(conds, s['meta']), totals_right]], colWidths=[330, 210])
    tot_outer.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING',  (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING',    (0,0), (-1,-1), 5),
    ]))
    story.append(tot_outer)
    story.append(Spacer(1, 16))

    sig_data = [[
        Paragraph("_______________________________<br/><b>Richard Hernández</b><br/><font color='#6D6D6D'>Director Creativo &amp; Planner</font>", s['sig']),
        Paragraph("_______________________________<br/><b>Jessy Sandoval</b><br/><font color='#6D6D6D'>Founder &amp; Lead Planner</font>", s['sig']),
    ]]
    sig_tbl = Table(sig_data, colWidths=[270, 270])
    sig_tbl.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 8)
    ]))
    story.append(sig_tbl)
    story.append(Spacer(1, 12))

    story.append(Paragraph("«Hacemos de tu celebración un recuerdo eterno. El arte de servir, hecho realidad.»", s['phrase']))

# ── Generador ───────────────────────────────────────────────────
def build_pdf_document(filename, total_val):
    path = os.path.join(project_dir, filename)
    doc = SimpleDocTemplate(path, pagesize=letter,
        leftMargin=36, rightMargin=36, topMargin=55, bottomMargin=68)
    s = get_styles()
    story = []

    build_header(story, s)
    story.append(Spacer(1, 4))
    story.append(Paragraph("Especificaciones del Paquete XV Años — 50 Personas", s['heading']))
    story.append(HRFlowable(width="100%", thickness=1, color=s['GOLD'], spaceAfter=8))
    build_package_desc(story, s)
    build_bonus_box(story, s)
    build_totals_and_sig(story, s, total_val)

    doc.build(story, canvasmaker=BrandedCanvas)
    print(f"Archivo generado: {path}")

if __name__ == '__main__':
    if not os.path.exists(project_dir):
        os.makedirs(project_dir)
    build_pdf_document("cotizacion_xv_yolomecatl_50px.pdf", 37900.0)
