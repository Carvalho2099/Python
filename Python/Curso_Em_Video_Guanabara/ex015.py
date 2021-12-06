# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade
# de dias pelos quais fois alugado. Calcule e mostre o valor a pagar, sabendo que o carro custa R$60 por dia
# e R$0,15 por Km rodado
qtd_dias = int(input('Digite a quantidade de dias alugado: '))
km_rodado = float(input('Digite a quantidade de Km rodados: '))
valor_final = (qtd_dias * 60) + (km_rodado * 0.15)
print(f'Valor total a ser pago: {valor_final:.2f}')
