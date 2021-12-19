# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input()
# do Python, só que fazendo a validação para aceitar apenas um valor númerico.
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Digite um número inteiro válido')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digita o número {n}.')