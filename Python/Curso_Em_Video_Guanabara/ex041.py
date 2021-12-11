# A confederação nacional de natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria de acordo com a idade:
# até 9 anos : MIRIM
# até 14 anos: INFANTIL
# até 19 anos : JUNIO
# até 20 anos : SÊNIOR
# acima: MASTER

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_nascimento
print(f'O atleta tem {idade} anos.')
print('Sua categoria é:')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SÊNIOR')
else:
    print('MASTER')