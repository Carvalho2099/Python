# Desenviolva um programa que leia seis números inteiros e mostre a soma apenas daquele que forem pares.
# se o valor digitado for impar desconsidere-o

soma_pares = 0

for item in range(0, 6):
    num = int(input('Digite um número inteiro qualquer: '))
    if num % 2 == 0:
        soma_pares += num

print(soma_pares)
