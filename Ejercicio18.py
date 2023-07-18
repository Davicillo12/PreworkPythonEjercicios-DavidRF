'''
Ejercicio: Define una función que tome una lista y retorne una nueva lista con
los elementos únicos de la lista original.
'''


def lista_unicos(lista):
  return list(set(lista))
print(lista_unicos([3,3,4,6,6,7,7,2,8,3,2,7]))