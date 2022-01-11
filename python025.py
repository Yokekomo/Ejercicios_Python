# Ejercicio 25: Crear un histograma a partir de una lista de enteros

lista = [21, 15, 16, 10, 19, 40, 30, 18]

def crear_histograma(lista, caracter='#'):
    for e in lista:
        print(caracter * e)

print(crear_histograma(lista))