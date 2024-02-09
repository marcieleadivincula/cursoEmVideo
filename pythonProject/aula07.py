# # Operadores aritméticos: +, -, *, /, **, //, %
# adicao = 5 + 2
# print(adicao)
# subtracao = 5 - 2
# print(subtracao)
# divisao = 5 / 2
# print(divisao)
# multiplicacao = 5 * 2
# print(multiplicacao)
# potencia = 5**2
# print(potencia)
# divisaoInteira = 5//2
# print(divisaoInteira)
# divisaoResto = 5 % 2
# print(divisaoResto)
#
# # Ordem de precedência: (), **, (*, /, //, %), (+,-),
# exp1 = 5+3*2
# print(exp1)
# exp2 = 3*5+4**2
# print(exp2)
# exp3 = 3*(5+4)**2
# print(exp3)
# exp4 = 365**522
# print(exp4)
# exp5 = pow(4, 3)
# print(exp5)
#
# nome = input('Qual é seu nome? ')
# print('Prazer em te conhecer, {:20}!'.format(nome))
# print('Prazer em te conhecer, {:>20}!'.format(nome))
# print('Prazer em te conhecer, {:<20}!'.format(nome))
# print('Prazer em te conhecer, {:^20}!'.format(nome))
# print('Prazer em te conhecer, {:=^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {} e \na subtração é {}'.format(a, s))
print('A multiplicação(produto) é {} e \na divisão é {:.2f}'.format(m, d))
print('A divisão inteira é {} e a potência é {}'.format(di, e), end=' >>>')