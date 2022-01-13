# Ejercicio 79: Obtener le Tamaño en Bytes de un Objeto.

import sys

python = 'Python'
javascript = 'Javascript'
java = 'Java'
csharp = 'C#'

print('La cadena %s ocupa %i bytes' % (python, sys.getsizeof(python)))
print('La cadena %s ocupa %i bytes' % (javascript, sys.getsizeof(javascript)))
print('La cadena %s ocupa %i bytes' % (java, sys.getsizeof(java)))
print('La cadena %s ocupa %i bytes' % (csharp, sys.getsizeof(csharp)))
