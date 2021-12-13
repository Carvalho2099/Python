# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.
while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    print('-'*15)
    if n < 0:
        break
    for item in range(1, 11):
        print(f'{n} x {item} = {n * item}')
    print('-'*15)
print('Programa Finalizado!')
