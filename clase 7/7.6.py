"""Problema 03"""

"""
- Pedir números al usuario hasta que ingrese 0 para finalizar.
- Mostrar la suma de sus dígitos y la suma de todos los número que hemos ingresado
- Reutilizar la función que se creo en el ejemplo anterior.
"""


def sumarDigito(numero):
    suma=0
    while numero!=0:
        digito = numero%10
        suma = suma+digito
        numero = int(numero/10)
    return suma

sumatoria = 0
num = int(input("Ingrese su número a procesar: "))

while num!=0:
    print("La suma de los dígitos es: {}".format(sumarDigito(num)))
    sumatoria = sumatoria+num
    num = int(input("Ingrese su número a procesar: "))

print("La suma de todos los número que has ingresado es: {}".format(sumatoria))
print("La suma de todos los dígitos es: {}".format(sumarDigito(sumatoria)))