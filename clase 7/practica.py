"""niko = "maggie"
lista=[40, 100, "Python",16]
tamaño = len(lista)
print(lista[2])
"""
print("---------------------------------------------------------------------------------------------")
"""Manejo de cadena de caracteres"""
"""Usando el rango y 'step'"""
"""
cadena = "Bienvenido al primer módulo de Python"
cantidad = len(cadena)
subcadena1 = cadena[14:cantidad]
subcadena2 = cadena[2:24:3]

print("El primer bloque de nuestra cadena es: {}".format(subcadena1))
print("El segundo bloque de nuestra cadena es: {}".format(subcadena2))
"""
print("---------------------------------------------------------------------------------------------")
"""Manejo de cadenas"""

"""Concatenación"""
"""
nombre = "Rosario"
apellido = "Deza"

nombreCompleto = "El nombre completo del usuario es: " + nombre + " " + apellido
print(nombreCompleto)

nombreCompleto2 = "El nombre completo del usuario es: {} {}".format(nombre, apellido)
print(nombreCompleto2)

nombre1= "Andrea"
apellido1="Ortiz"
nombreapellido = "El nombre completo del usuario es:"+nombre1+ " "+ apellido1
print(nombreapellido)
"""
print("-------------------------------------------------------------------------------------")
"""Manejo de cadenas"""

"""Multiplicación de cadena"""
"""
technology = "Python"

repetir = 6
for value in range(6):
    print(technology,end="")
print("ave maria","papa con pollo", "patricio parodi","magaly medina", "fiu fiu", sep="", end=" owo")
"""
print("-----------------------------------------------------------------------------")
"""
comida = "                                          Tallarines rojos                          con huancaina             "
print(comida.lstrip().upper().rstrip()+"pollo a la brasa")
print(comida.lstrip().lower())
print(comida.lstrip().title())
print(comida.lstrip())
"""

"""Manejo de cadenas"""
"""
cadena = "Pepsi-es-mejor-que-CocaCola"
listacadena=cadena.split(sep="-")
for value in  listacadena:
    print(value)
"""
print("--------------------------")
"""Manejo de cadenas"""
"""Manejo de impresión de valores de diferentes varaibles"""

"""Tercera forma de imprimir valores"""

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

print("Bienvenido "+ nombre + " usted cuenta con "+edad+" años")

print(nombre.find("p"))

