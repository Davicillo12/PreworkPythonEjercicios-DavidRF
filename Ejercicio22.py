'''
Ejercicio: Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena
'''


def min_may(cadena):
  min = sum(1 for letra in cadena if letra.islower())
  may = sum(1 for letra in cadena if letra.isupper())
  return min , may
print(min_may('Hola, ¿qué tal estás Pedro?'))