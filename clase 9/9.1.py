"""Programación Orientada a Objetos"""
"""Atributos de datos a una clase"""
class Carro:
    """Atributos"""
    ruedas = 4

    """Contructor: Valores que va a tener por defecto mi clase cuando se le instancia a una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Métodos: Son las funciones de la clase"""
    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad

carro1 = Carro("Rojo", 20)

print("El color de mi primer carro es: {}".format(carro1.color))
carro1.marchas = 1000

carro2 = Carro("Blanco", 40)
"""Se agegará un atributo de dato a la instancia del ssegundo carro"""

carro2.marchas = 2000

print("El número de de marchas que peude dar mi segundo carro es: {}".format(carro2.marchas))

"""No es posible llamar un atributo de dato que se le fue asiganda a otra instancia de la clase"""
print("El número de de marchas que peude dar mi primer carro es: {}".format(carro1.marchas))