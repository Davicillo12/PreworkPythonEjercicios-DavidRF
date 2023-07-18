'''
Ejercicio: Define una función que reciba una lista de números y retorne el
promedio de los números en la lista.
'''


def promedio(lista):
  return sum(lista) / len(lista)
print(promedio([1, 2, 3, 4, 5]))