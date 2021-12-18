# Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionarios em uma lista. No final mostre:
# quantas pessoas foram cadastradas
# A média de idade do grupo
# Uma lista com todas as mulheres
# Uma lista com todas as pessoas com idade acima da média
pessoas = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').lower()[0]
        if pessoa['sexo'] in 'mf':
            break
        print('Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    while True:
        continuar = input('Quer continuar? [S/N] ').strip().lower()[0]
        if continuar in 'sn':
            break
        print('Responda apenas S ou N.')
    if continuar == 'n':
        break
print(f'{len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'A média de idade é: {media:.2f} anos')
print('As mulherres cadastradas foram ', end='')
for item in pessoas:
    if item['sexo'] in 'Ff':
        print(f'{item["nome"]} ', end='')
print()
print('A lista de pessoas acima da média de idade')
for item in pessoas:
    if item['idade'] >= media:
        for chave, valor in item.items():
            print(f'{chave} = {valor}; ', end='')
        print()