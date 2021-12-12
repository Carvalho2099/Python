# Melhore o desafio 61, perguntando para o usuário se ele quer mostras mais alguns termos. O prorama encerra
# que ele disser que quer mostrar 0 termos
primeiro = int(input('Peimeiro termo: '))
razao = int(input('Razão: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print(f'Progressão finalizada com {total} tesmos mostrados.')