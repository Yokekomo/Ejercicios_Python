# Ejercicio 31: Calcular el minimo común múltiplo(MCM) de dos números

while True:
    try:
        numero1 = int(input("Introduce un número: "))
        break
    except:
        print('Debes de introducir un número.')

while True:
    try:
        numero2 = int(input("Introduce un otro número: "))
        break
    except:
        print('Debes de introducir otro número.')


def mcm(numero1, numero2):
    x = max(numero1, numero2)

    while True:
        if (x % numero1 == 0) and (x % numero2 == 0):
            return  x

        x += 1

print(mcm(numero1, numero2))


