# Faca um programa que leia uma frase pelo tecaldo e mostrar
# Quantas vezes aparece a letra 'A'
# Em que posicao ela aparece pela primeira vez
# Em que posicao ela aparece pela ultima vez
frase = input('Digite uma frase qualquer: ').strip()
print(f'A letra "A" aparece {frase.lower().count("a")} vezes.')
print(f'A letra a aparece pela preira vez na posicao {frase.lower().find("a") + 1}')
print(f'A letra a aparece pela preira vez na posicao {frase.lower().rfind("a") + 1}')