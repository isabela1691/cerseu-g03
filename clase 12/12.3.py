"""Ejercicion N°3 de Clases en Python"""

"""

3. Crear un programa que cargue los datos de un triángulo

Reglas:
- Crear una clase triángulo y método para inicializar sus atributos
- Crear un método para imprimir el valor de un lado con un tamaño mayor
- Crear un método para saber qué tipo de triángulo es (equílatero, isósceles o escaleno)
"""


class Triangulo:

    def __init__(self):
        self.lado1 = int(input("Ingrese el valor del primer lado "))
        self.lado2 = int(input("Ingrese el valor del segundo lado "))
        self.lado3 = int(input("Ingrese el valor del tercer lado "))

    def mostrarDatos(self):
        print("Los lados del triángulo tienen los siguientes valores")
        print("Lado 1: {}".format(self.lado1))
        print("Lado 2: {}".format(self.lado2))
        print("Lado 3: {}".format(self.lado3))

    def comparar(self):
        print("El mayor lado es:")
        if self.lado1 > self.lado2 and self.lado1>self.lado3:
            print("Lado 1 con valor: {}".format(self.lado1))
        elif self.lado2 > self.lado3 and self.lado2 > self.lado1:
            print("Lado 2 con valor: {}".format(self.lado2))
        elif self.lado3 > self.lado2 and self.lado3 > self.lado1:
            print("Lado 3 con valor: {}".format(self.lado3))
        elif self.lado3 == self.lado2 and self.lado2!=self.lado1:
            print("Hay dos lados iguales")
        else:
            print("Los tres lados son iguales")

    def tipo(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Es una triángulo equilatero")
        elif self.lado1!=self.lado2 and self.lado1 != self.lado3:
            print("Es una triángulo escaleno")
        else:
            print("Es un triángulo isósceles")


figura = Triangulo()
figura.mostrarDatos()
figura.comparar()
figura.tipo()