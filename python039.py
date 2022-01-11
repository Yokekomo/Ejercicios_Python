# Ejercicio 39: Calcular el valor futuro para una cantidad, interés y número de años específicos

def valor_furturo(vp, i, n):
    return vp * (1 + i) ** n


valor_presente = 10000
interes = 3.5
periodos = 7

print(valor_furturo(valor_presente, interes / 100, periodos))
