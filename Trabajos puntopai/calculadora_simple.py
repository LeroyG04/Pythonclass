def sumar(a, b):
    print("Resultado:", a + b)

def restar(a, b):
    print("Resultado:", a - b)

def calculadora():
    print("1. Sumar")
    print("2. Restar")
    opcion = input("Elige una opción: ")

    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    if opcion == "1":
        sumar(a, b)
    elif opcion == "2":
        restar(a, b)
    else:
        print("Opción inválida")

calculadora()
