# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule e mostre o seu status de acordo com a tebela abaixo:
# abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# acima de 40: obesidade mórbida
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >=25 and imc < 30:
    print('Sobrepeso.')
elif imc >=30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')