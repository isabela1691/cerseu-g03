from datetime import datetime
class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.nacionalidad=nacionalidad
        self.fecha= datetime.now()

    def cumpleaños(self):
        self.edad=self.edad + 1
    def fechaderegistro(self):
        return self.fecha

persona1=Persona("Alan", 24, "peruana")
persona2=Persona("Andrea", 17, "peruana")
persona1.cumpleaños()
print("La edad actualizada de la Persona1 es:{}".format(persona1.edad))
persona2.cumpleaños()
print("La edad actualizada de la Persona1 es:{}".format(persona2.edad))
print("La fecha de registro de la persona1 es:{}".format(persona1.fecha))
print("La fecha de registro de la persona2 es:{}".format(persona2.fecha))
