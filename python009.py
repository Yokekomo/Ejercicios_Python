# Ejercicio 09: Mostrar la fecha de un evento almacenada en una tupla

fecha_evento = (2023, 9, 14)
print(type(fecha_evento))

print('El evento programado es para la fecha: %i/%i/%i' % fecha_evento)

anyo, mes, dia = fecha_evento
print(f'El evento esta programado para el dia {dia} del mes {mes} y el año {anyo}')
print(f'El evento programado es para la fecha: {dia}/{mes}/{anyo}')

