# Crie um programa que leia o nome de uma pesoa e diga se ela tem "Silva" no nome
nome = input('Digite um nome completo: ')
if 'silva' in nome.lower():
    sim_nao = 'sim'
else:
    sim_nao = 'não'
print(f'O nome contem SILVA: {sim_nao}')