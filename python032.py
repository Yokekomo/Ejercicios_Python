# Ejercicio 32: Calcular la suma de tres números si todos son diferentes, en caso contrario la suma será 0.

while True:
    try:
        numero1 = int(input("Introduce el primer número: "))
        break
    except:
        print("Debe de introducir un número.")

while True:
    try:
        numero2 = int(input("Introduce el segundo número: "))
        break
    except:
        print("Debe de introducir un número.")

while True:
    try:
        numero3 = int(input("Introduce el tercer número: "))
        break
    except:
        print("Debe de introducir un número.")

def sumar(numero1, numero2, numero3):
    if numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
        return 0
    else:
        return numero1 + numero2 + numero3

print(sumar(numero1,numero2,numero3))