# Ejercicio 69: Ordenar Tres Números de Menor a Mayor sin Usar Condicionales ni Ciclos.

numeros = input('Introduce un número positivo entero de tres cifras: ')
lista_numeros = list(numeros)
lista_numeros = [int(c) for c in lista_numeros]

lista_numeros.sort()
print(lista_numeros)


"""
min = min(lista_numeros)
max = max(lista_numeros)
lista_numeros = sum(lista_numeros) - min - max

print('Los números ordenados: {}{}{}'.format(min, lista_numeros, max))"""
