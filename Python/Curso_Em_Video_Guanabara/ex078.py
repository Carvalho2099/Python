# Faça um prograa que leia 5 valores numéricos e guarde-os em uma lista.
# No final mostre qual foi o maior e menor valor digitado e suas respectivas posções na lista
lista = list()
for _ in range(0, 5):
    lista.append(float(input(f'digite o número da posição {_}: ')))
print(f'O maior valor digitado foi {max(lista)} e está na posição {lista.index(max(lista))}...', end=' ')
if lista.count(max(lista)) > 1:
    for index, item in enumerate(lista):
        if item == max(lista) and index != lista.index(max(lista)):
            print(f'{index}...', end=' ')
print(f'\nO menor valor digitado foi {min(lista)} e está na posição {lista.index(min(lista))}...', end=' ')
if lista.count(min(lista)) > 1:
    for index, item in enumerate(lista):
        if item == min(lista) and index != lista.index(min(lista)):
            print(f'{index}...', end=' ')
print(f'\n{lista}')
