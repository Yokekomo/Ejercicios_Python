# Ejercicio 76: Obtener los Argumentos de Línea de Comandos. => $ python programa.py 1 Python

import sys

nombre_script = sys.argv[0]
cantidad_argumentos = len(sys.argv)
argumentos = str(sys.argv)


print('Nombre Script: {}'.format(nombre_script))
print('Cantidad de argumentos: {}'.format(cantidad_argumentos))
print('Lista de argumentos: {}'.format(argumentos))
