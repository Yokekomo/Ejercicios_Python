# Ejercicio 99: Limpiar la Pantalla o Terminal en Windows u Otras Plataformas Operacionales.

import platform
import os
import time

def plataforma():
    time.sleep(2)

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


if __name__ == '__main__':
    plataforma()
