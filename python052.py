# Ejercicio 52: Imprimir cadenas de caracteres en la salida estándar de errores

import sys

while True:
    try:
        x = int(input("Introduce un número: \n"))
        print('-' * 40)
        break
    except:
        print('Este es un error Terrible', file=sys.stderr)
        print('-' * 40)


def error_print(*args, **kwargs):
    print(*args, file=sys.stderr)

error_print('Este es un mensaje de error!!!!')