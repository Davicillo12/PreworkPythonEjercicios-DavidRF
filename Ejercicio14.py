'''
Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
'''


def suma_lista(n):
  suma = 0
  for numero in n:
    suma += numero
  return suma
lista = (14,21,30,14,25)
print (suma_lista(lista))