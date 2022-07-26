"""Uso de la librería datetime"""
"""Importando la librería datetime"""
from datetime import datetime

"""Creando una lista con los días de la que usaremos para mostrar en la siguiente línea"""
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


"""weekday: Obtendremos el día de la semana de la fecha que estamos enviando como primer parámetro"""
d = datetime.strptime("2022/07/19 20:40:00", "%Y/%m/%d %H:%M:%S")
print(dias[d.weekday()]+" día")