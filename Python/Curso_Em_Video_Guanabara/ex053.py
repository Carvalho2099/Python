# Criem um programa que leia uma frase qualquer e diga se ala é um palidromo, desconsiderando os espaços

frase = input('Digite uma frase qualquer: ')
frase_invertida = frase.replace(" ", "")[::-1]
if frase_invertida == frase.replace(" ", ""):
    print("A frase digitada é um palidromo.")
else:
    print("A frase digitada não é um palidromo.")
