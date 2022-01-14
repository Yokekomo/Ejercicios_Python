# Ejercicio 90: Generar n Cantidad de Números Primos Consecutivos.

def generar_primos():
    numero = 2

    yield numero

    while True:
        temporal = numero

        while True:
            temporal += 1
            contador = 1
            contador_divisores = 0

            while contador <= temporal:
                if temporal % contador == 0:
                    contador_divisores += 1

                if contador_divisores > 2:
                    break

                contador += 1

            if contador_divisores == 2:
                yield temporal


g = generar_primos()

primos = [next(g) for _ in range(40)]

print(primos)
