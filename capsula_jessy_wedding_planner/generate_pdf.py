import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, KeepTogether)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfgen import canvas

ws_dir = r"C:\Users\Lenovo\Documents\primavera brain"
project_dir = os.path.join(ws_dir, "capsula_jessy_wedding_planner")
os.makedirs(project_dir, exist_ok=True)

PINK = colors.HexColor('#F65C7A')
GOLD = colors.HexColor('#C9A96E')
DARK = colors.HexColor('#1F1F1F')
GRAY = colors.HexColor('#6D6D6D')
SOFT = colors.HexColor('#FADADD')
BEIGE = colors.HexColor('#EFE7E1')
LIGHT = colors.HexColor('#F8F6F4')
GREEN = colors.HexColor('#2E7D5B')
RED = colors.HexColor('#C0392B')


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
        self.setFillColor(PINK)
        self.rect(36, 756, 540, 14, fill=True, stroke=False)
        self.setFillColor(colors.white)
        self.setFont("Helvetica-Bold", 7.5)
        self.drawString(46, 760, "PRIMAVERA EVENTS GROUP  |  EL ARTE DE SERVIR")
        self.setFont("Helvetica", 7)
        self.drawRightString(566, 760, "GUION DE PRODUCCION - USO INTERNO")

        self.setStrokeColor(GOLD)
        self.setLineWidth(1)
        self.line(36, 54, 576, 54)

        self.setFont("Helvetica", 7.5)
        self.setFillColor(GRAY)
        self.drawString(36, 40, "Capsula: Jessy - Wedding & Event Planner")
        self.drawRightString(576, 40, f"Pagina {self._pageNumber} de {total}")
        self.restoreState()


base = getSampleStyleSheet()

S = {
    'title': ParagraphStyle('title', parent=base['Normal'], fontName='Helvetica-Bold',
                            fontSize=19, leading=23, textColor=PINK, spaceAfter=2),
    'subtitle': ParagraphStyle('subtitle', parent=base['Normal'], fontName='Helvetica-Bold',
                               fontSize=10, leading=13, textColor=GOLD, spaceAfter=6),
    'meta': ParagraphStyle('meta', parent=base['Normal'], fontName='Helvetica',
                           fontSize=8.5, leading=12, textColor=GRAY),
    'h2': ParagraphStyle('h2', parent=base['Normal'], fontName='Helvetica-Bold',
                         fontSize=12.5, leading=15, textColor=colors.white),
    'h3': ParagraphStyle('h3', parent=base['Normal'], fontName='Helvetica-Bold',
                         fontSize=10.5, leading=13, textColor=DARK,
                         spaceBefore=8, spaceAfter=4),
    'body': ParagraphStyle('body', parent=base['Normal'], fontName='Helvetica',
                           fontSize=9, leading=12.5, textColor=DARK),
    'bold': ParagraphStyle('bold', parent=base['Normal'], fontName='Helvetica-Bold',
                           fontSize=9, leading=12.5, textColor=DARK),
    'ital': ParagraphStyle('ital', parent=base['Normal'], fontName='Helvetica-Oblique',
                           fontSize=8.8, leading=12, textColor=colors.HexColor('#4A4A4A')),
    'label': ParagraphStyle('label', parent=base['Normal'], fontName='Helvetica-Bold',
                            fontSize=7.5, leading=9, textColor=colors.white),
    'td': ParagraphStyle('td', parent=base['Normal'], fontName='Helvetica',
                         fontSize=8.3, leading=11, textColor=DARK),
    'td_b': ParagraphStyle('td_b', parent=base['Normal'], fontName='Helvetica-Bold',
                           fontSize=8.3, leading=11, textColor=DARK),
    'th': ParagraphStyle('th', parent=base['Normal'], fontName='Helvetica-Bold',
                         fontSize=8.5, leading=11, textColor=colors.white),
}

W = 540


def section_bar(text):
    t = Table([[Paragraph(text, S['h2'])]], colWidths=[W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), DARK),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
    ]))
    return t


def speaker(who, text, color, bg):
    tag = Table([[Paragraph(who, S['label'])]], colWidths=[46])
    tag.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), color),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    body = Paragraph(text, S['body'])
    t = Table([[tag, body]], colWidths=[52, W - 52])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (0, 0), 8),
        ('LEFTPADDING', (1, 0), (1, 0), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
        ('LINEBEFORE', (0, 0), (0, 0), 3, color),
    ]))
    return t


