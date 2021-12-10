# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deve escolher na tela se o usuário venceu ou perdeu.

from random import randint

numero_sorteado = randint(0, 5)
print('Adivinhe o número que escolhi entre 0 e 5')
numero_chutado = int(input('Escolha seu número: '))
if numero_chutado == numero_sorteado:
    print('Você ganhou!')
else:
    print('Você perdeu!')
print(f'O numero que você escolheu foi {numero_chutado} e o número que eu escolhi foi {numero_sorteado}')
