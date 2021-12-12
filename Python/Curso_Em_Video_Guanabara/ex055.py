# Faça um programa que leia o peso de 5 pessoas. no final mostre qual foi o maior pesso e o menor peso lido.

pesos = []
for item in range(0, 5):
    pesos += [float(input(f'Digite o peso da pessoa número {item + 1}: '))]
print(f'O maior peso digitado foi {max(pesos)}kg')
print(f'O menor peso digitado foi {min(pesos)}kg')
