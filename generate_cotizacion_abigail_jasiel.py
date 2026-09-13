import os
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

# Define paths
ws_dir = r"C:\Users\Lenovo\Documents\primavera brain"
pdf_path = os.path.join(ws_dir, "cotizacion_abigail_jasiel_boda.pdf")
artifact_dir = r"C:\Users\Lenovo\.gemini\antigravity\brain\ca8d6bb4-a19c-4bc9-9d68-aa23680d99c6"
artifact_pdf_path = os.path.join(artifact_dir, "cotizacion_abigail_jasiel_boda.pdf")
logo_path = os.path.join(ws_dir, "assets", "images", "primaveralogo.jpg")

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
        
        # Header banner decoration
        self.setFillColor(colors.HexColor('#F65C7A')) # Rosa Principal Primavera
        self.rect(36, 756, 540, 16, fill=True, stroke=False)
        self.setFillColor(colors.white)
        self.setFont("Helvetica-Bold", 8)
        self.drawString(44, 761, "PRIMAVERA EVENTS GROUP  |  EXPERIENCIAS EXCLUSIVAS & BANQUETES DE GALA")
        
        # Footer decoration
        self.setStrokeColor(colors.HexColor('#C9A96E')) # Oro Noble
        self.setLineWidth(1)
        self.line(36, 45, 576, 45)
        
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor('#6D6D6D'))
        self.drawString(36, 32, "contacto@primaveraeventsgroup.com  |  Tel. +52 777 458 7923  |  Cuernavaca, Morelos")
        self.drawRightString(576, 32, f"Página {self._pageNumber} de {page_count}")
        
        self.restoreState()

