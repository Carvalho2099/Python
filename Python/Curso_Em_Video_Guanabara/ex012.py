# Faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com desconto de 5%
produto = float(input('Digite o valor do produto: '))
print(f'O valor final do produto com 5% de desconto é R${(produto - (produto* 5)/100):.2f}')
