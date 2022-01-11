# Ejercicio 51: crear una tupla nombrada para representar un punto en el plano.

from collections import namedtuple
from math import sqrt

"""
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
"""

Punto = namedtuple('Punto', ['x', 'y'])

punto1 = Punto(2, 3)
punto2 = Punto(-3, -5)

print(punto1)
print(punto2)

def calcular_distancia_entre_dos_puntos(punto1, punto2):
    return sqrt((punto1.x - punto2.x) ** 2 + (punto1.y - punto2.y) ** 2)


print(calcular_distancia_entre_dos_puntos(punto1, punto2))
