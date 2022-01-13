# Ejercicio 67: Convertir kilopascales (kPa) en presión psi, mmHg, y atm.


def conversion_kilopascales(kpa):
    psi = kpa / 6.89475729
    mmhg = kpa *760 / 101.325
    atm = kpa / 101.325

    return psi, mmhg, atm    # Devolver una tupla

kilopascales = float(input('Introduce la presion en Kilopascales(KPa): '))


print(conversion_kilopascales(kilopascales))
