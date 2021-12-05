# Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informacoes possiveis sobre ele.
algo = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(algo))
print('Só tem espacos?', algo.isspace())
print('É um número', algo.isnumeric())
print('É alfabético', algo.isalpha())
print('É alfanumérico', algo.isalnum())
print('Esta em mai;usculas?', algo.isupper())
print('Esta em minusculas?', algo.islower())
print('Esta capitalizada?', algo.istitle())
