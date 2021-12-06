# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# considere U$$ 1.00 = R$3,27
reais = float(input('Quantos reais tem na sua carteira: '))
dolares = 3.27
print(f'Com R${reais}, voce consegue comprar U$${reais/dolares:.2f}')