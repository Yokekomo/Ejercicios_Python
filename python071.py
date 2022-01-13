# Ejercicio 71: Calcular el Tamaño de un Archivo.

import os

ruta_archivo = r'C:/Users/thebu/OneDrive/Asztali gép/HomeWorksProjects/Python_Basico/Ejercicios_Python/python071.py'

def calcular_tamaño_archivo(ruta_archivo):
    try:
        return  os.path.getsize(ruta_archivo)
    except expression as identifier:
        return None


print(calcular_tamaño_archivo(ruta_archivo))
