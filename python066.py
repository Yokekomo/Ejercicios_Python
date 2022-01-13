# Ejercicio 66: Calcula el índice de masa corporal (IMC). IMC=P/A*A(m)


def imc(altura, peso):
    return peso / altura ** 2


peso = float(input("Introduce tu peso en kg: "))
altura = float(input('Introduce tu altura en m: '))

indice = imc(altura, peso)

print('Su IMC es: {}'.format(indice))







