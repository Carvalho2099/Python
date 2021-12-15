# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na
# posição correta de inserção(sem usar o sort()) no final mostre a lista ordenada na tela.

lista = list()
for item in range(0, 5):
    n = int(input('Digite um número inteiro qualquer: '))
    if item == 0 or n > lista[-1]:
        lista.append(n)
    else:
        index = 0
        while index < len(lista):
            if n <= lista[index]:
                lista.insert(index, n)
                break
            index += 1
print(lista)

