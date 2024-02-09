# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Digite o seu salário: '))
# salario += (salario * 15 / 100)
aumentoSalarial = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento,\n passa a receber R${:.2f}'.format(salario, aumentoSalarial))