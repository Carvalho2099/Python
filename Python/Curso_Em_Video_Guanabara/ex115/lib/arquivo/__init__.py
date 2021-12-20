from ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        arquivo = open(nome, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arquivo = open(nome, 'wt+')
        arquivo.close()
    except:
        print('Houve um erro na criação do aarquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        arquivo = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        cabecalho('pessoas cadastradas')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        arquivo.close()



def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        arquivo = open(arquivo, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')
            arquivo.close()