# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for
n = int(input('Digite um número inteiro: '))
for num in range(0, 11):
    print(f'{n} X {num} = {num * n}')