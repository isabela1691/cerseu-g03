"""Programación funcional"""

var1 = int(input("Ingrese el primer valor: "))
var2 = int(input("Ingrese el segundo valor: "))


def resta(x, y, z=20):
    resultado = x-y-z
    return resultado


""""""
print("El resultado de mi función es: {}".format(resta(var1, var2, 40)))