def salo(text):
    return speaker("SALO", text, PINK, LIGHT)


def jessy(text):
    return speaker("JESSY", text, GOLD, colors.HexColor('#FBF6EC'))


def note(text, color=GOLD):
    t = Table([[Paragraph(text, S['ital'])]], colWidths=[W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.white),
        ('BOX', (0, 0), (-1, -1), 0.6, color),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    return t


def bullets(items, style=None):
    style = style or S['body']
    rows = [[Paragraph("&bull;", style), Paragraph(i, style)] for i in items]
    t = Table(rows, colWidths=[14, W - 14])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 2),
        ('RIGHTPADDING', (0, 0), (-1, -1), 2),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    return t


story = []
A = story.append

# ─── PORTADA / ENCABEZADO ───────────────────────────────────
A(Spacer(1, 16))
A(Paragraph("Capsula de Video: Jessy", S['title']))
A(Paragraph("LA WEDDING PLANNER QUE ADEMAS ES CONTADORA", S['subtitle']))
A(HRFlowable(width=W, thickness=1.2, color=GOLD, spaceBefore=2, spaceAfter=8))

info = Table([[
    Paragraph("<b>Duracion objetivo</b><br/>3:00 - 3:30 min", S['meta']),
    Paragraph("<b>Formato</b><br/>Entrevista dinamica, 2 personas a cuadro", S['meta']),
    Paragraph("<b>Tono</b><br/>Cercano, agil, humor ligero", S['meta']),
    Paragraph("<b>Salida</b><br/>Cortable en 4 clips (Reels / TikTok)", S['meta']),
]], colWidths=[110, 160, 125, 145])
info.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), LIGHT),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('LEFTPADDING', (0, 0), (-1, -1), 10),
    ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ('TOPPADDING', (0, 0), (-1, -1), 8),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ('BOX', (0, 0), (-1, -1), 0.5, BEIGE),
    ('INNERGRID', (0, 0), (-1, -1), 0.5, BEIGE),
]))
A(info)
A(Spacer(1, 6))
A(Paragraph(
    "Formatos base tomados del catalogo INIT-IDEA: <b>#06 Mitos vs Realidad</b> (educativo, rompe objeciones) "
    "y variante del <b>#05 Esto vs Aquello</b> convertida en <b>Bandera Roja / Bandera Verde</b>.", S['meta']))
A(Spacer(1, 14))

# ─── DIRECCION PREVIA ───────────────────────────────────────
A(section_bar("DIRECCION PREVIA &nbsp;&nbsp;|&nbsp;&nbsp; Leer con Jessy antes de grabar"))
A(Spacer(1, 8))
A(bullets([
    "<b>Regla 1 &mdash; No memorizar.</b> Las respuestas son <i>la idea que tiene que quedar</i>, no un texto para recitar. "
    "Si lo dice con sus palabras, se ve mil veces mas segura.",
    "<b>Regla 2 &mdash; Si se traba, no importa.</b> Grabamos por bloques; cada respuesta se puede repetir. No hay una sola toma.",
    "<b>Regla 3 &mdash; Hablarle a una persona, no a &lsquo;la audiencia&rsquo;.</b> Que imagine que se lo explica a una novia sentada frente a ella.",
    "<b>Regla 4 &mdash; En las dinamicas rapidas, responder corto y seguro.</b> Una frase contundente vale mas que un parrafo. "
    "Si duda, decir &lsquo;depende, y te digo por que&rsquo; tambien genera autoridad.",
]))
A(Spacer(1, 14))

# ─── BLOQUE 0 ───────────────────────────────────────────────
A(section_bar("BLOQUE 0 &nbsp;&nbsp;|&nbsp;&nbsp; HOOK DE APERTURA &nbsp;&nbsp;(0:00 - 0:15)"))
A(Spacer(1, 8))
A(salo("&ldquo;Todo el mundo cree que un wedding planner solo escoge flores y manteles&hellip; Hoy les voy a presentar "
       "a alguien que rompe ese mito por completo, porque ademas de organizar bodas, es contadora. "
       "Y eso cambia TODO. Jessy, &iquest;me ayudas a explicarles por que?&rdquo;"))
