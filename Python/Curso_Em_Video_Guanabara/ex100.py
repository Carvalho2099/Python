# Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteio() e somarPar(). A primeira
# função vai sortear 5 números e vai colocá-los dentro da lista e a segunda vai mostrar a soma entre todos os
# valores pares sorteados pela função anterior
from random import randint
from time import sleep


def sorteio():
    lista = list()
    print('Sorteando 5 valores: ', end='')
    for _ in range(5):
        sleep(1)
        n = randint(0, 10)
        print(f'{n} ', end='')
        lista.append(n)
    print('PRONTO!')
    somapar(lista)


def somapar(lista):
    soma = 0
    print(f'Somando os valores pares de {lista}, ', end='')
    for item in lista:
        if item % 2 == 0:
            soma += item
    if soma > 0:
        print(f'temos {soma}')
    else:
        print('Não temos números pares nessa lista.')


sorteio()
