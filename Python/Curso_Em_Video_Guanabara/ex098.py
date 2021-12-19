# Faça um programa que tenha uma função chamada contador(), que receba 3 parametros: inicio, fim e passo e realize a
# contagem. Seuprograma tem que realizar três contagens através da função criada:
# de 1 até 10, de 1 em 1
# de 10 até 0, de 2 em 2
# uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio > fim:
        passo *= -1
    print('-' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    fim += 1
    for cont in range(inicio, fim, passo):
        print(f'{cont} ', end='')
        sleep(0.3)
    print('FIM!')
    print('-' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez de personalizar a contagem')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Fim: '))
contador(inicio, fim, passo)
