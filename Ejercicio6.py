'''
Ejercicio: Dado un número, imprime si es par o impar.
'''

x = 12
if x % 2 == 0 :
  print('12 es par')
else :
  print('12 es impar')
  
  
def par_impar(n):
  if n % 2 == 0:
    return('este numero es par')
  else:
    return('este numero es impar')
resultado = par_impar(5)
print(resultado)