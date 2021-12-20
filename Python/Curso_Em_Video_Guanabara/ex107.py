# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade()
# Faça também um programa que importe esse módulo e use algumas dessas funções.
import moeda
valor = float(input('Digite o preço: R$'))
print(f'A metade de {valor} é {moeda.metade(valor):.1f}')
print(f'O dobro de {valor} é {moeda.dobro(valor):.1f}')
print(f'Aumentando 10%, temos {moeda.aumentar(valor, 10):.1f}')
print(f'Reduzindo 13%, temos {moeda.diminuir(valor, 13):.1f}')
