# Ejercicio 73: Calcular el Punto Medio de un Segmento de Recta.

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y) # Que se vea el bloque de memoria

def punto_medio(punto_1, punto_2):
    x = (punto_1.x + punto_2.x) / 2
    y = (punto_1.y + punto_2.y) / 2

    return Punto(x, y)


punto_1 = Punto(2, 3)
punto_2 = Punto(-5, -7)


m = punto_medio(punto_1, punto_2)

print(m)