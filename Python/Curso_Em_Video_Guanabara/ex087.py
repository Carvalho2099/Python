# Aprimore o desafio anterior, mostrando no final
# a soma de todos os valores pares digitados
# a soma dos valores da terceira coluna
# o maior valor digitado na segunda linha
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para {linha}, {coluna}: '))
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        if matriz[1][coluna] > maior_valor_segunda_linha:
            maior_valor_segunda_linha = matriz[1][coluna]

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
for linha in range(0, 3):
    soma_terceira_coluna += matriz[linha][2]
print(f'A soma dos valores pares: {soma_pares}')
print(f'A soma da terceira coluna: {soma_terceira_coluna}')
print(f'o maior valor digitado na segunda linha: {maior_valor_segunda_linha}')
