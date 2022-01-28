# Ejercicio 96: Imprimir el Estado de la Pila de Llamadas.

import traceback

def funcion3():
    traceback.print_stack()
    print('Hola')

def funcion2():
    funcion3()

def funcion1():
    funcion2()

def funcion():
    funcion1()

funcion()