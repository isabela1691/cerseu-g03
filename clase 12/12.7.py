"""Manejo de excepciones"""
"""Análisis del try except"""

try:
    valor1 = 1000/4
    #valor2 = 1000 / 0
except:
    print("Entró al except, ha ocurrido una excepción!!!")
else:
    print("Entró al else, no ha ocurrido un error")