def build_pdf(target_path):
    doc = SimpleDocTemplate(
        target_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=55,
        bottomMargin=60
    )
    
    styles = getSampleStyleSheet()
    
    # Custom Palette
    # Pink: #F65C7A, Gold: #C9A96E, Dark: #1F1F1F, Gray: #555555, SoftPink: #FFF0F2
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=23,
        textColor=colors.HexColor('#F65C7A'),
        spaceAfter=2
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=12,
        textColor=colors.HexColor('#C9A96E'),
        spaceAfter=4
    )
    
    sec_heading = ParagraphStyle(
        'SecHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#1F1F1F'),
        spaceBefore=10,
        spaceAfter=6
    )
    
    subsec_heading = ParagraphStyle(
        'SubSecHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=13,
        textColor=colors.HexColor('#F65C7A'),
        spaceBefore=6,
        spaceAfter=4
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor('#1F1F1F')
    )
    
    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )
    
    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.white
    )
    
    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#1F1F1F')
    )

    story = []
    
    # 1. Header with Logo & Title
    header_text_block = [
        Paragraph("PROPUESTA INTEGRAL DE BODA", title_style),
        Paragraph("PRIMAVERA EVENTS GROUP  —  EL ARTE DE SERVIR EN MORELOS", subtitle_style)
    ]
    
    if os.path.exists(logo_path):
        logo_img = Image(logo_path, width=65, height=65)
        header_table = Table([[logo_img, header_text_block]], colWidths=[75, 465])
        header_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ]))
        story.append(header_table)
    else:
        story.append(header_text_block[0])
        story.append(header_text_block[1])
        story.append(Spacer(1, 6))
        
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#C9A96E'), spaceAfter=8))
    
    # 2. Client & Event Info Block
    meta_left = [
        Paragraph("<b>Novios / Anfitriones:</b> Abigail y Jasiel", body_style),
        Paragraph("<b>Tipo de Evento:</b> Boda Social de Gala", body_style),
        Paragraph("<b>Número de Invitados:</b> 100 Personas", body_style),
    ]
    
    current_date = datetime.date.today().strftime("%d/%m/%Y")
    
    meta_right = [
        Paragraph("<b>Fecha del Evento:</b> 13 de Diciembre", body_style),
        Paragraph(f"<b>Fecha de Cotización:</b> {current_date}", body_style),
        Paragraph("<b>Planners Coordinadores:</b> Richard Hernández & Jessy Sandoval", body_style),
    ]
    
    meta_table = Table([[meta_left[0], meta_right[0]],
                        [meta_left[1], meta_right[1]],
                        [meta_left[2], meta_right[2]]], colWidths=[270, 270])
    meta_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFF0F2')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#F65C7A')),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 8))

    # CORTESÍAS EXCLUSIVAS DE REGALO BOX
    courtesy_text = (
        "<b>🎁 CORTESÍAS ESPECIALES DE REGALO DE LA MARCA (SIN COSTO ADICIONAL):</b><br/>"
        "• <b>Barra Mix de Snacks:</b> Estación especial con variedad de botanas y snacks para el disfrute de tus invitados.<br/>"
        "• <b>2 Chisperos Adicionales de Pirotecnia en Frío:</b> Sumados al show de cascada para maximizar los momentos cúspide."
    )
    courtesy_box = Table([[Paragraph(courtesy_text, body_style)]], colWidths=[540])
    courtesy_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFF5F6')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#F65C7A')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(courtesy_box)
    story.append(Spacer(1, 10))
    
    # 3. SECCIÓN 1: PAQUETE INTEGRAL BASE ($69,300.00)
    story.append(Paragraph("1. Paquete Base de Boda Integral (100 Personas)", sec_heading))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#F65C7A'), spaceAfter=6))
    
    p1_desc = (
        "Propuesta gastronómica, logística y de ambientación para 100 invitados con servicio VIP "
        "y atención personalizada durante todo el evento."
    )
    story.append(Paragraph(p1_desc, body_style))
    story.append(Spacer(1, 6))
    
    inclusions_data = [
        [
            Paragraph("<b>Categoría</b>", table_header_style),
            Paragraph("<b>Detalle de Inclusiones y Servicios</b>", table_header_style)
        ],
        [
            Paragraph("<b>Montaje Religioso</b>", table_cell_style),
            Paragraph("• Silla y mesa especial para el celebrador.<br/>"
                      "• Atril de lectura ceremonial.<br/>"
                      "• Alfombra roja para pasillo.<br/>"
                      "• Equipo de audio dedicado para la ceremonia.", table_cell_style)
        ],
        [
            Paragraph("<b>Coctelería & Bienvenida</b>", table_cell_style),
            Paragraph("• Coctelería sin alcohol: Margaritas, Piñadas y Aguas Frescas artesanales.<br/>"
                      "• 4 mesas periqueras con sombrilla.<br/>"
                      "• 1 Sala Lounge decorativa para confort de invitados.", table_cell_style)
        ],
        [
            Paragraph("<b>Barra de Mezcladores</b>", table_cell_style),
            Paragraph("• Agua natural y hielo en cubo ilimitado.<br/>"
                      "• Refrescos de la línea Coca-Cola (Pepsi, Manzanita, Toronja).<br/>"
                      "• Servicio continuo de ponche y café artesanal.", table_cell_style)
        ],
        [
            Paragraph("<b>Montaje Novios & General</b>", table_cell_style),
            Paragraph("• <b>Mesa Principal:</b> Con Sillón Rey y Reina y arreglo floral de gala.<br/>"
                      "• <b>Montaje General:</b> Mesas de lujo tipo mármol y sillas Tiffany.<br/>"
                      "• Vajilla completa, plato base, cubertería de gala, mantelería fina, loza fina y cristalería completa.", table_cell_style)
        ],
        [
            Paragraph("<b>Banquete de Gala</b>", table_cell_style),
            Paragraph("• <b>Plato Fuerte:</b> Barbacoa de Res tradicional de alta calidad.<br/>"
                      "• <b>Guarniciones:</b> Arroz rojo con verduras y frijoles refritos.<br/>"
                      "• <b>Complementos:</b> Tortillas calientes, salsas caseras, cilantro y limones.", table_cell_style)
        ],
        [
            Paragraph("<b>Estaciones & Impacto</b>", table_cell_style),
            Paragraph("• Set de Letras Gigantes Iluminadas: <b>Letra A, Letra J, Corazón (❤️) y símbolo (&)</b>.<br/>"
                      "• Barra de Esquites interactiva.<br/>"
                      "• <b>🎁 Barra Mix de Snacks (CORTESÍA DE REGALO)</b>.<br/>"
                      "• Show de pirotecnia en frío con remate de cascada (duración 2:30 min) + <b>🎁 2 Chisperos Adicionales (CORTESÍA DE REGALO)</b>.<br/>"
                      "• Entrada Triunfal: Luces de bengala con encendedor y logotipo personalizado de la boda.", table_cell_style)
        ],
        [
            Paragraph("<b>Producción & Cabinas</b>", table_cell_style),
            Paragraph("• DJ profesional, pantallas HD, mampara elegante, luces robóticas, micrófonos inalámbricos, torres iluminadas.<br/>"
                      "• Cabina 360° para videos dinámicos.<br/>"
                      "• Cabina inflable decorativa e interactiva.", table_cell_style)
        ]
    ]
    
    t_inc = Table(inclusions_data, colWidths=[130, 410])
    t_inc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#F65C7A')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E5E5E5')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#FFF9FA')]),
    ]))
    story.append(t_inc)
    story.append(Spacer(1, 6))
    
    price_box_data = [[
        Paragraph("<b>COSTO DEL PAQUETE INTEGRAL BASE (100 PERSONAS):</b>", body_bold),
        Paragraph("<b>$69,300.00 MXN</b>", ParagraphStyle('PriceText', parent=body_bold, fontSize=11, textColor=colors.HexColor('#F65C7A'), alignment=2))
    ]]
    t_price_box = Table(price_box_data, colWidths=[360, 180])
    t_price_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#FFF0F2')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#C9A96E')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_price_box)
    story.append(Spacer(1, 12))
    
    # 4. SECCIÓN 2: OPCIONES DE FOTOGRAFÍA, CINEMATOGRAFÍA Y CABINA 360 (ALFRED PHOTOGRAPHY)
    story.append(Paragraph("2. Opciones Adicionales de Fotografía, Cine y Cabina 360° (Alfred Photography)", sec_heading))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#C9A96E'), spaceAfter=6))
    story.append(Paragraph("<i>(Descripciones detalladas y precios oficiales sin inclusión de imágenes conforme a lo solicitado)</i>", body_style))
    story.append(Spacer(1, 6))
    
    # PAQUETE 1
    p1_content = [
        Paragraph("<b>PAQUETE 1 — FOTOGRAFÍA & VIDEO DIGITAL</b>", subsec_heading),
        Paragraph("<b>Inclusiones del Servicio:</b>", body_bold),
        Paragraph("• Cobertura de foto digital ilimitada el día del evento.<br/>"
                  "• Álbum fotográfico personalizado con capacidad para 200 fotos.<br/>"
                  "• Foto impresa: 200 piezas en tamaño postal 4x6 pulg.<br/>"
                  "• Ampliación 16x24 pulg. con protección y marco.<br/>"
                  "• Estuche de madera personalizado para USB.<br/>"
                  "• Dispositivo USB con película y fotos digitales completas.<br/>"
                  "• Sesión fotográfica previa al evento (Pre-boda).<br/>"
                  "• Videoclip para proyección el día del evento <i>(el cliente proporciona los medios para la proyección)</i>.", body_style),
        Spacer(1, 3),
        Paragraph("<b>Políticas y Forma de Pago (Paquete 1):</b><br/>"
                  "• <b>Costo Total: $8,900.00 MXN</b><br/>"
                  "• Apartado de fecha: $900.00 MXN | Pago el día del evento: $8,000.00 MXN.<br/>"
                  "• Tiempo de entrega: 10 días hábiles para el trabajo terminado.<br/>"
                  "• En caso de requerir venta de fotografía el día del evento, solicitarlo con anticipación.<br/>"
                  "• En caso de no cubrir el monto total el día del evento se aplicará una sanción de $1,500.00 MXN o la eliminación del trabajo realizado.", body_style)
    ]
    
    # PAQUETE 2
    p2_content = [
        Paragraph("<b>PAQUETE 2 — FOTOGRAFÍA, CINEMATOGRAFÍA & DRONE ULTRA HD (4K)</b>", subsec_heading),
        Paragraph("<b>Inclusiones del Servicio:</b>", body_bold),
        Paragraph("• Photobook personalizado y editado con capacidad para 100 fotos <i>(con selección de fotos por el cliente)</i>.<br/>"
                  "• Cobertura de foto digital ilimitada el día del evento.<br/>"
                  "• Ampliación 16x24 pulg. con marco de madera y protección contra líquidos y deterioro.<br/>"
                  "• Estuche de madera personalizado para USB.<br/>"
                  "• Sesión previa al evento (1 hora de servicio en locación).<br/>"
                  "• Videoclip para proyección el día del evento <i>(el cliente proporciona los medios para la proyección)</i>.<br/>"
                  "• Grabación cinemática profesional a <b>2 cámaras</b> (fija y móvil).<br/>"
                  "• Grabación aérea con <b>Drone profesional 4K</b>.<br/>"
                  "• 50 fotos impresas tamaño postal en medida 4x6 pulg.<br/>"
                  "• Dispositivo USB con fotografía digital y película completa en formato Ultra HD.", body_style),
        Spacer(1, 3),
        Paragraph("<b>Políticas y Forma de Pago (Paquete 2):</b><br/>"
                  "• <b>Costo Total: $12,900.00 MXN</b><br/>"
                  "• Apartado de fecha: 10% del valor ($1,900.00 MXN) | Liquidación el día del evento: $11,000.00 MXN.<br/>"
                  "• Tiempo de entrega: 30 días hábiles para el trabajo terminado.<br/>"
                  "• No se vende fotografía impresa a los invitados el día del evento.<br/>"
                  "• En caso de no liquidar el total del contrato el día del evento se sancionará con $2,500.00 MXN o eliminación del material grabado.", body_style)
    ]
    
    # CABINA 360
    p360_content = [
        Paragraph("<b>CABINA BOOTH DE VIDEO 360° (SERVICIO ADICIONAL POR HORA)</b>", subsec_heading),
        Paragraph("<b>Descripción & Inclusiones:</b><br/>"
                  "• Cabina de Video 360 grados que genera videos ilimitados en Slow Motion con efectos visuales y música agregada.<br/>"
                  "• Los videos se comparten al instante al celular de los invitados vía WhatsApp y al concluir el evento se comparten todos los archivos a los anfitriones vía Google Drive.<br/>"
                  "• Incluye la asistencia técnica de 1 operador y 1 técnico durante el servicio.<br/>"
                  "• Préstamo de accesorios (props/sombreros/lentes) para interacción de los invitados. <i>(No incluye letras luminosas)</i>.<br/>"
                  "• <b>Costo: $2,800.00 MXN por Hora de servicio</b>", body_style)
    ]
    
    photo_table_data = [
        [Table([[item] for item in p1_content], colWidths=[520])],
        [Table([[item] for item in p2_content], colWidths=[520])],
        [Table([[item] for item in p360_content], colWidths=[520])]
    ]
    
    photo_table = Table(photo_table_data, colWidths=[540])
    photo_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,0), 0.5, colors.HexColor('#C9A96E')),
        ('BOX', (0,1), (-1,1), 0.5, colors.HexColor('#C9A96E')),
        ('BOX', (0,2), (-1,2), 0.5, colors.HexColor('#C9A96E')),
        ('BACKGROUND', (0,0), (-1,0), colors.white),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#FFF9FA')),
        ('BACKGROUND', (0,2), (-1,2), colors.white),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    
    story.append(photo_table)
    story.append(Spacer(1, 10))
    
    # 5. SECCIÓN 3: RESUMEN COMPARATIVO DE INVERSIÓN
    story.append(Paragraph("3. Resumen de Inversión y Escenarios de Contratación", sec_heading))
    story.append(HRFlowable(width="100%", thickness=0.8, color=colors.HexColor('#F65C7A'), spaceAfter=6))
    
    summary_table_data = [
        [
            Paragraph("<b>Escenario de Contratación</b>", table_header_style),
            Paragraph("<b>Servicios Incluidos</b>", table_header_style),
            Paragraph("<b>Inversión Total (MXN)</b>", table_header_style)
        ],
        [
            Paragraph("<b>Opción A: Banquete Base</b>", table_cell_style),
            Paragraph("Paquete Integral de Boda (100 Px) + Banquete, Montajes, Dj, Pirotecnia, Cabinas + 🎁 <b>Cortesías Incluidas</b>", table_cell_style),
            Paragraph("<b>$69,300.00</b>", table_cell_style)
        ],
        [
            Paragraph("<b>Opción B: Base + Foto Paq. 1</b>", table_cell_style),
            Paragraph("Paquete Integral Base + Cortesías + Foto Digital, Álbum 200 fotos, Ampliación y Pre-boda", table_cell_style),
            Paragraph("<b>$78,200.00</b>", table_cell_style)
        ],
        [
            Paragraph("<b>Opción C: Base + Foto Paq. 2 VIP</b>", table_cell_style),
            Paragraph("Paquete Integral Base + Cortesías + Photobook 100 fotos, Drone 4K, 2 Cámaras y Cine", table_cell_style),
            Paragraph("<b>$82,200.00</b>", table_cell_style)
        ],
        [
            Paragraph("<b>Adicional: Cabina 360° Extra</b>", table_cell_style),
            Paragraph("Servicio adicional por hora de Cabina Booth 360° con videos en Slow Motion", table_cell_style),
            Paragraph("<b>$2,800.00 / hr</b>", table_cell_style)
        ]
    ]
    
    t_summary = Table(summary_table_data, colWidths=[140, 270, 130])
    t_summary.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1F1F1F')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E5E5E5')),
        ('ALIGN', (2,0), (2,-1), 'RIGHT'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#FFF5F6')]),
    ]))
    story.append(t_summary)
    story.append(Spacer(1, 10))
    
    # 6. CONDICIONES DE PAGO Y FIRMAS
    cond_text = (
        "<b>Condiciones de Pago y Políticas de Reservación:</b><br/>"
        "• <b>Anticipo:</b> 50% para formalizar la reservación y congelar la fecha del banquete.<br/>"
        "• <b>Liquidación Banquete:</b> 50% restante a liquidar un día antes de la celebración del evento.<br/>"
        "• <b>Pagos Fotografía:</b> Reservación según paquete ($900 o 10%) y saldo el día del evento.<br/>"
        "• Los precios presentados no incluyen IVA en caso de requerir factura fiscal."
    )
    
    cond_box = Table([[Paragraph(cond_text, body_style)]], colWidths=[540])
    cond_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8F6F4')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#C9A96E')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(cond_box)
    story.append(Spacer(1, 18))
    
    # Signatures
    sig_data = [
        [
            Paragraph("_______________________________<br/><b>Richard Hernández</b><br/><font color='#6D6D6D'>Director Creativo & Planner</font>", ParagraphStyle('Sig1', parent=body_style, alignment=1)),
            Paragraph("_______________________________<br/><b>Jessy Sandoval</b><br/><font color='#6D6D6D'>Founder & Lead Planner</font>", ParagraphStyle('Sig2', parent=body_style, alignment=1))
        ]
    ]
    sig_table = Table(sig_data, colWidths=[270, 270])
    sig_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(sig_table)
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generado exitosamente en: {target_path}")

if __name__ == '__main__':
    build_pdf(pdf_path)
    if not os.path.exists(artifact_dir):
        os.makedirs(artifact_dir)
    build_pdf(artifact_pdf_path)
