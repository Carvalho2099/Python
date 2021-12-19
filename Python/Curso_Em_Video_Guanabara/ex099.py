# Faça um programa que tenha uma função chamada maior(). que receba vários parametros com valores  inteiros.
# Seu programa tem que analisar todos os valores e dizer qual é o maior deles.
from random import randint
from time import sleep

def maior(* numeros):
    cont = maior = 0
    print('-'*40)
    print('Analisando os valores passados...')
    for num in numeros:
        print(f'{num} ', end='')
        sleep(1)
        if cont == 0:
            maior = num
        else:
            if num > maior:
                maior = num
        cont += 1
    print(f'Foram informado {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior},')
    print('-'*40)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior()

