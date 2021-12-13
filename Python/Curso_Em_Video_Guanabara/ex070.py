# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o suário vai continuar.
# No final mostre:
# Qual é o total gasto de compra
# Quantos produtos custam mais de R$1000
# Qual é o nome do produto mais barato

total = caro = valor_barato = 0
produto_barato = ''


while True:
    produto = input('Digite o nome do produto: ')
    valor = float(input('Digite o valor do produto: '))
    if total == 0:
        produto_barato = produto
        valor_barato = valor
    elif valor_barato > valor:
        produto_barato = produto
        valor_barato = valor
    total += valor
    if valor > 1000:
        caro += 1
    while continuar not in 'sn':
        continuar = input('Gostaria de fazer uma nova compra: [S/N] ').strip().lower()[0]
    if continuar in 'Nn':
        break
print('Compra finalizada!')
print(f'Total da compra: {total:.2f}')
print(f'{caro} Produtos custam mais de R$1000.')
print(f'O produto mais barato é a {produto_barato} custando R${valor_barato:.2f}.')