A(Spacer(1, 5))
A(jessy("&ldquo;Claro que si &mdash; y si, cambia todo, sobre todo para tu bolsillo.&rdquo; "
        "<font color='#6D6D6D'>(respuesta corta, con seguridad y sonrisa)</font>"))
A(Spacer(1, 5))
A(note("PRODUCCION: corte rapido aqui. Este bloque de 15 segundos funciona solo como clip independiente para TikTok."))
A(Spacer(1, 14))

# ─── BLOQUE 1 ───────────────────────────────────────────────
A(section_bar("BLOQUE 1 &nbsp;&nbsp;|&nbsp;&nbsp; &iquest;QUIEN ES JESSY Y QUE HACE? &nbsp;&nbsp;(0:15 - 1:00)"))
A(Spacer(1, 8))
A(salo("&ldquo;Jessy, presentate. &iquest;Quien eres y que haces exactamente dentro de Primavera Events Group?&rdquo;"))
A(Spacer(1, 6))
A(Paragraph("Base de respuesta &mdash; los 3 puntos que debe tocar:", S['h3']))
A(bullets([
    "<b>Quien es:</b> su nombre, que es socia de Primavera Events Group, y que es <b>contadora de profesion</b>.",
    "<b>Que hace en concreto:</b> administracion financiera del evento, gestion y calendario de pagos, y validacion de proveedores.",
    "<b>Frase clave de posicionamiento:</b> ella se encarga de que <i>los numeros del evento cuadren</i>, "
    "mientras Richard se encarga de que <i>el evento se vea espectacular</i>.",
]))
A(Spacer(1, 6))
A(jessy("<b>Version sugerida:</b> &ldquo;Soy Jessy, socia de Primavera Events Group. Soy contadora de profesion, y dentro del equipo "
        "me toca toda la parte financiera del evento: el presupuesto, el calendario de pagos, y sobre todo la validacion de "
        "proveedores. Richard se encarga del diseno, la logistica y de que el evento se vea espectacular. Yo me encargo de que "
        "los numeros cuadren y de que nadie se lleve una sorpresa desagradable.&rdquo;"))
A(Spacer(1, 10))
A(salo("&ldquo;A ver, explicame esto: &iquest;que le aporta a una novia que su wedding planner sea contadora? "
       "Porque suena a dos mundos completamente distintos.&rdquo;"))
A(Spacer(1, 6))
A(Paragraph("Base de respuesta &mdash; los 4 problemas reales que ella resuelve:", S['h3']))
A(bullets([
    "<b>El presupuesto no se dispara.</b> Hay control real desde el dia uno, no una estimacion optimista.",
    "<b>Los pagos se ordenan en el tiempo.</b> El cliente no recibe todos los cobros encima; se calendarizan.",
    "<b>Detecta los costos ocultos</b> que casi nadie menciona al principio: IVA, propinas, horas extras, descorche, servicio.",
    "<b>Valida que el proveedor sea confiable</b> &mdash; que este formalmente establecido y no desaparezca con el anticipo.",
]))
A(Spacer(1, 6))
A(jessy("<b>Version sugerida:</b> &ldquo;Mira, la parte bonita de una boda todo el mundo la ve. Lo que no se ve es que una boda es, "
        "en el fondo, un proyecto con un presupuesto, varios proveedores y muchos pagos en fechas distintas. Cuando nadie lleva "
        "ese control, es cuando la gente termina pagando mucho mas de lo que habia planeado. Yo llevo esa parte: te ordeno "
        "cuando se paga que, te digo que costos van a aparecer que nadie te menciono, y verifico que cada proveedor sea "
        "confiable antes de que le des un solo peso.&rdquo;"))
A(Spacer(1, 14))

# ─── BLOQUE 2 ───────────────────────────────────────────────
A(section_bar("BLOQUE 2 &nbsp;&nbsp;|&nbsp;&nbsp; DINAMICA 1: MITOS vs REALIDAD &nbsp;&nbsp;(1:00 - 2:00)"))
A(Spacer(1, 8))
A(note("PRODUCCION: ritmo rapido, corte seco entre cada mito. Grafico en pantalla: MITO (X) / REALIDAD (check).", PINK))
A(Spacer(1, 8))
A(salo("&ldquo;Vamos a jugar. Te voy a decir cosas que la gente cree sobre las bodas y los wedding planners, "
       "y tu me dices: &iquest;mito o realidad? Rapido, sin pensarlo mucho.&rdquo;"))
