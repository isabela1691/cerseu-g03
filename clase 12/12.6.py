"""Manejo de excepciones"""

"""Para controloar el error de división entre cero y el tipo de datos"""
"""Múltiples excepts en uno sólo"""

try:
    #valor1 = 500/0
    suma = "Hola Pythonistas" + 5000
except (ZeroDivisionError):
    print("Ha ocurrido un error de DivisionZero o TypeError")