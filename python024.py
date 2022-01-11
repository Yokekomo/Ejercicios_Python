# Ejercicio 24: Simular el funcionamiento del operador incorporado in

lista = ['madrid', 'valencia', 'barcelona']

def pertenece_a(lista, elemento):
    for e in lista:
        if elemento == e:
            return True
    return False

print(pertenece_a(lista, 'barcelona'))
print(pertenece_a(lista, 'canarias'))
print(pertenece_a(['Madrid', 'canarias'], 'canarias'))
print(pertenece_a(['Madrid', 'canarias'], 'valencia'))
print(pertenece_a('valencia', 'a'))
print(pertenece_a('valencia', 'x'))