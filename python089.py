# Ejercicio 89: Generar Números Aleatorios y Verificar que Todos sean Impares.

from random import randint

def numeros_random(n=15):
    impares = []

    while True:
        numeros = [randint(1,100) for _ in range(n)]

        if all(x % 2 == 1 for x in numeros):
            impares = numeros
            break

    return impares

impares = numeros_random()

print(impares)