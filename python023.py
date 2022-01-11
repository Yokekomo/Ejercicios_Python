# Ejercicio 23: Comprobar si un Carácter Dado es una Vocal



def comprobar_caracter(n):

    if len(n) == 1:
        vocales = 'aeiou'
        n = n.lower()
        return n in vocales

    else:
        return False

print(comprobar_caracter('a'))
print(comprobar_caracter('c'))
print(comprobar_caracter('ae'))