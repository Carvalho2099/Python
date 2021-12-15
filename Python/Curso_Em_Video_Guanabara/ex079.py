# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista,
# caso o número já exista na lista ele não sera add, no final serão exibidos todos os valores únicos digitados em ordem
# crescente
lista = list()
while True:
    n =int(input('Digite um número inteiro qualquer: '))
    if n in lista:
        print(f'O número {n} já existe na lista então não será add.')
    else:
        lista.append(n)
        print('Valor add.')
    continuar = input('Deseja incluir mais um número: [S/N] ').strip()[0].upper()
    while continuar not in 'SN':
        print('Tente novamente...')
        continuar = input('Deseja incluir mais um número: [S/N] ').strip()[0].upper()
    if continuar == 'N':
        break
print('Os valores digitados foram:')
print(sorted(lista))
