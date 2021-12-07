# Faca um programa que lea um angulo qualquer e mostre o valor do seno cosseno e tangente desse angulo
from math import cos,tan, sin, radians
a = float(input('Digite o angulo que voce deseja: '))
print(f'O seu seno é: {sin(radians(a)):.2f}')
print(f'O seu cosseno é: {cos(radians(a)):.2f}')
print(f'A sua tangente é: {tan(radians(a)):.2f}')
