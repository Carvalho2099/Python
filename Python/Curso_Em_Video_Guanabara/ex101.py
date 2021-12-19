# Crie um programa que tenha uma funcáão chamado voto() que vai receber como parametro o ano de nascimento de
# uma pessoa, retornando um valor literal indicando se uma pessoa tem o voto NEGADO, OPCIONAL ou OBRIGATÓRIO
# nas eleições

def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f'Você tem {idade} e seu voto é NEGADO'
    elif idade < 18 or idade > 60:
        return f'Você tem {idade} e seu voto é OPCIONAL'
    else:
        return f'Você tem {idade} e seu voto é OBROGATÓRIO'


nascimento = int(input('Digite o ano de seu nascimento: '))
print(voto(nascimento))
