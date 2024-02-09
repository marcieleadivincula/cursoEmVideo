# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('A média entre [{:.2f} e {:.2f}] é igual à {:.2f}'.format(n1, n2, media))
print('A média entre [{:.1f} e {:.1f}] é igual à {:.1f}'.format(n1, n2, media))