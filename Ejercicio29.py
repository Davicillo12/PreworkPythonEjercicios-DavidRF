'''
Ejercicio: Define una función que reciba una lista de palabras y un entero n, y
retorne la lista de palabras que son más largas que n.
'''


def filtrar_palabras(lista_palabras, n):
  return [palabra for palabra in lista_palabras if len(palabra) > n]
print(filtrar_palabras(["casa", "raton", "paisaje", "cristalino"], 5))