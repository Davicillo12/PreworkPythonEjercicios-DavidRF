'''
Ejercicio: Define una función que tome dos listas y retorne True si tienen al
menos un miembro en común, de lo contrario, retorne False.
'''


def numero_comun(lista1, lista2):
  return bool(set(lista1) and set(lista2))
print(numero_comun([4,6,7,3],[5,8,4,9]))