# Ejercicio 38: Resolver la expresión algebraica (x + y) * (x + y)

while True:
    try:
        x = float(input("Introduce un número: "))
        break
    except:
        print("No es un número valido.")

while True:
    try:
        y = float(input("Introduce otro número: "))
        break
    except:
        print("No es un número valido.")


def expresion_algebraica(x, y):
    return x ** 2 + 2 * x * y + y ** 2


print(expresion_algebraica(x, y))