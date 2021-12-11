# Escreva um programa que leia dois números inteiros e copare-os,
# mostrando na uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# não existe valor maior, os dois são iguais
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n1 > n2:
    print('- O primeiro valor é maior.')
elif n1 < n2:
    print('- O segundo valor é maior.')
else:
    print('- Não existe valor maior, os dois valores são iguais.')