"""Crear un programa de evaluación de pago de impuestos"""
class Persona:
    def __init__(self):
        self._nombre= input("Introduzca su nombre:")
        self.edad= int(input("Introduzca su edad:"))

    def imprimir(self):
        print("El nombre del usuario es:{}".format(self._nombre))
        print("La edad del usuario es:{}".format(self.edad))
class Empleado(Persona):
    def sueldo(self):
        self.sueldo=float(input("Introduzca su sueldo:"))
    def impuesto(self):
        if self.sueldo>2000:
            self.impuesto=0.1*self.sueldo
        else:
            self.impuesto=0
    def manejodiccionario(self):
        diccionario={"nombre":self._nombre,"edad":self.edad,"sueldo":self.sueldo,"impuesto":self.impuesto}
        print(diccionario)
    def generarArchivoEmpleado(self):
        fileExample = open("Datos de empleados.txt","a+")
        datos=self._nombre+" "+str(self.sueldo)+" "+str(self.impuesto)+","+"\n"
        fileExample.writelines(datos)
    def abrirarchivo(self):
        fileExample = open("Datos de empleados.txt", "r")
        print(fileExample.read())
diccionario1= Empleado()
diccionario1.sueldo()
diccionario1.impuesto()
diccionario1.manejodiccionario()
diccionario1.generarArchivoEmpleado()
diccionario1.abrirarchivo()

