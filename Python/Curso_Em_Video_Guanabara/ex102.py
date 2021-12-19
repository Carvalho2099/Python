# Crie um programa que tenha um função fatorial() que receba dois parametros: o primeiro que indique o numero a
# calcular e o soutro chamado show que será um valor lógico (opcional) indicando se será mostrado ou não na tela
# o processo de cáculo fatorial


def fatorial(valor, show=False):
    """
    -> calcula o fatorial de um número
    :param valor: O número a ser calculado
    :param show:(opcional) Mostrar ou não a conta
    :return: o valor do fatorial
    """
    from math import factorial
    f = 1
    for num in range(valor, 0, -1):
        if show:
            print(num, end='')
            if num > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= num
    return f


print(fatorial(5))