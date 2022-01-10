# Ejercicio 10: Solicita al usuario un número n y calcular n + nn + nn

n = int(input("Introduce un número: "))

nn = int('{}{}'.format(n, n))
nnn = int('{}{}{}'.format(n, n, n))
resultado = n + nn + nnn

print(f'{n} + {nn} + {nnn} = ', resultado)



