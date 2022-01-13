# Ejercicio 61: Convertir todas las unidades de tiempo en segundos

dias = int(input("Escriba una cantidad de días: "))
horas = int(input("Escriba una cantidad de horas: "))
minutos = int(input("Escriba una cantidad de minutos: "))

dias = dias * 24 * 60 * 60
horas = horas * 60 * 60
minutos = minutos * 60


print(dias)
print(horas)
print(minutos)