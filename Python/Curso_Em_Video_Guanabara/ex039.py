# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade:
# - Se ele ainda vai se alistar no serviço militar
# - Se é hora dele se alistar
# - Se já passou o temo do alistamento
# seu programa também deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade_alistamento = 18
idade_atual = ano_atual - ano_nascimento

if idade_atual < idade_alistamento:
    print(f'Ainda faltam {idade_alistamento - idade_atual} anos para se alistar')
elif idade_atual == idade_alistamento:
    print('Esta na idade correta de se alistar.')
else:
    print(f'Já passou {idade_atual - idade_alistamento} anos do alistamento.')
