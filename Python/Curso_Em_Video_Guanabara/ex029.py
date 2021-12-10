# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre um mensagem dizendo que ele foi multado
# A multa vai custar R$7.00 por cada km acima do limite

km_atual = float(input('Digite a kilometragem que passou no radar: '))
km_limite = 80

if km_atual <= km_limite:
    print('Sua velocidade está dentro da velocidade máxima permitida.')
    print('Continue assim, boa viagem!')
else:
    print('Você ultrapassou a velocidade máxima permitida e será multado!')
    print(f'Sua multa é de: R${(km_atual - km_limite) * 7:.2f}')
    print('Dirija com mais cuidado!!!')