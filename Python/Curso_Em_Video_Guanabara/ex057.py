# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

sexo = input('Digite o sexo: [F/M]: ').strip()
while sexo not in 'fFmM':
    print('Opção inválida:')
    print('Tente novamente.')
    sexo = input('Digite o sexo: [F/M]: ').strip()
print('Opção váida.')
print('Finalizado.')
