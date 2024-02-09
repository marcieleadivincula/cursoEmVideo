# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2 m².
import math

b = float(input('Largura da parede em metros: '))
h = float(input('Altura da parede em metros: '))
# Área
area = b * h
# Perímetro
perimetro = 2 * (b + h)
# Diagonal d² = h² + b²
d = (h ** 2) + (b ** 2)
diagonal = math.pow(d, (1/2))
# Tinta
tinta = area / 2
print('A área da parede é {:.2f} m²'.format(area))
print(f'São necessários {tinta:.2f} l de tinta para pintar a parede.')
print('O perímetro da parede é {:.2f} m²'.format(perimetro))
print('A diagonal da parede é {:.2f} m²'.format(diagonal))