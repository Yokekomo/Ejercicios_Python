# Ejercicio 65: Convertir Segundos en días, horas, minutos y segundos.

segundos = int(input("Introduce una cifra: "))

dias = segundos // (24 * 60 * 60)
segundos = segundos % (24 * 60 * 60)
horas = segundos // (60 * 60)
segundos = segundos % (60 * 60)
minutos = segundos // 60
segundos = segundos % 60

print(round(dias), round(horas), round(minutos))