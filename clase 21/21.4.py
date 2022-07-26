"""Manejo de archivos"""

"""w: Abre el archivo para poder escribir sobre el"""

file = open("my_files/file2.txt", "w")

file.write("Lenguaje multiplataforma\n")
file.write("Está basado en POOO\n")
file.write("Python es completamente intuitivo")

file = open("my_files/file2.txt", "r")

print("Nuestro file tiene el siguiente contenido: {}".format(file.read()))

"""Cierre del archivo"""
file.close()