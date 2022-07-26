"""Gestión de errores"""
"""Estructura y uso"""

while True:
    try:
        numero = int(input("Ingrese un número entero: "))
    except:   # Dentro del except se activará una acción si ocurre cierto tipo de error dentro del "try"
        print("No es un valor entero")

        print("Se encontró un dato erróneo en al posición 80")