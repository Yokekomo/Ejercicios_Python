# Ejercicio 28: Calcular la diferencia de conjuntos con elementos con nombres de colores
"""
colores_lista_1 = ['Negro', 'Rojo', 'Verde', 'Blanco']
colores_lista_2 = ['Blanco', 'Azul', 'Verde', 'Gris', 'Amarillo', 'Verde']
"""

colores_lista_1 = ['Negro', 'Rojo', 'Verde', 'Blanco']
colores_lista_2 = ['Blanco', 'Azul', 'Verde', 'Gris', 'Amarillo', 'Verde']

colores_conjunto_1 = set(colores_lista_1)
colores_conjunto_2 = set(colores_lista_2)

diferencia = colores_conjunto_1.difference(colores_conjunto_2)

print(diferencia)

