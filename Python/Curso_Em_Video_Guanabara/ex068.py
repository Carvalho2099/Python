# Faça um programa que jogue par ou impar com o comptuador.O Jogo será interrompido quano o jogador perder,
# mostrando o tatal de vitórias consecutivas que ele conquistou no final do jogo
from random import randint
print('Partida de PAR ou IMPAR')
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um valor: '))
    while par_impar not in 'pi':
        par_impar = input('Escolha Par ou Impar [P/I]: ').strip().lower()[0]
    if (jogador + computador) % 2 == 0:
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {jogador + computador } DEU PAR')
        if par_impar == 'p':
            print('Você venceu!')
            print('Vamos Jogar novamente...')
        else:
            print('Você perdeu!')
            print('Fim de Jogo!')
            break
    else:
        print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {jogador + computador} DEU IMPAR')
        if par_impar == 'i':
            print('Você venceu!')
            print('Vamos Jogar novamente...')
        else:
            print('Você perdeu!')
            print('Fim de Jogo!')
            break
