"""Aquí crearemos las funciones de nuestro módulo que será importado desde el archivo principal"""
"""Separando exclusivamente en funciones únicas y con un sólo objetivo"""

"""Importamos la librería random para poder obtener número aleatorios"""
import random

"""Función para pedir un número"""
def cargar():
    return int(input("ingrese un numero: "))


"""Función para obtener un número aleatorio"""
def cargarAleatorio():
    return random.randint(1, 40)


"""Función para adivinar al número"""
def adivinaNumero():
    numero = cargarAleatorio()
    print("Bienvenido al juego de adivina al numerito!!")
    esNumero = False
    while esNumero == False:
        #Solicitamos el número aleatorio
        x = cargar()
        #En caso el usuario haya acertado con el número que se cargó aleatoriamente en la variable 'numero'"""
        if numero == x:
            print("Has ganado!!!")
            esNumero = True
        #En caso el usuario haya ingresado un número mayor que está dentro de la variable 'numero'"""
        elif numero < x:
            print("El valor ingresado es menor")
        #En caso el usuario haya ingresado un número menor que está dentro de la variable 'numero'"""
        else:
            print("El valor es mayor")