"""Manejo de archivos"""
"""Apertura y lectura de archivos"""

"""r: Abre el archivo en modo de lectura"""

file = open("../my_files/file.txt", "r")

"""read(): Nos permite leer el contenido de un archivo"""
print("Contenido de nuestro archivo 'file': {}".format(file.read()))