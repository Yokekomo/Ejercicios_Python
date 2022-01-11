# Ejercicio 59: Calcular la estatura (dada en pies y pulgadas) en centímetros.

# 1 ft = 30.48 cm
# 1 " = 2.54 cm

while True:
    try:
        pies = float(input("Introduzca su estatura en pies: "))
        break
    except:
        print("Tiene que introducir un valor numérico.")

while True:
    try:
        pulgadas = float(input("Introduzca su estatura en pulgadas: "))
        break
    except:
        print("Tiene que introducir un valor numérico.")

cm = pies * 30.48
cm += pulgadas * 2.54

print(cm)

