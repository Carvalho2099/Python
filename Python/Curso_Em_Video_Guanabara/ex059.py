# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operaçao solicitada em cada caso.

saida = 1
resultado = 0
n1 = float(input('Digite um número qualquer: '))
n2 = float(input('Digite outro número qualquer: '))
while saida != 5:
    print('MENU')
    print("""
[1] somar 
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
    """)
    saida = int(input('Escolha uma das opções acima: '))
    if saida == 1:
        print(f'{n1} + {n2} = {n1 + n2:.1f}')
    elif saida == 2:
        print(f'{n1} x {n2} = {n1 * n2:.1f}')
    elif saida == 3:
        if n1 > n2:
            print(f'O maior número digitado foi {n1}')
        else:
            print(f'O maior número digitado foi {n2}')
    elif saida == 4:
        n1 = float(input('Digite um número qualquer: '))
        n2 = float(input('Digite outro número qualquer: '))
        print('MENU')
        print(""""
            [1] somar 
            [2] multiplicar
            [3] maior
            [4] novos números
            [5] sair do programa
        """)
        saida = int(input('Escolha uma das opções acima: '))

print('Programa finalizado!')
