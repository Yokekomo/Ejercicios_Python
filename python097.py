# Ejercicio 97: Imprimir el Listado de Variables Especiales que Usa Python.

nombres = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))

print('\n'.join(' '.join(nombres[i:i+2]) for i in range(0, len(nombres), 8)))