#Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que
# se encontram no intervalo de 1 até 500

soma = 0
soma2 = 0
for item in range(1, 501):
    if item % 2 == 1 and item % 3 == 0:
        soma += item
print(soma)

for item in range(1, 501, 2):
    if item % 3 == 0:
        soma2 += item
print(soma)