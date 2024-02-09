# Crie um algorítmo que leia um número e mostre o dobro, o triplo e a raiz quadrada.

num = int(input('Digite um número inteiro: '))
print('O dobro de {} vale {}'.format(num, (num * 2)))
print('O triplo de {} vale {}\n'.format(num, (num * 3)))

import math
# Raiz quadrada com o método pow()
print('A raiz quadrada de {} vale {:.2f}'.format(num, math.pow(num, (1/2))))
print(f'A raiz quadrada de {num} é {math.pow(num, (1/2))}')
# Raiz quadrada com o método sqrt()
print('A raiz quadrada de {} vale {:.2f}'.format(num, math.sqrt(num)))
print(f'A raiz quadrada de {num} é {math.sqrt(num)}')
# Raiz quadrada com o operador **
print(f'A raiz quadrada de {num} é {num ** 0.5}')

# Raiz quadrada de números complexos
import cmath
num2 = 1 + 2j
raiz2 = cmath.sqrt(num2)
print(f'A raiz quadrada de {num2} é {raiz2:.2f}')