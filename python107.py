# Ejercicio 107: Obtener las Propiedades Básicas de un Archivo.


import os
import  time

archivo = 'python100.py'

print('Archivo: %s' % archivo)
print('Fecha de modificación: {}'.format(time.ctime(os.path.getmtime(archivo))))
print('Fecha de acceso: {}'.format(time.ctime(os.path.getatime(archivo))))
print('Tamaño: %d bytes' % os.path.getsize(archivo))