import os
import fitz  # PyMuPDF
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Paths
workspace_dir = r"C:\Users\Lenovo\Documents\primavera brain"
pdf_filename = "Cotizacion_Graduacion_Universidad_G_Primavera.pdf"
pdf_path_ws = os.path.join(workspace_dir, pdf_filename)

artifact_dir = r"C:\Users\Lenovo\.gemini\antigravity\brain\2662e14f-6269-4a71-8fa5-e4f99bece5d8"
pdf_path_art = os.path.join(artifact_dir, pdf_filename)
png_preview_path = os.path.join(artifact_dir, "preview_page_1.png")

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
        fontSize=20,
        leading=22,
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
    meta_val_pink = ParagraphStyle('MetaValPink', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10, leading=12, textColor=PINK)
    
    th_style = ParagraphStyle('TH', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9, leading=11, textColor=colors.white)
    
    concept_style = ParagraphStyle('ConceptCell', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=DARK)
    included_style = ParagraphStyle('IncludedCell', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=8.5, leading=11, textColor=DARK)
    desc_style = ParagraphStyle('DescCell', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11, textColor=DARK)
    
    notes_header_style = ParagraphStyle('NotesHeader', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=9.5, leading=11.5, textColor=DARK, spaceBefore=3, spaceAfter=2)
    notes_item_style = ParagraphStyle('NotesItem', parent=styles['Normal'], fontName='Helvetica', fontSize=8, leading=10, textColor=DARK)
    
    slogan_style = ParagraphStyle('Slogan', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=8.5, leading=10.5, textColor=GOLD, alignment=1, spaceBefore=3, spaceAfter=2)
    footer_style = ParagraphStyle('FooterText', parent=styles['Normal'], fontName='Helvetica', fontSize=7.5, leading=9.5, textColor=GRAY, alignment=1)

    story = []

    # 1. Header (Official Floral "P" Logo + Titles with ® trademark)
    title_flowables = [
        Paragraph("PRIMAVERA EVENTS GROUP®", title_style),
        Paragraph("PROPUESTA DE PAQUETE · EVENTO UNIVERSITARIO", subtitle_style)
    ]
    
    if os.path.exists(logo_path):
        logo_img = Image(logo_path, width=54, height=54)
        header_table = Table([[logo_img, title_flowables]], colWidths=[64, 476])
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

    # 2. Client & Event Info Box (Table)
    meta_data = [
        [
            Paragraph("<b>A quien corresponda</b>", meta_label),
            Paragraph("<b>Universidad G · Comité de Alumnos</b>", meta_label)
        ],
        [
            Paragraph("<b>Invitados</b><br/>100 personas", meta_val),
            Paragraph("<b>Duración</b><br/>Horas de servicio: a definir", meta_val)
        ],
        [
            Paragraph("<b>Precio por persona</b><br/><font color='#F65C7A'><b>$799.00 MXN</b></font>", meta_val_pink),
            Paragraph("<b>Fecha</b><br/>A definir", meta_val)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[270, 270])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), BG_CREAM),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_LIGHT),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_LIGHT),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 6))

    # 3. Section Title
    story.append(Paragraph("PAQUETE DE BANQUETE, MONTAJE Y ENTRETENIMIENTO", section_title_style))
    story.append(Paragraph("Propuesta diseñada para 100 invitados, con una tarifa única por persona. Todo lo descrito a continuación se considera incluido dentro del costo de <b>$799.00 MXN por persona</b>, sujeto a las condiciones de contratación.", section_desc_style))

    # 4. Main Concept Breakdown Table
    table_data = [
        # Header (Row 0)
        [Paragraph("CONCEPTO", th_style), Paragraph("INCLUIDO", th_style), Paragraph("DESCRIPCIÓN", th_style)],
        
        # 1 · RECEPCIÓN Y COCTELERÍA (Rows 1, 2, 3)
        [Paragraph("1 · RECEPCIÓN Y COCTELERÍA", concept_style), Paragraph("Cóctel de bienvenida", included_style), Paragraph("Servicio de cóctel de bienvenida para los invitados.", desc_style)],
        ["", Paragraph("Mezcladores", included_style), Paragraph("Mezcladores línea Coca-Cola, Manzanita, Agua Mineral, etc.", desc_style)],
        ["", Paragraph("Hielo", included_style), Paragraph("Hielo incluido para el servicio de bebidas.", desc_style)],
        
        # 2 · BANQUETE Y GASTRONOMÍA (Rows 4, 5, 6)
        [Paragraph("2 · BANQUETE Y GASTRONOMÍA", concept_style), Paragraph("Primer tiempo", included_style), Paragraph("Primer tiempo a elegir.", desc_style)],
        ["", Paragraph("Segundo tiempo", included_style), Paragraph("Segundo tiempo a elegir.", desc_style)],
        ["", Paragraph("Tercer tiempo", included_style), Paragraph("Postre a elegir.", desc_style)],
        
        # 3 · MONTAJE (Rows 7, 8)
        [Paragraph("3 · MONTAJE", concept_style), Paragraph("Letras gigantes", included_style), Paragraph("Letras gigantes como elemento decorativo y fotográfico.", desc_style)],
        ["", Paragraph("Montaje elegante", included_style), Paragraph("Montaje general con presentación elegante para el evento.", desc_style)],
        
        # 4 · STAFF Y SERVICIO (Rows 9, 10, 11, 12)
        [Paragraph("4 · STAFF Y SERVICIO", concept_style), Paragraph("Meseros", included_style), Paragraph("Personal de servicio para atención de los invitados.", desc_style)],
        ["", Paragraph("Coordinador", included_style), Paragraph("Coordinación y supervisión operativa del evento.", desc_style)],
        ["", Paragraph("Personal de barra", included_style), Paragraph("Personal asignado para el servicio de barra.", desc_style)],
        ["", Paragraph("Cocina", included_style), Paragraph("Personal de cocina para la operación del servicio.", desc_style)],
        
        # 5 · ENTRETENIMIENTO (Rows 13, 14, 15)
        [Paragraph("5 · ENTRETENIMIENTO", concept_style), Paragraph("Show de Cabezones", included_style), Paragraph("Show de Cabezones (ejemplo: La Máscara).", desc_style)],
        ["", Paragraph("Tornafiesta · Chilaquiles", included_style), Paragraph("Servicio de chilaquiles para el cierre del evento.", desc_style)],
        ["", Paragraph("Cabina 360° o Cabina Espejo", included_style), Paragraph("A elegir una opción: cabina 360° o cabina espejo.", desc_style)],
    ]

    main_table = Table(table_data, colWidths=[135, 145, 260])
    main_table.setStyle(TableStyle([
        # Header style
        ('BACKGROUND', (0,0), (-1,0), DARK),
        ('VALIGN', (0,0), (-1,0), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,0), 4),
        ('BOTTOMPADDING', (0,0), (-1,0), 4),
        
        # Grid & alignment
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_LIGHT),
        ('VALIGN', (0,1), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,1), (-1,-1), 3),
        ('BOTTOMPADDING', (0,1), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        
        # Spans for Concept column
        ('SPAN', (0, 1), (0, 3)),   # 1 · RECEPCIÓN Y COCTELERÍA
        ('SPAN', (0, 4), (0, 6)),   # 2 · BANQUETE Y GASTRONOMÍA
        ('SPAN', (0, 7), (0, 8)),   # 3 · MONTAJE
        ('SPAN', (0, 9), (0, 12)),  # 4 · STAFF Y SERVICIO
        ('SPAN', (0, 13), (0, 15)), # 5 · ENTRETENIMIENTO
        
        # Alternating background colors per concept group
        ('BACKGROUND', (0, 1), (-1, 3), colors.HexColor('#FFFFFF')),
        ('BACKGROUND', (0, 4), (-1, 6), colors.HexColor('#FFF9FA')),
        ('BACKGROUND', (0, 7), (-1, 8), colors.HexColor('#FFFFFF')),
        ('BACKGROUND', (0, 9), (-1, 12), colors.HexColor('#FFF9FA')),
        ('BACKGROUND', (0, 13), (-1, 15), colors.HexColor('#FFFFFF')),
    ]))
    
    story.append(main_table)
    story.append(Spacer(1, 6))

    # 5. Investment Summary Box (Totals)
    summary_left = Paragraph("<b>100 personas × $799.00 MXN</b><br/><font color='#6D6D6D' size='7.5'>INVERSIÓN TOTAL ESTIMADA</font>", ParagraphStyle('SumLeft', parent=styles['Normal'], fontName='Helvetica', fontSize=9.5, leading=13))
    summary_right = Paragraph("<font color='#F65C7A' size='14'><b>$79,900.00 MXN</b></font><br/><b>$79,900.00 MXN</b>", ParagraphStyle('SumRight', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=14, alignment=2))
    
    summary_table = Table([[summary_left, summary_right]], colWidths=[270, 270])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), BG_CREAM),
        ('BOX', (0,0), (-1,-1), 0.75, GOLD),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 5))

    # 6. Conditions and Notes
    story.append(Paragraph("CONDICIONES Y NOTAS", notes_header_style))
    notes = [
        "• La propuesta considera <b>100 personas</b>.",
        "• Tarifa: <b>$799.00 MXN por persona</b>.",
        "• Inversión calculada para 100 personas: <b>$79,900.00 MXN</b>.",
        "• Horas de servicio: <b>a definir</b> con el comité de alumnos.",
        "• Cabina: se deberá elegir entre <b>Cabina 360°</b> o <b>Cabina Espejo</b>.",
        "• Fecha y lugar: <b>a definir</b>.",
        "• La propuesta se basa en los conceptos solicitados y podrá formalizarse al confirmar fecha, horario y condiciones del evento."
    ]
    for note in notes:
        story.append(Paragraph(note, notes_item_style))
        story.append(Spacer(1, 0.5))

    story.append(Spacer(1, 3))

    # 7. Slogan & Footer with Marca Registrada ® & Rights Reserved Notice
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
