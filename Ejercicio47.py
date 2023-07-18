'''
Ejercicio: Define una función que reciba una cadena y retorne la misma cadena
pero con las palabras en orden inverso.
'''


def invertir_palabras(cadena):
  return ' '.join(cadena.split()[::-1])
print(invertir_palabras("Hola, ¿cómo estás?"))