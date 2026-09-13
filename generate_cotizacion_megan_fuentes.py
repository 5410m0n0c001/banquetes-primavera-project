import os
import datetime
import fitz  # PyMuPDF
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Paths
workspace_dir = r"C:\Users\Lenovo\Documents\primavera brain"
pdf_filename = "cotizacion_megan_fuentes_petit.pdf"
pdf_path_ws = os.path.join(workspace_dir, pdf_filename)

artifact_dir = r"C:\Users\Lenovo\.gemini\antigravity\brain\2662e14f-6269-4a71-8fa5-e4f99bece5d8"
pdf_path_art = os.path.join(artifact_dir, pdf_filename)
png_preview_path = os.path.join(artifact_dir, "preview_megan_fuentes.png")

logo_path = os.path.join(workspace_dir, "assets", "images", "logo_principal_p.png")

def create_pdf(target_path):
    doc = SimpleDocTemplate(
        target_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=30,
        bottomMargin=30
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Brand Colors
    PINK = colors.HexColor('#F65C7A')
    GOLD = colors.HexColor('#C9A96E')
    DARK = colors.HexColor('#1F1F1F')
    GRAY = colors.HexColor('#6D6D6D')
    BG_CREAM = colors.HexColor('#FAF7F5')
    BORDER_LIGHT = colors.HexColor('#E2DDD5')
    
    # Custom Paragraph Styles
    title_style = ParagraphStyle(
        'HeaderTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=19,
        leading=21,
        textColor=DARK,
        alignment=1 # Centered
    )
    
    subtitle_style = ParagraphStyle(
        'HeaderSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=GRAY,
        alignment=1,
        spaceBefore=3
    )
    
    section_title_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=13,
        textColor=DARK,
        spaceBefore=4,
        spaceAfter=3
    )
    
    section_desc_style = ParagraphStyle(
        'SectionDesc',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=DARK,
        spaceAfter=4
    )
    
    meta_label = ParagraphStyle('MetaLabel', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=DARK)
    meta_val = ParagraphStyle('MetaVal', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=12, textColor=DARK)
    meta_val_pink = ParagraphStyle('MetaValPink', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.5, leading=12, textColor=PINK)
    
    th_style = ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=10.5, textColor=colors.white)
    
    td_style = ParagraphStyle('TD', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11, textColor=DARK)
    td_bold = ParagraphStyle('TDBold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=DARK)
    td_center = ParagraphStyle('TDCenter', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11, textColor=DARK, alignment=1)
    td_right = ParagraphStyle('TDRight', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11, textColor=DARK, alignment=2)
    td_right_bold = ParagraphStyle('TDRightBold', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=DARK, alignment=2)
    
    notes_header_style = ParagraphStyle('NotesHeader', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.5, leading=11.5, textColor=DARK, spaceBefore=3, spaceAfter=2)
    notes_item_style = ParagraphStyle('NotesItem', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=10, textColor=DARK)
    
    slogan_style = ParagraphStyle('Slogan', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=8.5, leading=10.5, textColor=GOLD, alignment=1, spaceBefore=3, spaceAfter=2)
    footer_style = ParagraphStyle('FooterText', parent=styles['Normal'], fontName='Helvetica', fontSize=7.5, leading=9.5, textColor=GRAY, alignment=1)

    story = []

    # 1. Header (Official Floral "P" Logo + Titles with ® trademark)
    title_flowables = [
        Paragraph("PRIMAVERA EVENTS GROUP®", title_style),
        Paragraph("COTIZACIÓN DE MOBILIARIO Y CRISTALERÍA · EVENTO PETIT", subtitle_style)
    ]
    
    if os.path.exists(logo_path):
        logo_img = Image(logo_path, width=52, height=52)
        header_table = Table([[logo_img, title_flowables]], colWidths=[60, 480])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('ALIGN', (0,0), (0,0), 'CENTER'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(header_table)
    else:
        story.extend(title_flowables)

    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=PINK, spaceBefore=0, spaceAfter=5))

    # 2. Client & Event Info Box
    today_str = datetime.date.today().strftime("%d / %m / %Y")
    valid_str = (datetime.date.today() + datetime.timedelta(days=15)).strftime("%d / %m / %Y")
    
    meta_data = [
        [
            Paragraph("<b>Dirigido a:</b> Megan Fuentes", meta_val),
            Paragraph(f"<b>Fecha de Emisión:</b> {today_str}", meta_val)
        ],
        [
            Paragraph("<b>Tipo de Evento:</b> Graduación Petit (en Airbnb)", meta_val),
            Paragraph(f"<b>Validez de Cotización:</b> {valid_str} (15 días)", meta_val)
        ],
        [
            Paragraph("<b>Capacidad Solicitada:</b> 30 personas", meta_val),
            Paragraph("<b>Coordinadores:</b> Richard Hernández & Jessy Sandoval", meta_val)
        ],
        [
            Paragraph("<b>Costo estimado p/p:</b> <font color='#F65C7A'><b>$121.67 MXN / persona</b></font>", meta_val_pink),
            Paragraph("<b>Estatus:</b> Presupuesto de Factibilidad", meta_val)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[270, 270])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), BG_CREAM),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_LIGHT),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_LIGHT),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 6))

    # 3. Section Title
    story.append(Paragraph("DESGLOSE DETALLADO DE MOBILIARIO Y SERVICIOS DE MESA", section_title_style))
    story.append(Paragraph("Cotización especial adaptada a espacio petit (Airbnb) para 30 invitados. Todos los colores de loza, cristalería y servilletas quedan a elección del cliente.", section_desc_style))

    # 4. Itemized Pricing Table
    table_data = [
        [Paragraph("CONCEPTO / ITEM", th_style), Paragraph("DESCRIPCIÓN Y ESPECIFICACIÓN", th_style), Paragraph("CANT.", th_style), Paragraph("P. UNIT.", th_style), Paragraph("SUBTOTAL", th_style)],
        
        # Mobiliario
        [Paragraph("Sillas Crossback", td_bold), Paragraph("Sillas artesanales modelo Crossback de madera fina.", td_style), Paragraph("30 pzas", td_center), Paragraph("$45.00", td_right), Paragraph("$1,350.00", td_right_bold)],
        [Paragraph("Mesa de Madera (6 px)", td_bold), Paragraph("Mesa rústica de madera rectangular para 6 personas.", td_style), Paragraph("1 pza", td_center), Paragraph("$200.00", td_right), Paragraph("$200.00", td_right_bold)],
        [Paragraph("Mesa de Madera (10 px)", td_bold), Paragraph("Mesas rústicas de madera rectangulares para 10 personas.", td_style), Paragraph("3 pzas", td_center), Paragraph("$300.00", td_right), Paragraph("$900.00", td_right_bold)],
        
        # Servicios de loza y cristaleria
        [Paragraph("Plato Base (Bajo Plato)", td_bold), Paragraph("Plato base decorativo (color a elegir por la clienta).", td_style), Paragraph("30 pzas", td_center), Paragraph("$10.00", td_right), Paragraph("$300.00", td_right_bold)],
        [Paragraph("Cubiertos Premium", td_bold), Paragraph("Juego de cubiertos (tenedor y cuchillo) de loza fina.", td_style), Paragraph("60 pzas", td_center), Paragraph("$4.00", td_right), Paragraph("$240.00", td_right_bold)],
        [Paragraph("Vaso Cubero", td_bold), Paragraph("Vaso de cristal para servicio de bebidas y mezcladores.", td_style), Paragraph("30 pzas", td_center), Paragraph("$2.00", td_right), Paragraph("$60.00", td_right_bold)],
        [Paragraph("Copa de Cristal", td_bold), Paragraph("Copa de cristal fina para agua o vino.", td_style), Paragraph("30 pzas", td_center), Paragraph("$8.00", td_right), Paragraph("$240.00", td_right_bold)],
        [Paragraph("Plato Trinchere / Loza", td_bold), Paragraph("Plato principal de porcelana/loza blanca o decorada.", td_style), Paragraph("30 pzas", td_center), Paragraph("$5.00", td_right), Paragraph("$150.00", td_right_bold)],
        [Paragraph("Servilleta de Tela", td_bold), Paragraph("Servilleta de tela fina institucional (color a elegir).", td_style), Paragraph("30 pzas", td_center), Paragraph("$7.00", td_right), Paragraph("$210.00", td_right_bold)],
    ]

    items_table = Table(table_data, colWidths=[125, 225, 50, 65, 75])
    items_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,0), 4),
        ('BOTTOMPADDING', (0,0), (-1,0), 4),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_LIGHT),
        ('TOPPADDING', (0,1), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,1), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#FFF9FA')]),
    ]))
    story.append(items_table)
    story.append(Spacer(1, 6))

    # 5. Totals & Investment Summary Table
    totals_left = Paragraph(
        "<b>Condiciones Presupuestales:</b><br/>"
        "• 50% de anticipo para formalizar y bloquear el apartado de equipo.<br/>"
        "• 50% restante a liquidar un día antes del evento.<br/>"
        "• Flete y montaje/desmontaje en Airbnb se cotizan según ubicación exacto en Morelos.",
        ParagraphStyle('TotLeft', parent=styles['Normal'], fontName='Helvetica', fontSize=7.5, leading=10, textColor=GRAY)
    )
    
    subtotal_val = 3650.00
    totals_right_data = [
        [Paragraph("<b>Subtotal Neto:</b>", td_style), Paragraph(f"<b>${subtotal_val:,.2f} MXN</b>", td_right_bold)],
        [Paragraph("<font color='#6D6D6D'>I.V.A. (16% en caso de factura):</font>", td_style), Paragraph(f"<font color='#6D6D6D'>${subtotal_val*0.16:,.2f} MXN</font>", td_right)],
        [Paragraph("<b>TOTAL ESTIMADO:</b>", td_bold), Paragraph(f"<font color='#F65C7A'><b>${subtotal_val:,.2f} MXN</b></font>", ParagraphStyle('BigPink', parent=td_right_bold, fontSize=11, textColor=PINK))]
    ]
    totals_right_table = Table(totals_right_data, colWidths=[130, 90])
    totals_right_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('LINEBELOW', (0,0), (-1,1), 0.5, BORDER_LIGHT),
    ]))
    
    totals_outer = Table([[totals_left, totals_right_table]], colWidths=[310, 230])
    totals_outer.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(totals_outer)
    story.append(Spacer(1, 5))

    # 6. Conditions & Notes
    story.append(Paragraph("NOTAS IMPORTANTES PARA EL EVENTO PETIT", notes_header_style))
    notes = [
        "• Cotización especial diseñada para <b>Megan Fuentes</b> para evento de graduación en Airbnb (30 personas).",
        "• Todos los insumos de cristalería, vajilla y mantelería son de calidad premium de graduación.",
        "• Los colores de bajo plato, servilletas y combinaciones de loza se confirmarán con el coordinador previa al evento.",
        "• Precios netos vigentes por 15 días a partir de su emisión."
    ]
    for note in notes:
        story.append(Paragraph(note, notes_item_style))
        story.append(Spacer(1, 0.5))

    story.append(Spacer(1, 3))

    # 7. Slogan & Legal Footer
    story.append(Paragraph("«Hacemos de tu celebración un recuerdo eterno. El arte de servir, hecho realidad.»", slogan_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("<b>PRIMAVERA EVENTS GROUP®</b> · Av. Defensa Nacional #8, Col. Chamilpa, 62210 Cuernavaca, Mor.<br/>Tel / WhatsApp: +52 777 458 7923 · primaveraeventsgroup.com<br/><b>Primavera Events Group®</b> y <b>Banquetes Primavera®</b> son marcas registradas. © Todos los derechos reservados.", footer_style))

    doc.build(story)
    print(f"Generated PDF at: {target_path}")

if __name__ == '__main__':
    # Build PDF in workspace
    create_pdf(pdf_path_ws)
    
    # Build PDF in artifact directory
    os.makedirs(artifact_dir, exist_ok=True)
    create_pdf(pdf_path_art)
    
    # Render PDF page 1 to PNG preview and check page count
    doc = fitz.open(pdf_path_ws)
    print(f"Total PDF pages: {len(doc)}")
    page = doc.load_page(0)
    pix = page.get_pixmap(dpi=150)
    pix.save(png_preview_path)
    print(f"Rendered PNG preview at: {png_preview_path}")
