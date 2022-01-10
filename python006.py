# Ejercicio 06: Obtener un conjunto de números separados por coma y crear una lista

numeros = '862478423t784378432'
numeros = list(numeros)
print(numeros)

numeros2 = input('Introduce un número de 10 cifras: ')
numero2 = list(numeros2)
print(numero2)

numeros3 = input('Introduce más números pero separados por coma: ')
numeros3 = numeros3.split(',')
print(numeros3)
