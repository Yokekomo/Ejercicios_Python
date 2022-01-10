# Ejercicio 20: Emular el funcionamiento del producto de cadenas de caracteres

# print("Python" * 3) Emular con una función

def producto_cadenas(cadena, repeticion):
    resultado = ""

    for i in range(repeticion):
        resultado += cadena

    return resultado

print(producto_cadenas("Python", 3))