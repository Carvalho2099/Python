# Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e castre-os (com idade) em um dicionario
# se por acaso a CTPS for diferente de zero, o dicionário também receberá o ano de contrtação e o salário. Calule
# e acrescente além da idade, com quantos anos a pessoa vai se aposentar.
# levando em consideração somente o tempo de contribuição sendo no total 35 anos

from datetime import date
ano_atual = date.today().year
pessoa = dict()
pessoa['nome'] = input('Nome: ')
ano_nascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = ano_atual - ano_nascimento
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    aposentadoria = ano_atual - pessoa['contratacao']
    if aposentadoria < 35:
        pessoa['aposentadoria'] = pessoa['idade'] + (35 - (ano_atual - pessoa['contratacao']))
    else:
        pessoa['aposentadoria'] = 'Já aposentado'
else:
    del pessoa['ctps']
print(pessoa)
for chave, valor in pessoa.items():
    print(f'{chave} tem o valor {valor}')
