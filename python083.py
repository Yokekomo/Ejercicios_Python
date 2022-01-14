# Ejercicio 83: Comprobar si Todos los Elementos de una Lista son mayores respecto a un número.

lista = [13, 5, 3, 9, 45, 77, 5, 4, 3]

print(all(x > 3 for x in lista))
print(all(x > 1 for x in lista))