# Crie um programa que tenha um tupla totalmente preenchida com uma contafem por extenso de zero até 20
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso

numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
                   'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Qual número de 0 a 20 quer ver por extenso: '))
    if numero < 0 or numero > 20:
        print('Número inválido, tente novamente...')
    else:
        break
print(f'O número {numero} por extenso fica: {numeros_extenso[numero]}')
