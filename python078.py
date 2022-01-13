# Ejercicio 78: Obtener el Listado de los Módulos Incorporados Disponibles.

import sys

nombres_modulos = sorted(sys.builtin_module_names)
nombres_modulos = '\n'.join(nombres_modulos)

print(nombres_modulos)
