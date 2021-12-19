# Faça um mini-sistema que utilize o interactiv Help do Python. O usuário vai digitar o comaando e o manual
# vai aparecer quano o usuário digitar 'FIM' o programa se encerrará

def mensagem(msg):
    tam = len(msg)
    print('=' * (tam + 4))
    print(f'  {msg}')
    print('=' * tam)
    print(help(msg))
    print('=' * tam)


mensagem('SISTEMA DE AJUDA PyHELP')
while True:
    func_Lib = input('Função ou Biblioteca > ')
    if func_Lib.lower().strip() == 'fim':
        break
    mensagem(func_Lib)
mensagem('FIM')