A(Spacer(1, 8))

mitos = [
    ("MITO 1", "&ldquo;Contratar un wedding planner sale mas caro.&rdquo;",
     "Es <b>mito</b>. Un planner con manejo financiero suele <b>ahorrarte</b> dinero: negocia mejor, "
     "evita errores caros y detecta cobros innecesarios.",
     "&ldquo;Mito. Y es el mas comun. Lo que en realidad es caro es equivocarse: contratar mal, pagar de mas por "
     "desconocimiento o tener que resolver algo a ultima hora. Un planner que sabe de numeros te ahorra mas de lo que te cuesta.&rdquo;"),
    ("MITO 2", "&ldquo;El wedding planner nada mas decora.&rdquo;",
     "<b>Mito total.</b> La decoracion es la parte visible; debajo hay administracion, contratos, "
     "coordinacion de proveedores y control de pagos.",
     "&ldquo;Mito. La decoracion es como la punta del iceberg. Abajo hay contratos, calendarios de pago, coordinacion de "
     "diez o quince proveedores distintos... y alguien tiene que llevar todo eso ordenado.&rdquo;"),
    ("MITO 3", "&ldquo;El presupuesto que me dan al principio es el que voy a terminar pagando.&rdquo;",
     "<b>Depende de quien lo arme.</b> Un presupuesto sin desglose real casi siempre crece. "
     "Uno bien hecho contempla desde el inicio los extras previsibles.",
     "&ldquo;Ahi depende, y te digo por que. Si tu presupuesto viene desglosado de verdad &mdash;con IVA, servicio, horas extras "
     "contempladas&mdash; si se respeta. Si te dieron un numero redondito y bonito sin desglose... preparate, porque va a crecer.&rdquo;"),
    ("MITO 4", "&ldquo;Yo puedo organizar mi boda sola, con lo que veo en internet.&rdquo;",
     "<b>Si se puede... pero hay que ser honestos con el costo real:</b> tu tiempo, tu estres, "
     "y el riesgo de contratar proveedores sin verificar.",
     "&ldquo;Claro que se puede, no voy a decir que no. Pero preguntate: &iquest;quieres pasar los meses previos a tu boda "
     "cotizando, persiguiendo proveedores y revisando contratos... o quieres disfrutar tu compromiso? Y sobre todo: "
     "en internet nadie te dice cual proveedor es confiable y cual no.&rdquo;"),
]

for tag, pregunta, idea, sugerido in mitos:
    blk = [
        Paragraph(f"<font color='#F65C7A'><b>{tag}</b></font>", S['h3']),
        salo(pregunta),
        Spacer(1, 4),
        Paragraph(f"<b>Idea a transmitir:</b> {idea}", S['body']),
        Spacer(1, 4),
        jessy(f"<b>Sugerido:</b> {sugerido}"),
        Spacer(1, 9),
    ]
    A(KeepTogether(blk))

A(Spacer(1, 6))

# ─── BLOQUE 3 ───────────────────────────────────────────────
A(section_bar("BLOQUE 3 &nbsp;&nbsp;|&nbsp;&nbsp; DINAMICA 2: BANDERA ROJA / BANDERA VERDE &nbsp;&nbsp;(2:00 - 3:00)"))
A(Spacer(1, 8))
A(note("PRODUCCION: el bloque mas divertido y compartible &mdash; aqui es donde Jessy luce su especialidad. "
       "Graficos de bandera roja / verde en pantalla. Ritmo muy agil.", PINK))
A(Spacer(1, 8))
A(salo("&ldquo;Ahora la buena. Te voy a describir proveedores reales que se le presentan a cualquier novia, "
       "y tu, como contadora, me dices: &iquest;bandera roja o bandera verde?&rdquo;"))
A(Spacer(1, 8))

RED_HEX = '#C0392B'
GREEN_HEX = '#2E7D5B'

