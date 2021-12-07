# Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
# retangulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
print(f'Sua hipotenusa é: {hypot(co, ca):.2f}')
