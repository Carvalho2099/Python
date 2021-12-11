# Crie um programa que leia duas notas de um aluno e calcule sua média
# mostrando uma mensagem no final de acordo com a nédia atingida:
# média abaixo de 5.0: REPROVADO
# média entre 5.0 e 6.9: RECUPERAÇAO
# média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeir nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f'Sua média é : {media:.1f}')
if media < 5:
    print('\033[1;31mREPROVADO')
elif media >= 5 and media <= 6.9:
    print('\033[1;33mRECUPERAÇAO')
else:
    print('\033[1;32mAPROVADO')
