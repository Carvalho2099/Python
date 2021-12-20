#Dentro do pacote UtilidadeCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
# leiaDinheiro() que seja capaz de funcionar como a func'~ao input(), mas com uma validação de dados para aceitar
# apenas valores que sejam monetários
from ex111.utilidadescev import moeda

valor = float(input('Digite o preço: '))
moeda.resumo(valor, 35, 22)
