import os
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

# Define path
pdf_dir = r"C:\Users\Lenovo\Documents\primavera brain"
pdf_path = os.path.join(pdf_dir, "cotizacion_fiorella.pdf")
artifact_dir = r"C:\Users\Lenovo\.gemini\antigravity\brain\ea456458-da0e-423d-83aa-e3df5e91c057"
artifact_pdf_path = os.path.join(artifact_dir, "cotizacion_fiorella.pdf")
logo_source_path = r"C:\Users\Lenovo\Downloads\Sin título - 12 de marzo de 2026, 02.23.12 (2).png"

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor('#F65C7A')) # Rosa Principal
        
        # Top banner decoration
        self.rect(36, 756, 540, 15, fill=True, stroke=False)
        self.setFillColor(colors.white)
        self.drawString(46, 760, "PRIMAVERA EVENTS GROUP  |  EXPERIENCIAS EXCLUSIVAS")
        
        # Bottom footer line
        self.setStrokeColor(colors.HexColor('#C9A96E')) # Oro Noble
        self.setLineWidth(1)
        self.line(36, 54, 576, 54)
        
        # Footer text
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor('#6D6D6D'))
        self.drawString(36, 40, "contacto@primaveraeventsgroup.com  |  Tel. +52 777 458 7923  |  Cuernavaca, Morelos")
        self.drawRightString(576, 40, f"Página {self._pageNumber} de {page_count}")
        
        self.restoreState()

