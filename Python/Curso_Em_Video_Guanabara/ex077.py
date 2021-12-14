# Crie um programa que tenha um tupla com várias palavras (não usar acento) Depois disso vc deve mostrar para
# cada palavra, quais são suas vogais.
palavras = ('Estudando', 'python', 'para', 'analise', 'de', 'dados')
for palavra in palavras:
    print(f'\n Na palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end='')