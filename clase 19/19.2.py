"""Importación y uso de librerías"""
"""Uso específico de una funcionalidad para una librería o dependencia"""

#Importamos solamente las librerías que usaremos en nuestro programa
from math import sqrt, pow
import math

numero = int(input("Por favor ingrese un número:"))

valorRaiz = sqrt(numero)

print("La raíz cuadrada de su número ingresado es: {}".format(valorRaiz))

valorPotencia = pow(5, 6)
print("El valor de mi potencia es {}".format(valorPotencia))

print("Todas funciones que tiene la librería math es: {}".format(dir(math)))