# Crie um programa onde o usuário digite uma expressão qualquer que use parenteses. Seu aplicativo devera analisar
# se a expressão passada esta com o parenteses abertos e fechados na ordem correta.
expressao = input('Digite a sua expressão: ')
if expressao.count('(') > 0 or expressao.count(')') > 0:
    if expressao.count('(') == expressao.count(')'):
        print('E expressão digitada está correta.')
    else:
        print('A expressão digitada esta incorreta.')
else:
    print('A expressão não contém parenteses.')
