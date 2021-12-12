# Faça um programa que leia um número inteiro qualquer e mostre o seu fatorial
fatorial = n1 = n2 = int(input('Digite um número inteiro qualquer: '))
msg = ''
while n1 != 1:
    msg += str(n1) + "x"
    n1 -= 1
    fatorial *= n1
msg += "1="
print(f'{n2}!={msg}{fatorial}')
