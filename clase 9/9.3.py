"""Programación Orientada a Objetos"""
"""Herencia entre clases"""

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

"""Aplicando Herencia"""
"""Creando nuestra clase hija"""

class CarroVolador(Carro):
    ruedas = 6

    def __init__(self, color, aceleracion, estadoVolando=False):
        super().__init__(color, aceleracion)
        self.estadoVolando = estadoVolando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False


carro1 = Carro("rojo", 30)
carVolador = CarroVolador("Blanco", 40)

print("El color de mi carro volador es: {}".format(carVolador.color))
print("La aceleración de mi carro volador es: {}".format(carVolador.aceleracion))
print("La velocidad inical de mi carro volador es: {}".format(carVolador.aceleracion))
"""Aquí aplicamos el efecto de herencia al usar el método de la clase padre 'Carro'"""

carVolador.acelera()
carVolador.acelera()

print("La velocidad actual de mi carro volador es: {}".format(carVolador.velocidad))

""""""
print("El estado de vuelo de mi carro 1 es: {}".format(carro1.estadoVolando))