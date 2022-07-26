"""Problema 01"""

"""
- Pedir al usuario su email y mostrarlo por pantalla indicando que es su dirección
- Validar si es una dirección de correo electrónico.
- El email se considerará si tiene el símbolo del '@'
"""


def validar(email):
    caracaterPedido = "@"
    for letra in email:
        if letra == caracaterPedido:
            return True
    return False


emailUsuario = input("Ingrese su email por favor: ")

if validar(emailUsuario):
    print("Email válido")
else:
    print("Email incorrecto")