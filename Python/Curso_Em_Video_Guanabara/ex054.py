# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores

from datetime import date

ano_atual = date.today().year
maioridade = 21
maiores = 0
menores = 0

for item in range(0, 7):
    ano_nascimento = int(input(f'Individuo {item + 1} digite seu ano de nascimento: '))
    if (ano_atual - ano_nascimento) >= maioridade:
        maiores += 1
    else:
        menores += 1

print(f'{maiores} pessoas são maiores de idade e {menores} são menores de idade.')
