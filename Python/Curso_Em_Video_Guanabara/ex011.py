# Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e mostre
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
print(f'A parede tem uma área de {area:.2f}m²')
print(f'São necessária {area/2:.2f} latas de tinta')