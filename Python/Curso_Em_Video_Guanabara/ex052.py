# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

num = int(input('Digite um número inteiro qualquer: '))
soma = 0
for item in range(1, num + 1):
    if num % item == 0:
        soma += 1
if soma == 2:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')
