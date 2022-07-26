def ingresodedatos():
    a=int(input("Ingresa el primer dato"))
    b=int(input("Ingresa el segundo dato"))
    return a,b
def suma(a,b):
    return a+b
def divisionerronea(a,b):
    print("La división entre los datos ingresados es incorrecta")
    print("la suma de a con b es:{}".format(suma(a,b)))
    a = int(input("Ingresa el primer dato"))
    b = int(input("Ingresa el segundo dato"))
    return a, b

while True:
    a, b = ingresodedatos()
    try:
        div = a/b
        print("la division de a con b es:{}".format(div))
        break
    except ZeroDivisionError:
        a,b=divisionerronea(a,b)

