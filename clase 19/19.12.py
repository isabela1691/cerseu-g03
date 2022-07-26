"""Aquí crearemos las funciones de nuestro módulo que será importado desde el archivo principal"""
"""Separando exclusivamente en funciones únicas y con un sólo objetivo"""

"""Importamos la librería random para poder obtener número aleatorios"""
import random

"""Función para generar números aleatorios"""
def generarNumeros():
    lista = []
    for i in range(15):
        num = random.randint(1, 50)
        lista.append(num)
    return lista


"""Función para ordenar la lista"""
def ordenar(lista):
    return lista.sort()


"""Función para imprimir el valor de la lista"""
def imprimir(lista):
    print(lista)