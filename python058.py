# Ejercicio 58: Calcula la suma de los primeros n números enteros.

n = 10

# Usando la fórmula de Gauss: n*(n+1)/2
suma = n * (n + 1) / 2
print(suma)

print('-' * 40)

# Usando un ciclo

suma = 0

for i in range(1, n + 1):
    suma += i
print(suma)

print('-' * 40)

# Usar la función sum

suma = sum(range(1, n + 1))

print(suma)