'''
Ejercicio: Define una función que tome un número y retorne su factorial.
'''

def factorial(n):
  for a in range(1,n):
    n = n * a
  return n 

resultado = factorial(10)
print(resultado)
