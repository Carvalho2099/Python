# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuário que será o
# valor sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$ 10 e R$1

cedulas_50 = cedulas_20 = cedulas_10 = cedulas_1 = 0
valor = int(input('Digite o valor que será sacado: '))
if valor >= 50:
    cedulas_50 = valor // 50
    valor = valor - (50 * cedulas_50)
    print(f'Total de {cedulas_50} cédulas de R$50')
if valor >= 20:
    cedulas_20 = valor // 20
    valor = valor - (20 * cedulas_20)
    print(f'Total de {cedulas_20} cédulas de R$20')
if valor >= 10:
    cedulas_10 = valor // 10
    valor = valor - (10 * cedulas_10)
    print(f'Total de {cedulas_10} cédulas de R$10')
if valor >= 1:
    cedulas_1 = valor // 1
    valor = valor - (1 * cedulas_1)
    print(f'Total de {cedulas_1} Cédulas de R$1')
