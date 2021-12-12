# Refaça o desafio 051, lendo o peimeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da
# progressão usando a estrutura while
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 1
while cont != 11:
    print(f'{primeiro}', end=' ')
    primeiro += razao
    cont += 1
