"""Importando los módulos"""

from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

"""inicializando las variable con valores"""
fileName = "reporte.pdf"
documentTitle = "Reporte"
title = "Python"
subtitle = "Lo primordial ahora es!!"
textLine = [
    'La tecnología nos hace conscientes de',
    'el mundo alrededor de nosotros'
]

image = 'image.png'

"""Creando un objeto pdf"""
pdf = canvas.Canvas(fileName)

"""Estableciendo el título del documento pdf"""
pdf.setTitle(documentTitle)

"""agregando una fuente externa de python"""
pdfmetrics.registerFont(
    TTFont('abc', "SakBunderan.ttf")
)

"""Estableciendo el título y la fuente sobre el lienzo de mi pdf"""
pdf.setFont("abc", 36)
pdf.drawCentredString(300, 700, title)


"""Estableciendo el título dentro del lienzo de mi pdf"""
pdf.setFillColorRGB(255, 125, 24)
pdf.setFont("Courier-Bold", 24)
pdf.drawCentredString(290, 720, subtitle)

"""dibujando una línea"""
pdf.line(30, 680, 550, 680)

"""Creando un texto de muchas líneas usando"""
"""líneas de texto y el ciclo for"""
text = pdf.beginText(50, 640)
text.setFont("Courier", 18)
text.setFillColor(colors.red)

for line in textLine:
    text.textLine(line)
pdf.drawText(text)

"""Dibujando una imagen en una posición específica (x,y, height, weith)"""
"""Sobre el lienzo"""
pdf.drawInlineImage(image, 280, 450, 100, 100)


"""Gerando el pdf"""
pdf.save()