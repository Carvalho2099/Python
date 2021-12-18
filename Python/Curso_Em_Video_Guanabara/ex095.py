# aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um seitema de visualização de detalhes
# do aproveitamento de cada jogador

grupo = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do Jogador: ')
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogo? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append((int(input(f'Quantos gols na partida {c + 1}? '))))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    grupo.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
        print('Escolha apenas S ou N.')
    if resp == 'N':
        break

for index, item in enumerate(grupo):
    print(f'{index:>3} ', end='')
    for d in item.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para sair) '))
    if busca == 999:
        break
    if busca >= len(grupo):
        print('Não existe jogador para o valor digitado')
    else:
        print(f'Levantamento do jogador {grupo[busca]["nome"]}:')
        for index, item in enumerate(grupo[busca]['gols']):
            print(f'No jogo {index + 1} fez {item} gols')
