# Ejercicio 37: Crear una jerarquía de herencia básica

class Persona:
    def __init__(self, documento, nombre, correo):
        self.documento = documento
        self.nombre = nombre
        self.correo = correo

class Estudiante(Persona):
    def __init__(self, documento, nombre, correo, carnet, carrera):
        super().__init__(documento, nombre, correo)
        self.carnet = carnet
        self.carrera = carrera


albano = Estudiante('2222222y', 'Albano', 'albano"gmail.com', '123', 'Programación')

print(isinstance(albano, Estudiante))
print(isinstance(albano, Persona))
