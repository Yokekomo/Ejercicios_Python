# Ejercicio 77: Determinar el Orden de los Bytes en la Arquitectura de Ejecución Actual. #Big-Endian, Little-Endian

import sys

if sys.byteorder == 'little':
    print('Plataforma little-Endian')
else:
    print('Plataforma Big-Endian')
