"""Problema 02"""

"""
- Pedir números al usuario hasta que ingrese 0.
- Mostrar la suma de sus dígitos
-  Crear una función que realice dicha suma
"""


def sumarDigito(numero):
    suma=0
    while numero!=0:
        digito =numero%10
        suma = suma+digito
        numero = int(numero/10)
    return suma


num = int(input("Ingrese número a procesar: "))
while num!=0:
    print("Suma {}".format(sumarDigito(num)))
    num = int(input("Ingrese número a procesar: "))