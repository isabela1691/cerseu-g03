"""Uso de la librería de fechas y de tiempo"""

from datetime import datetime

#Creamos una fecha de ejemplo de tipo str (string)
strFecha = "2/6/2023"

"""
Usar estas referencias como tal para indicar el día, mes y año (Si es con mayúscula o minúscula, usarlo como tal)
    d: día
    m: mes
    Y: año
"""
conversion = datetime.strptime(strFecha, "%m/%d/%Y")
print("La fecha formateada es: {}".format(conversion))


"""Traer el mes de la fecha con formato letras usando: strftime de datetime"""

conversionMes = datetime.strftime(conversion, "%d de %b del %Y")

print("Nuestra fecha con cambio en el mes es el siguiente: {}".format(conversionMes))

"""b: reemaplza a 'm' para representar el mes"""