# Crie um programa que leia um número real qualquer pelo teclado e mostre sua porcao inteira
from math import trunc
num = float(input('Digite um número: '))
print(f'O número {num} tem a parte inteira {trunc(num)}.')