flags = [
    ("&ldquo;Me pide el 100% del pago por adelantado.&rdquo;", "ROJA", RED_HEX,
     "&ldquo;Nadie serio te pide todo antes de trabajar. Un anticipo razonable si; el total, no.&rdquo;"),
    ("&ldquo;Me da contrato por escrito, con penalizaciones para ambas partes.&rdquo;", "VERDE", GREEN_HEX,
     "&ldquo;Esa es la mejor senal. Que el contrato lo proteja a el y a ti &mdash; eso habla de un proveedor formal.&rdquo;"),
    ("&ldquo;Me esta dando un precio 40% mas barato que todos los demas.&rdquo;", "ROJA", RED_HEX,
     "&ldquo;Si es demasiado bueno para ser verdad... normalmente lo es. Ahi hay que preguntar que te estan quitando.&rdquo;"),
    ("&ldquo;Me da factura y tiene todo en regla.&rdquo;", "VERDE", GREEN_HEX,
     "&ldquo;Significa que es un negocio formalmente establecido. Si algo sale mal, tienes con quien responder.&rdquo;"),
    ("&ldquo;El &lsquo;contrato&rsquo; es un mensaje de WhatsApp.&rdquo;", "ROJA", RED_HEX,
     "&ldquo;Un WhatsApp no te protege de nada. Si no hay documento, no hay acuerdo.&rdquo;"),
    ("&ldquo;Me desglosa cada concepto de la cotizacion, hasta el ultimo detalle.&rdquo;", "VERDE", GREEN_HEX,
     "&ldquo;Ese es el proveedor que quieres. El desglose es lo que te permite comparar de verdad y saber por que estas pagando.&rdquo;"),
    ("&ldquo;Me pide todo en efectivo, sin recibo de nada.&rdquo;", "ROJA", RED_HEX,
     "&ldquo;Si no queda registro, no hay forma de comprobar que pagaste. Nunca.&rdquo;"),
]

rows = [[Paragraph("SALO DICE...", S['th']),
         Paragraph("VEREDICTO", S['th']),
         Paragraph("JESSY RESPONDE", S['th'])]]
for pregunta, veredicto, col_hex, respuesta in flags:
    rows.append([
        Paragraph(pregunta, S['td']),
        Paragraph(f"<font color='{col_hex}'><b>{veredicto}</b></font>", S['td_b']),
        Paragraph(respuesta, S['td']),
    ])

ftbl = Table(rows, colWidths=[195, 62, 283], repeatRows=1)
fstyle = [
    ('BACKGROUND', (0, 0), (-1, 0), DARK),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('ALIGN', (1, 0), (1, -1), 'CENTER'),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('INNERGRID', (0, 0), (-1, -1), 0.4, BEIGE),
    ('BOX', (0, 0), (-1, -1), 0.6, GOLD),
]
for i, (_, veredicto, _, _) in enumerate(flags, start=1):
    bg = colors.HexColor('#FDF1F0') if veredicto == "ROJA" else colors.HexColor('#F0F7F3')
    fstyle.append(('BACKGROUND', (0, i), (-1, i), bg))
ftbl.setStyle(TableStyle(fstyle))
A(ftbl)
A(Spacer(1, 8))
A(salo("&ldquo;Osea que basicamente... tu eres el filtro antes de que alguien meta la pata.&rdquo;"))
A(Spacer(1, 5))
A(jessy("&ldquo;Exacto. Prefiero que la novia se lleve el susto conmigo revisando, y no el dia de su boda.&rdquo;"))
A(Spacer(1, 14))

# ─── BLOQUE 4 ───────────────────────────────────────────────
A(section_bar("BLOQUE 4 &nbsp;&nbsp;|&nbsp;&nbsp; CIERRE: EL COMPLEMENTO CON RICHARD + CTA &nbsp;&nbsp;(3:00 - 3:30)"))
A(Spacer(1, 8))
A(salo("&ldquo;Ultima pregunta. Richard y tu se reparten el trabajo. En una frase: &iquest;por que funcionan juntos?&rdquo;"))
A(Spacer(1, 6))
A(Paragraph("Idea a dejar:", S['h3']))
A(Paragraph("Son dos perfiles <b>complementarios, no repetidos</b>. El aporta la vision creativa y la ejecucion; "
            "ella aporta el orden financiero y la seguridad. Un evento necesita las dos cosas.", S['body']))
A(Spacer(1, 6))
A(jessy("<b>Version sugerida:</b> &ldquo;Porque una boda necesita emocion y necesita orden. Richard pone la emocion: el diseno, "
        "la logistica, que todo se vea y se sienta increible. Yo pongo el orden: que los numeros cuadren, que los proveedores "
        "sean confiables y que no haya sorpresas. Si solo tienes una de las dos, algo se cae.&rdquo;"))
