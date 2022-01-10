# Ejercicio 07: Obtener el nombre de extension de un nombre de archivo

nombre_archivo = input('Ingrese el nombre y ruta del archivo: ')

partes_nombre_archivo = nombre_archivo.split('.')
partes_nombre_archivo2 = nombre_archivo.split('/')

print(nombre_archivo)
print(partes_nombre_archivo2[-2], ' => ', end='')
print(partes_nombre_archivo2[-1])
print(partes_nombre_archivo[-2], ' => ', end='')
print(partes_nombre_archivo[-1])