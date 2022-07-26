"""Problema 04"""

"""
- Solicitar al usuario que ingrese un número entero
- Indicar si este número es primo o no.
- utilizar una función para el desarrollo de este problema
"""


def primo(numero):
    for valor in range(2, numero):
        if numero%valor==0:
            return False
    return True


num = int(input("Ingrese un número a evaluar: "))
if primo(num):
    print("El número ingresado es primo!!")
else:
    print("El número no es primo!!")