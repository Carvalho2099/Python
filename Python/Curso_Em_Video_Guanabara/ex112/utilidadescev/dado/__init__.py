def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'{entrada} não é um valor numérico válido, digite um valor numérico!')
        else:
            valido = True
            return float(entrada)
