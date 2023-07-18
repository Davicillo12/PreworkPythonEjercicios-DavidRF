'''
Ejercicio: Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista.
'''


def primeros_elementos(lista,n):
  return lista[:n]
print(primeros_elementos([2,6,9,7,5,4,3,4],4))