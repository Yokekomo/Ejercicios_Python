# Ejercicio 45: Encontrar la ruta del Script actual en ejecución.

import os

print(os.path.realpath(__file__))