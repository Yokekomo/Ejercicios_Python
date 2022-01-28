# Ejercicio 92: Filtrar Números por medio de la Función filter.

lista_numeros = [i for i in range(100)]
print(lista_numeros)

filtro_impares = lambda x: x % 2 == 1
filtro_pares = lambda x: x % 2 == 0

impares = filter(filtro_impares, lista_numeros)

pares = filter(filtro_pares, lista_numeros)

print(list(impares))
print(list(pares))