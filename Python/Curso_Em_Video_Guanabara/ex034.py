# Faca um programa que pergunte o salário de um funcionário e clacule o valor do seu aumento.
# Para salarios superiores a R$1.250,00, calcule um aumento de 10%
# para os inferiores ou iguaris o aumento é de 15%

salario_base = 1250
salario = float(input('Digite o seu salário: '))
if(salario > salario_base):
    print('Seu aumento é de 10%')
    print(f'Seu salário passa de R${salario} para R${(salario) + ((salario * 10)/100):.2f}')
else:
    print('Seu aumento é de 15%')
    print(f'Seu salário passa de R${salario} para R${(salario) + ((salario * 15)/100):.2f}')
