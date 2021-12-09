# Faca um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos seprados.
num = input('Digite um número: ')

print(f'unidade: {num[0]}' if len(num) > 0 else '')
print(f'dezena: {num[1]}' if len(num) > 1 else '')
print(f'centena: {num[2]}' if len(num) > 2 else '')
print(f'milhar: {num[3]}' if len(num) > 3 else '')
