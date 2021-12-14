# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em um tupla. No final mostre:
# Quantas vezes apareceu o valor 9
# Em que posição foi digitado o primeiro valor 3
# quais foram os números pares
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))
tupla = (n1, n2, n3, n4)
cont = 0
print(f'O número 9 apareceu {tupla.count(9)} vezes.')
print(f'O número 3 ', end='')
print(f'apareceu pela primeira vez na posição {tupla.index(3) + 1}.' if tupla.count(3) > 0 else 'não aparece nessa tupla.')

for num in tupla:
    if num % 2 == 0:
        cont += 1
        if cont == 1:
            print('Numeros pares digitados: ', end='')
        print(f'{num} ', end='')
if cont == 0:
    print('Não foi digitado nenhum número par.')
