# Ejercicio 03: Obtener la Fecha y la Hora actuales del sistema con el módulo datetime.

import datetime

ahora = datetime.datetime.now()
print(ahora)
print(type(ahora))

print(ahora.strftime('%d/%m/%Y %H:%M:%S'))  #Cadena de formateo pata datetime
print(ahora.strftime('%d/%m/%y'))
print(ahora.strftime('%H:%M'))
