# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.
num = int(input('Digite um número inteiro: '))
print('Você digitou {}, e seu antecessor é {} e o sucessor é {}'.format(num, (num-1), (num+1)))