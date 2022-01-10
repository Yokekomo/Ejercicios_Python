# Ejercicio 17: Crear una función para determinar si un número es cercano a 1000 o 2000

def cercania(n):
    return (abs(1000 - n) < 499) or (abs(2000 - n) < 499)

print(cercania(1600))