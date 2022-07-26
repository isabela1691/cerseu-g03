"""Uso de la librería datetime"""
"""Usando la función strptime"""

from datetime import datetime

print("La fecha actual {}".format(datetime.now()))

"""strptime: Convierte en una cadena de texto tipo datetime"""
"""Primer parámetro: cadena de texto datetime, segundo parámetro: formato datetime requerido"""
date = datetime.strptime("01-07-2022 20:20:00",  "%d-%m-%Y %H:%M:%S")

"""strftime: Nos permite manejar una cadena de texto incrustando el día, mes, año y tiempo que se obtuvieron en date"""
print(date.strftime("%d/%m del año %Y, son las %H horas con %M minutos"))