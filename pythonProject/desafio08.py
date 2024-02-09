# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
metros = float(input('Uma distância em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
print(f'A medida de {metros:.2f}m corresponde à {centimetros:.2f}cm e {milimetros:.2f}mm')