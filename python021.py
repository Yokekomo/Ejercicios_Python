# Ejercicio 21: Generar los n Primeros Números Pares Positivos.

def genera_pares(n):
    pares =[]
    contador = 0
    numeros = 0

    while contador < n:
        if numeros % 2 == 0:
            pares.append(numeros)
            contador += 1
        numeros += 1
    return pares

n = int(input("Ingresa la cantidad de números pares a calcular: "))

if n > 0:
    pares = genera_pares(n)
    print(pares)
    print(f'Ha ingresado', len(pares),"pares")
else:
    print('Advertencia el número ingresado tiene que ser positivo.')
