'''
Ejercicio: Define una función que tome un número y retorne True si es un
número perfecto, False en caso contrario. Un número perfecto es aquel que es
igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número
perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
'''


def numero_perfecto(n):
  return n == sum(divisor for divisor in range(1, n) if n % divisor == 0)
print(numero_perfecto(6))