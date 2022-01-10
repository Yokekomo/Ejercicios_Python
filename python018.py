# Ejercicio 18: Calcular la suma de tres números, e incluir una condición de igualdad

def suma_numeros(a,b,c):
    suma = a + b + c
    if a == b and b == c:
        suma = suma * 3
    return suma

print(suma_numeros(4,4,4))
print(suma_numeros(5,8,2))
