# Ejercicio 100: Obtener el Nombre del Host donde se Ejecuta un Script.

import socket

nombre_host = socket.gethostname()

print(nombre_host)
