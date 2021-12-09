# Crie um programa que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras maiúsculas
# O nome com todas as letrar minúsculas
# Quantas letras ao todo (sem contar os espacos)
# Quantas letras tem o primeiro nome

nome_completo = input('Digite o seu nome completo: ')
print(f'{nome_completo.upper()}')
print(f'{nome_completo.lower()}')
print(f'Seu Nome tem {len(nome_completo.replace(" ", ""))} letras.')
print(f'Seu primeiro nome tem {len(nome_completo.split()[0])} letras.')