"""Uso de la librería de fechas y tiempos"""

from datetime import date, time, datetime

"""Obtenemos la fecha y hora actual con la función today() de date"""
fecha = date.today()
print("La fecha a manejar es la siguiente: {}".format(fecha))

tiempo = datetime.now()

print("El tiempo actual es: {}".format(tiempo))

anio = tiempo.year   #Obtenemos el año
mes = tiempo.month   #Obtenemos el mes
dia = tiempo.day     #Obtenemos el día

print("Año actual es: {}".format(anio))
print("Mes actual es: {}".format(mes))
print("Día actual es: {}".format(dia))

"""Uso del dateime para extraer el hora, minuto y el segundo"""

hora = tiempo.hour      #Obtenemos la hora
minuto = tiempo.minute  #Obtenemos el minuto
segundo = tiempo.second #Obtenemos el segundo

print("La hora exacta son las : {} horas con {} minutos y {} segundos".format(hora, minuto, segundo))