A(Spacer(1, 10))
A(salo("<b>Cierre a camara + CTA:</b> &ldquo;Ahi lo tienen: un wedding planner no es quien pone las flores, es quien cuida su "
       "evento y su dinero. Si estan organizando una boda, unos XV anos o cualquier evento, escribannos: la primera platica "
       "es sin compromiso. Y si comentan <b>&lsquo;Yo lo quiero&rsquo;</b>, les mandamos por privado el <b>Kit Planner gratuito</b> "
       "con la plantilla de presupuesto que usamos nosotros.&rdquo;"))
A(Spacer(1, 14))

# ─── CORTES PARA REDES ──────────────────────────────────────
A(section_bar("CORTES SUGERIDOS PARA REDES SOCIALES"))
A(Spacer(1, 8))

cortes = [
    ("1", "Hook + &lsquo;soy contadora y eso cambia todo&rsquo;", "15 - 20 s", "TikTok / Reels"),
    ("2", "Mitos vs Realidad (los 4)", "45 - 60 s", "Reels / TikTok"),
    ("3", "Bandera Roja / Verde completo", "60 s", "TikTok (el mas viral)"),
    ("4", "&lsquo;Por que funcionan juntos&rsquo; + CTA", "30 s", "Facebook / Instagram"),
    ("5", "Capsula completa", "3:30", "YouTube / Facebook"),
]
crows = [[Paragraph("CLIP", S['th']), Paragraph("CONTENIDO", S['th']),
          Paragraph("DURACION", S['th']), Paragraph("PLATAFORMA", S['th'])]]
for c in cortes:
    crows.append([Paragraph(f"<b>{c[0]}</b>", S['td_b']), Paragraph(c[1], S['td']),
                  Paragraph(c[2], S['td']), Paragraph(c[3], S['td'])])
ctbl = Table(crows, colWidths=[45, 250, 95, 150], repeatRows=1)
ctbl.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), DARK),
    ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, LIGHT]),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('ALIGN', (0, 0), (0, -1), 'CENTER'),
    ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ('RIGHTPADDING', (0, 0), (-1, -1), 8),
    ('TOPPADDING', (0, 0), (-1, -1), 6),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ('INNERGRID', (0, 0), (-1, -1), 0.4, BEIGE),
    ('BOX', (0, 0), (-1, -1), 0.6, GOLD),
]))
A(ctbl)
A(Spacer(1, 14))

# ─── PENDIENTES ─────────────────────────────────────────────
A(section_bar("POR CONFIRMAR ANTES DE GRABAR"))
A(Spacer(1, 8))
pend = Table([[Paragraph(
    "<b>1. El nombre en pantalla.</b> En la base de datos hay dos versiones distintas del apellido: "
    "<font color='#C0392B'><b>Jessica Patricia Sandoval</b></font> (brain/proyectos) vs. "
    "<font color='#C0392B'><b>W.P. Jessica Rodriguez</b></font> (playbook comercial). "
    "Confirmar cual es el correcto para no rotularlo mal en el video y corregirlo en la base de datos.<br/><br/>"
    "<b>2. Datos duros no incluidos.</b> A proposito no se pusieron anos de experiencia, numero de eventos ni cifras "
    "de ahorro: no estan confirmados y no se inventan. Si Jessy quiere reforzar autoridad, encajan perfecto frases como "
    "<i>&lsquo;en X anos organizando bodas...&rsquo;</i>. Proporcionar los numeros reales para integrarlos al guion.",
    S['body'])]], colWidths=[W])
pend.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#FFF9E6')),
    ('BOX', (0, 0), (-1, -1), 0.8, GOLD),
    ('LEFTPADDING', (0, 0), (-1, -1), 12),
    ('RIGHTPADDING', (0, 0), (-1, -1), 12),
    ('TOPPADDING', (0, 0), (-1, -1), 10),
    ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
]))
A(pend)

out = os.path.join(project_dir, "guion_capsula_jessy.pdf")
doc = SimpleDocTemplate(out, pagesize=letter,
                        leftMargin=36, rightMargin=36,
                        topMargin=64, bottomMargin=64,
                        title="Guion Capsula - Jessy | Primavera Events Group",
                        author="Primavera Events Group")
doc.build(story, canvasmaker=BrandedCanvas)
print(f"Archivo generado: {out}")
