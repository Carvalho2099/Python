# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista, no final mostre:
# Quantas pessoas foram cadastrada.
# Uma lista com as pessoas mais pesadas
# uma lista com as pessoas mais leves

pessoa = list()
pessoas = list()
pesadas = list()
leves = list()
while True:
    pessoa.append(input('Digite um nome: '))
    pessoa.append(int(input('Digite um peso: ')))
    pessoas.append(pessoa[:])
    continuar = input('Inserir nome e peso de mais uma pessoa: [S/N] ').strip().lower()[0]
    while continuar not in 'sn':
        print('Tente novamente...')
        continuar = input('Inserir nome e peso de mais uma pessoa: [S/N] ').strip().lower()[0]
    if continuar == 'n':
        break
    if len(pessoas) < 3:
        pesadas.append(pessoa[:])
        leves.append(pessoa[:])
    else:
        if pesadas[1] == pessoa[1]:
            pesadas.append(pessoa[:])
        elif pesadas[1] < pessoa[1]:
            pesadas.clear()
            pesadas.append(pessoa[:])
        if leves[1] == pessoa[1]:
            leves.append(pessoa[:])
        elif leves[1] > pessoa[1]:
            leves.clear()
            leves.append(pessoa[:])
    pessoa.clear()

print(f'Foram cadastradas {len(pessoas)/2} pessoas.')
print(f'O maior peso foi de {pesadas[1]:.1f}kg. Peso de ', end='')
if len(pesadas) > 2:
    for pesada in range(0, len(pesadas), 2):
        print(f'{pesada}', end='')
else:
    print(f'{pesadas[0]}')
print(f'O menor peso foi de {leves[1]:.1f}kg. Peso de ', end='')
if len(leves) > 2:
    for leve in range(0, len(leves), 2):
        print(f'{leve}', end='')
else:
    print(f'{leves[0]}')
