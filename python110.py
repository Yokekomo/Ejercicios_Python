# Ejercicio 110: Obtener los Números Divisibles por 7 usando una Función Anónima.

lista_numeros = [8, 9, 62, 3, 695, 21, 375, 25, 396, 52, 36, 98, 54, 23, 767, 65, 251]

variable = lambda x: x % 7 == 0

divisibles = filter(variable, lista_numeros)

print(list(divisibles))

