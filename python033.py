# Ejercicio 33: Sumar dos números. Si la suma está entre 10 y 30, devolver 30.

def sumar(x, y):
    suma = x + y

    if (suma >= 10) and (suma <= 30):
        return 30
    else:
        return suma


print(sumar(4,20))
print(sumar(16,20))
print(sumar(20,11))

print('-' * 30)

def sumar2(a, b):
    suma = a + b

    if suma in range(10, 30 + 1):
        return 30
    else:
        return suma


print(sumar2(4,20))
print(sumar2(16,20))
print(sumar2(20,11))