def build_pdf(target_path):
    # Page setup
    doc = SimpleDocTemplate(
        target_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=60,
        bottomMargin=72
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    # Primary colors: Pink #F65C7A, Gold #C9A96E, Gray #6D6D6D, Dark #1F1F1F
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#F65C7A'),
        spaceAfter=3
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=13,
        textColor=colors.HexColor('#C9A96E'),
        spaceAfter=5
    )
    
    heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=15,
        textColor=colors.HexColor('#1F1F1F'),
        spaceBefore=12,
        spaceAfter=8
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#1F1F1F')
    )
    
    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )
    
    meta_style = ParagraphStyle(
        'MetaText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#6D6D6D')
    )
    
    table_text = ParagraphStyle(
        'TableText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=11,
        textColor=colors.HexColor('#1F1F1F')
    )
    
    table_header_text = ParagraphStyle(
        'TableHeaderText',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=11,
        textColor=colors.white
    )

    story = []
    
    # Title & Header with Logo
    header_content = [
        Paragraph("COTIZACIÓN DE SERVICIOS", title_style),
        Paragraph("PRIMAVERA EVENTS GROUP  —  EL ARTE DE SERVIR", subtitle_style)
    ]
    
    if os.path.exists(logo_source_path):
        # Insert logo image (75x75 points)
        logo_img = Image(logo_source_path, width=70, height=70)
        header_table_data = [[logo_img, header_content]]
        header_table = Table(header_table_data, colWidths=[80, 460])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ]))
        story.append(header_table)
    else:
        # Fallback if logo not found
        story.append(header_content[0])
        story.append(header_content[1])
        story.append(Spacer(1, 10))
    
    # Meta Info (2 columns: Client on left, Cotización Info on right)
    meta_left = [
        Paragraph("<b>Dirigido a:</b> Fiorella", body_style),
        Paragraph("<b>Ubicación del Evento:</b> Xochitepec, Morelos", body_style),
        Paragraph("<b>Tipo de Evento:</b> Boda / Social", body_style),
    ]
    
    current_date = datetime.date.today().strftime("%d / %m / %Y")
    valid_date = (datetime.date.today() + datetime.timedelta(days=15)).strftime("%d / %m / %Y")
    
    meta_right = [
        Paragraph(f"<b>Fecha de Emisión:</b> {current_date}", body_style),
        Paragraph(f"<b>Validez de Cotización:</b> {valid_date} (15 días)", body_style),
        Paragraph("<b>Coordinadores:</b> Richard Hernández & Jessy Sandoval", body_style),
    ]
    
    meta_data = [
        [meta_left[0], meta_right[0]],
        [meta_left[1], meta_right[1]],
        [meta_left[2], meta_right[2]]
    ]
    
    meta_table = Table(meta_data, colWidths=[270, 270])
    meta_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("Detalle de Servicios Cotizados", heading_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#C9A96E'), spaceAfter=10))
    
    # Itemized Table
    headers = [
        Paragraph("Concepto", table_header_text),
        Paragraph("Descripción y Especificaciones", table_header_text),
        Paragraph("Cant.", table_header_text),
        Paragraph("P. Unitario", table_header_text),
        Paragraph("Total", table_header_text)
    ]
    
    row1 = [
        Paragraph("<b>Maestro de Ceremonias</b>", table_text),
        Paragraph("Conducción profesional del evento, maestro de ceremonias para protocolo oficial, brindis y coordinación del programa de bodas en vivo.", table_text),
        Paragraph("1 Serv.", table_text),
        Paragraph("$3,500.00", table_text),
        Paragraph("$3,500.00", table_text)
    ]
    
    row2 = [
        Paragraph("<b>Taquiza Especial (Trompo en Vivo)</b>", table_text),
        Paragraph("Servicio de taquitos de pastor y suadero. Incluye taqueros profesionales cocinando y cortando al momento en el evento desde el trompo. Acompañado de cebollitas asadas, piña picada, nopales, tortillas calientes y salsas artesanales.", table_text),
        Paragraph("120 Px", table_text),
        Paragraph("$120.00", table_text),
        Paragraph("$14,400.00", table_text)
    ]
    
    row3 = [
        Paragraph("<b>Pastel Rectangular de Gala</b>", table_text),
        Paragraph("Pastel rectangular especial decorado con frutos rojos selectos, diseñado para un rendimiento de 120 porciones.", table_text),
        Paragraph("1 Pza.", table_text),
        Paragraph("$6,500.00", table_text),
        Paragraph("$6,500.00", table_text)
    ]
    
    table_data = [headers, row1, row2, row3]
    items_table = Table(table_data, colWidths=[110, 230, 50, 75, 75])
    items_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F65C7A')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E5E5E5')),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('ALIGN', (2,0), (-1,-1), 'CENTER'),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#FFF5F6')]),
    ]))
    story.append(items_table)
    story.append(Spacer(1, 15))
    
    # Totals Table
    totals_left = [
        Paragraph("<b>Condiciones de Pago:</b><br/>"
                  "• 50% de anticipo para formalizar la reservación de la fecha.<br/>"
                  "• 50% restante a liquidar un día antes del evento.<br/>"
                  "• Los precios no incluyen impuestos (16% de IVA en caso de facturación).", meta_style)
    ]
    
    subtotal_val = 3500 + 14400 + 6500
    totals_right = Table([
        [Paragraph("<b>Subtotal:</b>", table_text), Paragraph(f"<b>${subtotal_val:,.2f} MXN</b>", table_text)],
        [Paragraph("<font color='#6D6D6D'>I.V.A. (16%):</font>", table_text), Paragraph(f"<font color='#6D6D6D'>${subtotal_val*0.16:,.2f} MXN</font>", table_text)],
        [Paragraph("<b>Total Neto:</b>", table_text), Paragraph(f"<b>${subtotal_val*1.16:,.2f} MXN</b>", body_bold)]
    ], colWidths=[90, 100])
    totals_right.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (1,0), (1,-1), 'RIGHT'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('LINEBELOW', (0,0), (-1,0), 0.5, colors.HexColor('#E5E5E5')),
        ('LINEBELOW', (0,1), (-1,1), 0.5, colors.HexColor('#E5E5E5')),
    ]))
    
    totals_data = [[totals_left[0], totals_right]]
    totals_table = Table(totals_data, colWidths=[330, 210])
    totals_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(totals_table)
    story.append(Spacer(1, 40))
    
    # Signature Section
    signature_data = [
        [
            Paragraph("_______________________________<br/><b>Richard Hernández</b><br/><font color='#6D6D6D'>Director Creativo & Planner</font>", ParagraphStyle('Sig', parent=body_style, alignment=1)),
            Paragraph("_______________________________<br/><b>Jessy Sandoval</b><br/><font color='#6D6D6D'>Founder & Lead Planner</font>", ParagraphStyle('Sig', parent=body_style, alignment=1))
        ]
    ]
    sig_table = Table(signature_data, colWidths=[270, 270])
    sig_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 15),
    ]))
    story.append(sig_table)
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generated successfully at: {target_path}")

if __name__ == '__main__':
    # Build in both workspace and artifacts folder to be accessible
    build_pdf(pdf_path)
    if not os.path.exists(artifact_dir):
        os.makedirs(artifact_dir)
    build_pdf(artifact_pdf_path)
