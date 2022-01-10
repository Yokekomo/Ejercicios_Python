# Ejercicio 12: Imprimir el calendario para un mes y año específico

import calendar

anyo = int(input('Introduce el año: '))
mes = int(input('Introduce el mes. '))

print(calendar.month(anyo, mes))
