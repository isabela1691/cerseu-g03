"""Programación Orientada a Objetos"""
"""Polimorfismo"""

class Perro():
    def sonido(self):
        print("Guauuuu")


class Gato():
    def sonido(self):
        print("Miauuu")


class Vaca():
    def sonido(self):
        print("Muuu")


vaca = Vaca()
perro = Perro()
gato = Gato()

listaAnimales = [vaca, perro, gato]


def cantar(animales):
    for animal in animales:
        animal.sonido()

"""Aplicando poliporfismo: Es el uso de los métodos que tienen las clases con el mismo nombre pero diferntes acciones"""

cantar(listaAnimales)