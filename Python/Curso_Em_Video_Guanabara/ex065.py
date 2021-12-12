# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos eles
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer continuar ou
# não a digitar valores.

maior = menor = cont = soma = 0
continuar = 's'
while continuar in 'sS':
    n = int(input('Digite um valor inteiro qualquer: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    continuar = input('Deseja continuar: [S/N] ').strip()
print('Programa finalizado.')
print(f'A média entre os valores digitados foi: {soma/cont}')
print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')