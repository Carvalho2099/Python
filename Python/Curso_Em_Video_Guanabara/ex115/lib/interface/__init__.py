def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('Valor inválido, digite um número inteiro.')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número')
            return 0
        else:
            return valor


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.upper().center(42))
    print(linha())


def menu(lista):
    cabecalho('menu principal')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c+=1
    print(linha())
    resposta = leiaInt('Sua Opção: ')
    return resposta