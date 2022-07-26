"""Ejercicion N°4 de Clases en Python"""

"""

4. Crear un programa que pueda realizar depósitos y extracciones de dinero

Reglas:
- El banco va a requerir que al finalizar el día calcule el dinero que se ha depositado
- Crear dos clases, una clase cliente y otra clase banco.
- La clase cliente tendrás los atributos de nombre y cantidad
- Crear los métodos constructor, depositar, extraer, mostrar el total de dinero depositado.
- El banco tendrá 3 atributos de la clase cliente, el método constructor, operar y depósito total
- Instanciar para el caso de 3 personas.
- Mostrar los datos de todos los clientes, incluyendo el monto total de cada uno
"""

class Banco:

    def __init__(self):
        self.cliente1 = Cliente("Susana")
        self.cliente2 = Cliente("Jorge")
        self.cliente3 = Cliente("Elizabeth")

    def operar(self):
        self.cliente1.depositar(500)
        self.cliente2.depositar(100)
        self.cliente3.depositar(80)
        self.cliente1.extraer(40)

    def depositos(self):
        total = self.cliente1.mostrarCantidad() + self.cliente2.mostrarCantidad() + self.cliente3.mostrarCantidad()
        print("El total de dinero que tiene el banco es: {}".format(total))
        self.cliente1.imprimiDatos()
        self.cliente2.imprimiDatos()
        self.cliente3.imprimiDatos()


class Cliente:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = 0

    def depositar(self, monto):
        self.cantidad += monto

    def extraer(self, monto):
        if monto > self.cantidad:
            print("No tienes suficiente lado para que retire")
        elif self.cantidad == 0:
            print("No tienes saldo para retirar")
        else:
            self.cantidad -= monto

    def mostrarCantidad(self):
        return self.cantidad

    def imprimiDatos(self):
        print("{} tiene un cantidad depositada de: {}".format(self.nombre, self.cantidad))


banco = Banco()
banco.operar()
banco.depositos()

banco.cliente1.imprimiDatos()