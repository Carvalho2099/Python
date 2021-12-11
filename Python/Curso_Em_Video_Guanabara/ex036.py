# Escreva um programa para aprovar um empréstimo bancário para a compra
# de uma casa. O programa vai perguntar o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder
# 30% do salário ou então o empréstimo será negado

valor_casa = float(input('Digite o valor da casa: '))
valor_salario = float(input('Digite quanto é o seu salário: '))
pagamento_anos = float(input('Em quantos anos vai pagar a casa: '))
porcentagem_salario = (valor_salario * 30) / 100
valor_parcela = valor_casa / (pagamento_anos * 12)
if(porcentagem_salario < valor_parcela):
    print(f'O valor da parcela será de R${valor_parcela:.2f}')
    print('Esse valor ultrapassa 30% do seu salário')
    print('\033[1;31mEMPRESTIMO NEGADO')
else:
    print(f'O valor da parcela será de R${valor_parcela:.2f}')
    print('Esse valor não ultrapassa 30% do seu salário')
    print('\033[1;32mEMPRESTIMO APROVADO')