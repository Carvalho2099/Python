# Faça um programa que tenha uma função chamada ficha(), que recebe dois parametros opcionais:
# o nome de um jogador e quantos gols ele marcaou.
# o programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente
def ficha(jogador='', gols=''):
    if len(jogador) == 0:
        jogador = '<desconhecido>'
    if len(gols) == 0 or not gols.isnumeric():
        gols = '0'
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato'


nome = input('Nomme do jogador: ')
gols = input('Número de Gols: ')
print(ficha(nome, gols))
