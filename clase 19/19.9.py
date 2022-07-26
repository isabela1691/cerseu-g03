"""Uso de la librería datetime"""
"""Operación resta"""

"""Importamos la librería datatime"""
from datetime import datetime

"""Obtenemos los datos tipo datetime"""
datetime1 = datetime.strptime("01-07-2022 20:20:00",  "%d-%m-%Y %H:%M:%S")
datetime2 = datetime.strptime("15-07-2022 20:20:00",  "%d-%m-%Y %H:%M:%S")

"""Realizamos la resta de ambos datos"""
tiempo = datetime1 - datetime2

"""Mostramos el resueltado de la resta"""
print("El tiempo final es: {}".format(tiempo))