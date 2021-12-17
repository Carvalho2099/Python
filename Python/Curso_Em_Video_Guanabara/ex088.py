# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 números entre 1 e 60 para cara jogo cadastrando tudo em ma lista composta

from random import randint
lista = list()
jogos = list()
total = 1
qtd = int(input('Quantos jogos quer criar: '))
while total <= qtd:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogos:
            lista.append(num)
            cont += 1
            if cont >= 6:
                break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for index, jogo in enumerate(jogos):
    print(f'Jogo {index + 1}: {jogo}')
