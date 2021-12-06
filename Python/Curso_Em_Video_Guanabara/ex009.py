# Faca um programa que leia um numero inteiro e mostre na tela a sua tabuada
n = int(input('Digite um número inteiro: '))
for num in range(0, 11):
    print(f'{n} X {num} = {num * n}')