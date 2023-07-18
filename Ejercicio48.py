'''
Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla.
'''


def ordenar_por_ultimo_elemento(tuplas):
  return sorted(tuplas, key=lambda x: x[-1])
print(ordenar_por_ultimo_elemento([(1, 2), (3, 1), (4, 5)]))