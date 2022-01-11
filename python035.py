# Ejercicio 35: Crear una función únicamente para sumar números enteros

def sumar_enteros(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return x + y
    else:
        raise TypeError('Los valores no eran enteros')


try:
    print(sumar_enteros(10, 6))
    print(sumar_enteros(20, 15))
    print(sumar_enteros(11, 6))
    print(sumar_enteros(30, 16))
except TypeError as e:
    print(e)

print('_' * 30)


def sumar_enteros(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        raise TypeError('Los valores no eran enteros')


try:
    print(sumar_enteros(2, 3))
    print(sumar_enteros(20, '30'))
    print(sumar_enteros(11, 6))
    print(sumar_enteros(30, 16))
except TypeError as e:
    print(e)
