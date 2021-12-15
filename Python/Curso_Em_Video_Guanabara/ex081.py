# Crie um programa que vai ler vários números e coloca-los em uma lista. depois disso mostre.
# Quantos números foram digitados
# A lista em orderm decrescente
# se o valor 5 foi digitado e está ou não na lista
lista = list()
while True:
    lista.append(int(input('Digite um número inteiro qualquer: ')))
    continuar = input('Deseja incluir mais um número: [S/N] ').strip()[0].upper()
    while continuar not in 'SN':
        print('Tente novamente...')
        continuar = input('Deseja incluir mais um número: [S/N] ').strip()[0].upper()
    if continuar == 'N':
        break
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista em ordem decresente fica: {lista}')
if 5 in lista:
    print('O número 5 foi digitado na lista.')
else:
    print('O número 5 não foi digitado na lista.')
