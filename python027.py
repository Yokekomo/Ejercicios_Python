# Ejercicio 27: Generar un conjunto de números aleatorios y determinar cuáles son impares y cuáles pares

from random import randint

numeros_aleatorios = [randint(1,100) for _ in range(20)]
print(numeros_aleatorios)

numeros_impares = filter(lambda n: n % 2 == 1, numeros_aleatorios)
print(list(numeros_impares))

numeros_pares = filter(lambda n: n % 2 == 0, numeros_aleatorios)
print(list(numeros_pares))

def encontrar_impares(lista):
    impares = []
    pares = []

    for n in lista:
        if n % 2 == 1:
            impares.append(n)
        else:
            pares.append(n)

    return impares, pares

print(encontrar_impares(numeros_aleatorios))