# Ejercicio 95: Validar si una Cadena de Caracteres Representa un Número.

cadena = 346643
cadena2 = 'ihis'


def esnumerico(cadena):
    try:
        float(cadena)
        return True
    except (TypeError, ValueError):
        return False

print(esnumerico(cadena))
print(esnumerico(cadena2))

