# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faca um programa
# que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
from random import randint
nomes = ['Lisa', 'Felipe', 'Thiago', 'André']
n = randint(0, 3)
print(f'O aluno que irá apagar o quadro é {nomes[n]}')
