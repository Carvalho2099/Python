# Crie um programa que vai gerar cinco números aleatórios e colocar um uma tupla.
# Depois disso mostre a listagem dos números gerados e também indique o menor e o maior valor que estão na tupla
from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Valores da tupla: {tupla}')
print(f'O maior valor da tupla é: {max(tupla)}')
print(f'O menor valor da tupla é: {min(tupla)}')
