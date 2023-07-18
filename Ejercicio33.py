'''
Ejercicio: Define una función que reciba una lista de números y retorne el
segundo número más grande de la lista.
'''


def segundo_maximo(lista):
  return sorted(set(lista), reverse=True)[1]
print(segundo_maximo([1, 4, 8, 7, 7, 5]))