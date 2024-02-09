# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
num = int(input('Digite um número para ver sua tabuada: '))
print(f'A tabuada do {num} é: ')
print('-' * 16)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-' * 16)

# Minha resolução
# tabuada = 0
# print(f'A tabuada do {num} é: ')
# print('=================')
# for count in range(1, 11):
#     tabuada = num * count
#     print(f'{num} x {count} = {tabuada}')
# print('=================')