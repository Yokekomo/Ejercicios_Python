# Ejercicio 49: Mostrar los archivos de un directorio específico

from os import listdir
from os.path import isfile, join


ruta = r'C:\Descargas'

def listar_directorio(ruta):
    archivos = [a for a in listdir(ruta) if isfile(join(ruta, a))]

    return archivos


listado_archivos = listar_directorio(ruta)

print(listado_archivos)
print(len(listado_archivos))