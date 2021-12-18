# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
# em um dicionário No final coloque esse dicionário em ordem sabendo que o vencedor tirou o maior número no dado

from random import randint
from operator import itemgetter
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6),
}
ranking = dict()
print('Valores sorteados:')
for chave, valor in jogo.items():
    print(f'{chave} tirou {valor} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)