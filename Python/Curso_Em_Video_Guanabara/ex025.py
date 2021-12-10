# Crie um programa que leia o nome de uma pesoa e diga se ela tem "Silva" no nome
nome = input('Digite um nome completo: ').strip()
sim_nao = 'Sim' if ('silva' in nome.lower()) else 'Não'
print(f'O nome contém SILVA: {sim_nao}')
