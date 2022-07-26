"""Problema 05"""

"""
- Solicitar al usuario que ingrese un número entero
- Solicitar al usuario que ingrese un dígito
- Mediante una función indicar cuántas veces aparece el dígito en el número ingresado
"""

def frecuencia(numero, digito):
    i = 0
    while numero!=0:
        ultDigito = numero%10
        if ultDigito==digito:
            i = i + 1
        numero = int(numero/10)
    return i

num = int(input("Ingrese un número: "))
uDigito = int(input("Ingrese el dígito a encontrar: "))
print("La frecuencia con la que aparece el dígio : {uDigito}, en el número: {numero} es de {frecuencia} veces"
      .format(uDigito=uDigito, numero=num, frecuencia=frecuencia(num, uDigito)))