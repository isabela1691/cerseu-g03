"""
2. Hacer un programa que pueda generar 15 números aleatorios entre 1 y 50.

Reglas:
- Mostrar la lista con los número random que se han obtenido
- Ordenar los valores de la lista e imprimirlos en pantalla.
- Modularizar o dividir nuestro programa en funciones.

"""

"""Dentro de este archivo principal se realizará el llamada del módulo"""
"""Obteniendo un archivo principal más limpio y compacto"""

from func import *

miLista = generarNumeros()
imprimir(miLista)
ordenar(miLista)
imprimir(miLista)