# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista unica
# que mantenha separados os valores de pares e impares. no final mostre os valores de pares e impares
# em ordem crescente
numeros = [[],[]]
for num in range(0, 7):
    n = int(input('Digite um valor inteiro: '))
    if n % 2 == 0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
numeros.sort()
print(numeros)
