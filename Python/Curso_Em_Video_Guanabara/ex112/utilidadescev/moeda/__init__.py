def aumentar(valor=0, taxa=0, show=False):
    valor_aumentar = (valor * taxa) / 100
    resp = valor + valor_aumentar
    if show:
        return moeda(resp)
    else:
        return resp


def diminuir(valor=0, taxa=0, show=False):
    valor_diminuir = (valor * taxa) / 100
    resp = valor - valor_diminuir
    if show:
        return moeda(resp)
    else:
        return resp


def metade(valor=0, show=False):
    resp = valor / 2
    if show:
        return moeda(resp)
    else:
        return resp


def dobro(valor=0, show=False):
    resp = valor * 2
    if show:
        return moeda(resp)
    else:
        return resp


def moeda(valor=0, moeda='R$'):
    return f'{moeda}{valor:>8.2f}'.replace('.', ',')


def resumo(valor, taxa_aumentar, taxa_diminuir, show=True):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado:\t{moeda(valor)}')
    print(f'Dobro do preço:\t\t{dobro(valor, show)}')
    print(f'Metade do Preço:\t{metade(valor, show)}')
    print(f'{taxa_aumentar}% de aumento:\t\t{aumentar(valor, taxa_aumentar, show)}')
    print(f'{taxa_diminuir}% de redução:\t\t{diminuir(valor, taxa_diminuir, show)}')
    print('-'*30)

