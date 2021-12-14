# Crie um programa que tenha um tupla única com nomes de produtos e seus respectivos preços na sequencia
# No final mostre uma listagem de preços  organizando os dados de forma tabular.
produtos_valores = ('Notebook', 3500, 'Mouse', 50, 'Monitor', 1100, 'Teclado', 219)

for item in range(0, len(produtos_valores)):
    if item % 2 ==  0:
        print(f'{produtos_valores[item]:.<30}', end='')
    else:
        print(f'R${produtos_valores[item]:>7.2f}')

    