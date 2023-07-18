'''
 Ejercicio: Define una función que tome un número y determine si es primo.
'''


def primo(n):
  if n < 2:
    return False
  for number in range(2, n):
    if n % number == 0:
      return False
  return True
resultado = primo(2)
print(resultado)
