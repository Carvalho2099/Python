# Faça um programa que tenha uma função chamada escreva(), que recebe um texto como parametro e mostre uma mensagem
# com o tamanho adaptável

def escreva(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))

escreva('Curso em Video')
escreva('Python')
escreva('CEV')
