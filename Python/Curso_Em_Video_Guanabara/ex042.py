# Refaça o desafio 035 dos triângulos, acrescentando o recurso
# de mostrar que tipo de triangulo será formado:
# Equilatero: todos os lados iguais
# Isoceles: dois lados iguais
#Escaleno todos os lados diferentes
seg1 = float(input('Digite o primeiro segmento: '))
seg2 = float(input('Digite o segundo segmento: '))
seg3 = float(input('Digite o terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos podem formar um triângulo.')
    if seg1 == seg2 and seg2 == seg3:
        print('Triangulo formado é Equilátero.')
    elif seg1 == seg2 or seg2 == seg3 or seg1 == seg3:
        print('Triangulo formado é Isóceles')
    elif seg1 != seg2 or seg2 != seg3 or seg1 != seg3:
        print('Triangulo formado é Escaleno.')
else:
    print('Os segmentos não podem formar um triângulo.')


