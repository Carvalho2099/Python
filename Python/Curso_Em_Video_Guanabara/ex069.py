# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos

maiores = homens = mulheres = 0
while True:
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    if idade > 19:
        maiores += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulheres += 1
    while continuar not in 'sn':
        continuar = input('Deseja continuar cadastrando: [S/N] ').strip().lower()[0]
    if continuar in 'Nn':
        break
print('Programa Finalizado!')
print('Foram cadastrado:')
print(f'{maiores} pessoas maiores de idade.')
print(f'{homens} homens')
print(f'{mulheres} mulheres com menos de 20 anos.')
