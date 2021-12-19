#Faça um programa que tenha uma função chamada area(), que recebe as dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno

def area(largura, comprimento):
    area = largura * comprimento
    print(f'A area do terreno com as informações digitadas é de : {area:.1f}m²')


largura = float(input('Digite a largura do terreno em metros: '))
comprimento = float(input('Digite co comprimento do terreno em metros: '))
area(largura, comprimento)