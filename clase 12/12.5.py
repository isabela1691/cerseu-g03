"""Manejo de excepciones"""

"""Para controloar el error de división entre cero y el tipo de datos"""

try:
    #val1 = 100/0
    suma = 1000 + "Hola Pythonistas!"
except ZeroDivisionError:
    print("No es posible una división entre cero!!")
except TypeError:
    print("No es posible sumar tipo de dato entero y tipo string")