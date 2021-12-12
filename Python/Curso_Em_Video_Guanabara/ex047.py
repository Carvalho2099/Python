# Crie um programa que mostre na tela todos os números pares que estão no intervalo de 1 e 50.

for item in range(1, 51):
    if item % 2 == 0:
        print(item, end=' ')
print()
for item in range(2, 51, 2):
    print(item, end=' ')
