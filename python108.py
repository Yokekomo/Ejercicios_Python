# Ejercicio 108: Consultar Propiedades de Archivos y Directorios.

import os

rutas = ['python100.py', r'c:\\Descargas']

for i in rutas:
    print('Archivo: %s' % i)
    print('¿es ruta absoluta? {}'.format(os.path.isabs(i)))
    print('¿es dir? {}'.format(os.path.isdir(i)))
    print('¿es un archivo? {}'.format(os.path.isfile(i)))
    print('¿es un link? {}'.format(os.path.islink(i)))
    print()