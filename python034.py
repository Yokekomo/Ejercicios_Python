# Ejercicio 34: Validar dos números. Si son iguales o la suma o el valor absoluto son 5.

def validar_numeros(x, y):

    if x == y or (x + y) == 5 or abs(x - y) == 5:
        return True
    else:
        return False


print(validar_numeros(4, 1))
print(validar_numeros(5, 9))
print(validar_numeros(11, 16))
print(validar_numeros(15, 19))
print(validar_numeros(9, 9))

