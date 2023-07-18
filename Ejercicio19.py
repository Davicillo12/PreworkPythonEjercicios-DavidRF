'''
Ejercicio: Define una función que tome un número y retorne la suma de sus
dígitos.
'''


def digitos_suma(n):
  return sum(int(digito) for digito in str(n))
print(digitos_suma(2875))