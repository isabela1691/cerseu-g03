"""Uso de la librería de fechas y tiempo"""
"""Conversión total del tiempo"""

from datetime import datetime

"""
Usar estas referencias para indicar la hora, el minuto y el segundo (Siempre)
    H: Hora
    M: Minuto
    S: Segundos
"""

"""Obtendremos la cantidad total en segundos usando: timestamp"""
timeNow = datetime.strptime("2023/02/01 20:40:00", "%Y/%m/%d %H:%M:%S").timestamp()

print("La conversión de nuestro valor en tiempo es: {}".format(timeNow))