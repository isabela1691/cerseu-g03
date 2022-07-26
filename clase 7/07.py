"""Programación funcional"""

var1 = int(input("Ingrese un primer valor: "))
var2 = int(input("Ingrese un segundo valor: "))


def multplicar(a, b):
    resultado = a*b
    return resultado


print("El resultado de mi función es: {}".format(multplicar(var1, var2)))