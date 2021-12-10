#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

num = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
numeros = [num, num2, num3]

menor = num
if num2 < num and num2 < num3:
    menor = num2
if num3 < num and num3 < num2:
    menor = num3

maior = num
if num2 > num and num2 > num3:
    maior = num2
if num3 > num and num3 > num2:
    maior = num3

print(f'O maior número digitado foi {max(numeros)}')
print(f'O menor número digitado foi {min(numeros)}')
