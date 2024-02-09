# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00=R$3,27.
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolarAntigo = real / 3.27
dolarAtual = real / 4.99
print(f'Antes, você poderia comprar US${dolarAntigo:.2f} dólares')
print(f'Hoje você pode comprar US${dolarAtual:.2f} dólares')