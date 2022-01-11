# Ejercicio 26: Emular el funcionamiento de la función join para concatenar una lista

lista = ['P', 'y', 't', 'h', 'o', 'n']
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(''.join(lista))
print(''.join([str(n) for n in numeros]))

print('-' * 20)

def concatenar_cosas(listas):
    resultado = ''

    for n in listas:
        resultado += str(n)

    return resultado

print(concatenar_cosas(lista))
print(concatenar_cosas(numeros))

