'''
Ejercicio: Define una función que reciba un número y retorne la suma de sus
dígitos al cubo.
'''


def suma_al_cubo(n):
  return sum(int(digito)**3 for digito in str(n))
print(suma_al_cubo(237))