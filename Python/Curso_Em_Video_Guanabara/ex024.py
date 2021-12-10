# Crie um programa que leia o nome de uma cidade e difa se ela comeca ou não com o nome "SANTO".
cidade = input('Digite o nome de uma cidade: ').strip()
sim_nao = 'sim' if cidade.lower().split()[0] == 'santo' else 'não'
print(f'A cidade {sim_nao} contem santo no comeco do nome.')
