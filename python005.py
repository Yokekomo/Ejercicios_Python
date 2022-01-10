# Ejercicio 05: Obtener la representación inversa de una cadena de caracteres.

cadena = '¿Hola Python como estas?'

for i in range(len(cadena) -1, -1, -1):
    print(cadena[i], end='')

print()

print(cadena[::-1])

for i in range(len(cadena) -1, -1, -1):
    print(cadena[i], end='-')

print()

print(cadena[1:23:])

print(len(cadena))


