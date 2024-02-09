# Aluguel de carros
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço à pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.
diasAlugado = int(input('Quantos dias alugados? '))
kmPercorrido = float(input('Quantos Km rodados? '))
precoDiaria = diasAlugado * 60
precoKm = kmPercorrido * 0.15
total = precoKm + precoDiaria
# total = (diasAlugado * 60) + (kmPercorrido * 0.15)
print('O total a pagar é de R${:.2f}'.format(total))