# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade
# em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.
from ex115.lib.interface import *
from ex115.lib.arquivo import *

arquivo = 'pessoas.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arquivo)
    if resposta == 2:
        cabecalho('novo cadastro')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    if resposta == 3:
        print('Saindo dos Sistema...')
        break
    else:
        print('Opção inválida, Digite uma opção valida...')