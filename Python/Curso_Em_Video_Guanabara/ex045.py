# Crie um programa que faça o computador jogar jokênpo com você

from random import randint
computador = randint(1, 3)
print('Partida de jokenpô:')
print('1 - PEDRA')
print('2 - PAPEL')
print('3 - TESOURA')
humano = int(input('ESCOLHA UMA DAS OPÇOES ACIMA: '))
if humano == 1:
    if computador == 1:
        print('Ambos escolhemos PEDRA')
        print('EMPATE')
    elif computador == 2:
        print('Você escolheu Pedra e eu escolhi PAPEL')
        print('EU GANHEI')
    else:
        print('Você escolheu PEDRA e eu escolhi TESOURA')
        print('VOCÊ GANHOU')
elif humano == 2:
    if computador == 1:
        print('Você escolheu PAPEL eu escolhi PEDRA')
        print('VOCÊ GANHOU')
    elif computador == 2:
        print('Ambos escolhemos PAPEL')
        print('EMPATE')
    else:
        print('Você escolheu PAPEL eu escolhi TESOURA')
        print('EU GANHEI')
else:
    if computador == 1:
        print('Você escolheu TESOURA eu escolhi PAPEL')
        print('VOCÊ GANHEI')
    elif computador == 2:
        print('Você escolheu TESOURA eu escolhi PEDRA')
        print('EU GANHEI')
    else:
        print('Ambos escolhemos TESOURA')
        print('EMPATE')
