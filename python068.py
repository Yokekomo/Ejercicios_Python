# Ejercicio 68: Sumar los Dígitos Integrales de un Número Entero.

# 1234 => 1 + 2 + 3 + 4 = 10

numero = input('Introduzca un número entero positivo: ')

lista_cifras = list(numero)

print(lista_cifras)

lista_cifras = [int(c) for c in lista_cifras]  # Transformamos a números enteros desde la lista de cadenas de caracteres

print(lista_cifras)

suma = sum(lista_cifras)

print(suma)

print('-' * 40)

suma = sum([int(c) for c in numero])  # Versión corta

print(suma)