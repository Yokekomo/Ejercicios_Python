# Ejercicio 63: Comprobar si el nombre de un archivo corresponde con una ruta absoluta.

from os import path

nombre_archivo = 'archivo.txt'
ruta_absoluta = r'C:\Users\thebu\OneDrive\Asztali gép\HomeWorksProjects\Python_Basico\Ejercicios_Python\archivo.txt'

print(path.isabs(nombre_archivo))
print(path.isabs(ruta_absoluta))
print(__file__)
print(path.isabs(__file__))
