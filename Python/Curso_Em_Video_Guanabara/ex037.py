#Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# e para hexadecimal

num = int(input('Digite um número inteiro qualquer: '))
print('ESCOLHA A BASE DE CONVERSÃO:')

print('- 1 para binário')
print('- 2 para octal')
print('- 3 para hexadecimal')

base = int(input('Base escolhida: '))

if(base == 1):
    print(f'O valor {num} convertido para binário fica {bin(num)[2:]}')
elif(base == 2):
    print(f'O valor {num} convertido para octal fica {oct(num)[2:]}')
else:
    print(f'O valor {num} convertido para hexadecimal fica {hex(num)[2:]}')
