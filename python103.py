#  Ejercicio 103: Obtener el Nombre de Archivo de una Ruta Absoluta.

import os

ruta = r'C:\Users\thebu\PycharmProjects\python\ejercicios_python_1000\python100.py'

nombre_archivo = os.path.basename(ruta)


print(nombre_archivo)