# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar, mostrando no final quandos palpites foram necessários para vencer

from random import randint

numero_sorteado = randint(0, 10)
cont = 1

print('Adivinhe o número que escolhi entre 0 e 5')
numero_chutado = int(input('Escolha seu número: '))

while numero_chutado != numero_sorteado:
    print('Errou!')
    print('Tente novammente.')
    numero_chutado = int(input('Escolha seu número: '))
    cont += 1
print('Acertou!')
print(f'Foram necessárias {cont} tentativas.')
