# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final mostre um boletim conendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente
alunos_notas = list()

while True:
    nome = input('Nome: ')
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2)/2
    alunos_notas.append([nome, [nota1, nota2], media])
    continuar = input('Quer continuar: [S/N]').strip().lower()[0]
    while continuar not in 'sn':
        print('Respota invalida, tente novamente...')
        continuar = input('Quer continuar: [S/N] ').strip().lower()[0]
    if continuar == 'n':
        break
print(f'N -   Nome -   Média')
print('-='* 15)
for index, aluno in enumerate(alunos_notas):
    print(f'{index} - {aluno[0]} - {aluno[2]}')

while True:
    aluno = int(input('Digite o número do aluno no qual quer ver as notas: (999 interrompe) '))
    if aluno == 999:
        break
    if aluno <= len(alunos_notas):
        print(f'Notas de {alunos_notas[aluno][0]} são {alunos_notas[aluno][1]}')

