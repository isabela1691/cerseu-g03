"""Uso de la librería de fechas y tiempo"""
"""Comparación de fechas"""

"""Importamos la librería datetime"""
import datetime

#Declaramos dos variables para dos dato tipo datetime
fecha1 = datetime.datetime(2023, 4, 19) #Tipo de datos datetime
fecha2 = datetime.datetime(2023, 4, 15) #Tipo de datos datetime

"""Empezamos a comparar las fechas que tenemos"""
if fecha1 == fecha2:
    print("Nacieron el mismo día")
elif fecha1 < fecha2:
    print("El niño 1 es mayor que el niño 2")
else:
    print("El niño 2 es mayor que el niño 1")