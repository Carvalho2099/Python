# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário,
# no final mostre o conteúdo da estrutura na tela
aluno = dict()
aluno['nome'] = input('Digite o nome do aluno: ')
aluno['média'] = float(input('Digite a média do aluno: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'
elif aluno['média'] >= 5:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
print(f'O aluno : {aluno["nome"]}, está com a média {aluno["média"]}, e sua situação é {aluno["situação"].upper()}.')
