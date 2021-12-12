# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A média de idade do grupo.
# Qual o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos.

soma_idade = 0
mais_velho = 0
nome_mais_velho = ""
mullheres = 0

for item in range(0, 4):
    nome = input(f'Digite o nome da pessoa número {item + 1}: ').strip()
    idade = int(input(f'Digite a idade da pessoa número {item + 1}: '))
    sexo = input(f'Digite o sexo da pessoa número {item + 1} (M/F): ').strip()

    soma_idade += idade
    if sexo.upper() == "M" and mais_velho < idade:
        mais_velho = idade
        nome_mais_velho = nome
    if sexo.upper() == "F" and idade < 20:
        mullheres += 1

print(f'A média de idade do grupo é {soma_idade / 4:.1f}')
print(f'O nome do homem mais velho é: {nome_mais_velho}')
print(f'{mullheres} mulheres tem menos de 20 anos. ')
