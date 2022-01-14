# Ejercicio 85: Comprobar si una Ruta es un Directorio o un Archivo.

import os

ruta = 'archivo.txt'


def validar_ruta(ruta):
    if os.path.isdir(ruta):
        return 'Es un directorio'
    elif os.path.isfile(ruta):
        return 'Es un archivo'
    else:
        return False

print(validar_ruta(ruta))