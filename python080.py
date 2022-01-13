# Ejercicio 80: Obtener el Valor Límite de Recursión.

import sys


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(sys.getrecursionlimit())

numero = 50

print(fibonacci(numero))
