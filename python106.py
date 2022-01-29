# Ejercicio 106: Separar la Ruta de la Extensión de Archivo.

import os

ruta = [r'C:\Descargas\Nueva carpeta (2)\Nueva carpeta\Apuntes11 (1).odt']

for i in ruta:
    print('%s: ' % i, os.path.splitext(i))