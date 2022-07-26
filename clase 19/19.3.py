"""Importación y uso de librerías"""
"""Poniéndole un nombre a una funcionalidad específica"""

#Le ponemos un nombre a la función que usaremos con la palabra reservada: 'as'
#En el siguiente ejemplo se pone de nombre raiz y pot respectivamente para sqrt y pow
from math import sqrt as raiz, pow as pot

numero = int(input("Por favor ingrese un número:"))

valorRaiz = raiz(numero)

print("La raíz cuadrada de su número ingresado es: {}".format(valorRaiz))

valorPotencia = pot(5, 6)
print("El valor de mi potencia es {}".format(valorPotencia))