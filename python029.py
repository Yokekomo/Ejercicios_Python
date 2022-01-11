# Ejercicio 29: Calcular el área de un triángulo 'a = base * altura / 2'

while True:
    try:
        base = float(input("Cual es la base del triangulo: "))
        break
    except:
        print("Debe introducir un número.")

while True:
    try:
        altura = float(input("Y su altura: "))
        break
    except:
        print("Debe introducir un número.")


def calcular_area_triangulo(base, altura):
    area = base * altura / 2
    return area

print(calcular_area_triangulo(base,altura))
