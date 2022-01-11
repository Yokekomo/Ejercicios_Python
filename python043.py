# Ejercicio 43: Encontrar el nombre del SO, el nombre y la versión de la plataforma

import os
import platform

print(os.name)
print(platform.system())
print(platform.release())
print(platform.version())
print(platform.machine())