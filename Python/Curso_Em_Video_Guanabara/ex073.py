# Crie um tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileito de Futebol, na ordem
# de dolocaçao. Depois mostre:
# Apenas os 5 primeiros colocados.
# Os ultimos 4 colocados da tabela
# uma lista com os times em ordem alfabética
# Em que posicao na tabela está o time da Chapecoense
tabela_brasileiro = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
                     'América-MG', 'Atlético-GO', 'Santos', 'Ceará-SC', 'Internacional', 'São Paulo', 'Athletico_PR',
                     'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife', 'Chapecoense')

print('Posição atual dos times em 2021: ')
for index, times in enumerate(tabela_brasileiro):
    print(f'{index + 1} - {times}')
print()
print(f'Os cinco primeiros colocados são: {tabela_brasileiro[:5]}')
print(f'Os quatro ultimos colocados da tabela são: {tabela_brasileiro[-5:]}')
print('Times em ordem alfabética: ')
for index, times in enumerate(sorted(tabela_brasileiro)):
    print(f'{index + 1} - {times}')
print(f'O time Chapecoense esta na posição: {tabela_brasileiro.index("Chapecoense")+1}')

