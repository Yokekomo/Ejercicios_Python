# Ejercicio 19: Comprobar si una cadena de caracteres termina con la extensión .py
# Si no es así, agregar la extensión.

def comprobar(cadena):
    if '.py' in cadena:
        return cadena
    else:
        return cadena + ".py"

print(comprobar("files"))
print(comprobar("main.py"))

print("-"*35)

def validar_nombre_archivo(nombre_archivo):
    if len(nombre_archivo) >= 3 and nombre_archivo[-3:] == '.py':
        return nombre_archivo
    return nombre_archivo + ".py"

print(validar_nombre_archivo("file"))
print(validar_nombre_archivo("main.py"))


