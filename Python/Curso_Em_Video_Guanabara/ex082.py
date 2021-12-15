# Crie um programa que leia vários números e colocar em uma lista.
# Depois disso crie duas listas extras que vão conter apenas os valores pares e impares digitados, respectivamente
# No final mostre o conteúdo das três listas digitadas.
pares = list()
impares = list()
lista = list()

while True:
    lista.append(int(input('Digite um número inteiro qualquer: ')))
    continuar = input('Deseja incluir mais um número: [S/N] ').strip()[0].upper()
    while continuar not in 'SN':
        print('Tente novamente...')
        continuar = input('Deseja incluir mais um número: [S/N] ').strip()[0].upper()
    if continuar == 'N':
        break

for item in lista:
    if item != 0:
        if item % 2 == 0:
            pares.append(item)
        else:
            impares.append(item)

print(f'Lista digitada: {lista}')
print(f'Lista de pares: {pares}')
print(f'Lista de impares: {impares}')
