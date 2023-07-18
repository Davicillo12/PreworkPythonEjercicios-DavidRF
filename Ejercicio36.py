'''
Ejercicio: Define una función que reciba una cadena y cuente el número de
dígitos y letras que contiene.
'''


def contar_digitos_letras(cadena):
  digitos = sum(c.isdigit() for c in cadena)
  letras = sum(c.isalpha() for c in cadena)
  return digitos, letras
print(contar_digitos_letras("Python 3.8"))