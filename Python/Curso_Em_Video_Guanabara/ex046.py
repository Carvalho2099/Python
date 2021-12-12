#Faça um prgama que mostre na tela uma contagem regressiva para o estou ro de fogos de artificio, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles

from time import sleep

for item in range(10, -1, -1):
    print(item)
    sleep(1)
print('KABUM!!!!!!')
