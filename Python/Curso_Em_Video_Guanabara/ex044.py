# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista cartão: 5% de desconto
# em até duas vezes no cartão: preço normal
# 3X ou mais no cartão 20% de juros

valor_produto = float(input('Digite o valor do produto: '))
print('CONDIÇÃO DE PAGAMENTO:')
print('1 - À VISTA')
print('2 - PARCELADO')
condicao_pagamento = int(input('Escolha uma das condições de pagamento acima: '))
if condicao_pagamento == 1:
    print('CONDIÇÃO DE PAGAMENTO À VISTA')
    print('FORMAS DE PAGAMENTO:')
    print('1 - DINHEIRO/CHEQUE')
    print('2 - CARTÃO')
    forma_pagamento = int(input('Escolha uma das formas de pagamento acima: '))
    if forma_pagamento == 1:
        print('FORMA PAGAMENTO ESCOLHIDA FOI DINHEIRO/CHEQUE')
        print('Você obteve 10% de desconto')
        print(f'O preço final do produto passou a ser: {valor_produto - (valor_produto * 10)/100:.2f}')
    elif forma_pagamento == 2:
        print('FORMA PAGAMENTO ESCOLHIDA FOI CARTÃO')
        print('Você obteve 5% de desconto')
        print(f'O preço final do produto passou a ser: {valor_produto - (valor_produto * 5) / 100:.2f}')
elif condicao_pagamento == 2:
    print('CONDIÇÃO DE PAGAMENTO PARCELADO')
    parcelas = int(input('DIGITE A QUANTIDADE DE PARCELAS: '))
    if parcelas <= 2:
        print(f'Voce escolheu {parcelas} parcelas.')
        print('Não existe desconto nessa forma de pagamento.')
        print(f'O valor final do produto continua sendo {valor_produto:.2f}')
    elif parcelas >= 3:
        print(f'Voce escolheu {parcelas} parcelas.')
        print('Nessa forma tem o acrescimo de 20% de juros')
        print(f'O valor final do produto continua sendo {valor_produto + (valor_produto * 20) / 100:.2f}')

