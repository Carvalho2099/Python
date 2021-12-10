# Faca um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente
nome_completo = input('Digite seu nome completo: ').strip()
print(f'Nome digitado: {nome_completo}')
print(f'Primeiro nome: {nome_completo.split()[0]}')
print(f'Último nome: {nome_completo.split()[-1]}')
print(f'Último nome: {nome_completo.split()[len(nome_completo.split()) -1]}')
