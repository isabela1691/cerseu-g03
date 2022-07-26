"""Adivina al numerito"""
import random
def aleatorio():
    numeroaleatorio=random.randint(1,30)
    return numeroaleatorio

def pedirnumero():
    while True:
        try:
            while True:
                numero = int(input("Ingrese un número:"))
                if 0<numero and numero<100:
                    return numero
                else:
                    print("Ingresa un numero nuevo")
        except(ValueError):

            print("El valor ingresado es incorrecto")

from datetime import datetime
def adivina():
    numeroaleatorio1=aleatorio()
    while True:
        numeroingresado=pedirnumero()
        if numeroingresado>numeroaleatorio1:
            print("numero ingresado es mayor al número aleatorio registrado")
            print("Vuelve a ingresar el número")
        elif numeroingresado<numeroaleatorio1:
            print("numero ingresado es menor al número aleatorio registrado")
            print("Vuelve a ingresar el número")
        elif numeroingresado==numeroaleatorio1:
            print("Has ganado")
            fecha = datetime.now()
            print("Se acertó el número en la fecha:{}".format(fecha))
            return numeroingresado
