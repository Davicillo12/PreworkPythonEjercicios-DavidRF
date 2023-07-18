'''
Ejercicio: Dado un número, imprime si es positivo o negativo.
'''

x = 4
if x > 0:
  print('positivo')
else:
  print('negativo')
  
  
  
def positividad(n):
  if n > 0:
    return('este numero es positivo')
  elif n == 0:
    return('este numero es 0')
  else:
    return('este numero es negativo')
resultado = positividad(-5)
print(resultado)