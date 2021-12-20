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


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print('Valor inválido, digite um número inteiro.')
            continue
        except KeyboardInterrupt:
            print('Usuário preferiu não digitar esse número')
            return 0
        else:
            return valor
