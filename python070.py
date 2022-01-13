# Ejercicio 70: Ordenar un Conjunto de Archivos por Fecha de Creación.

import glob
import os

ruta = r'C:/Users/thebu/OneDrive/Asztali gép/HomeWorksProjects/Python_Basico/Ejercicios_Python/'

archivos = glob.glob(ruta + os.path.sep + '*.py')

archivos.sort(key=os.path.getctime)

print('\n'.join(archivos))