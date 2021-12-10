# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem cobrando
# R$0,50 por km para viagens até 200km e R$0,45 para viagens mais longas.
distancia = float(input('Digite a distancia da sua viagem em km: '))
distancia_maxima = 200
if(distancia <= distancia_maxima):
    valor_passagem = distancia * 0.50
else:
    valor_passagem = distancia * 0.45
print(f'Sua passagem vai ser de R${valor_passagem:.2f}')
