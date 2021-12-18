# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida. no final,
# tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato
informacoes = dict()
gols = list()
nome = input('Nome do jogador: ')
partidas = int(input(f'Quantas partidas {nome} jogou: '))
for index in range(0, partidas):
    gol = int(input(f'Gols feitos na partida {index}: '))
    gols.append(gol)
informacoes['nome'] = nome
informacoes['gols'] = gols
informacoes['total'] = sum(informacoes["gols"])
print(informacoes)
for chave, valor in informacoes.items():
    print(f'O campo {chave}, tem o valor {valor}')
print(f'O jogador {informacoes["nome"]} jogou {partidas} partidas.')
for index, gol in enumerate(informacoes["gols"]):
    print(f'=> Na partida {index}, fez {gol} gols.')
print(f'Foi um total de {informacoes["total"]}')
