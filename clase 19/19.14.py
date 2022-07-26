"""Función principal"""
"""Llama a las demás funciones de mi módulo externo"""

"""Dentro de este archivo principal se realizará el llamada del módulo"""
"""Obteniendo un archivo principal más limpio y compacto"""

"""Importamos sólo las funciones que necesitaremos necesitemos usar dentro del archivo principal"""
from funciones import suma, multiplicacion, resta

"""Pedimos dos vlores al usuario el cuál los ingresará por consola"""
x = int(input("Ingrese un valor: "))
y = int(input("Ingrese su segundo valor: "))

print("El resultado de las suma de los dos valores ingresado es: {}".format(suma(x, y)))

print("El resultado de la multiplicación de los dos valores ingresado es: {}".format(multiplicacion(x, y)))

print("El resultado de la resta de los dos valores ingresado es: {}".format(resta(x, y)))