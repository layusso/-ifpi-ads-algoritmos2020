def operacoes():
    valor_1 = float(input('Insira o primeiro valor:'))
    valor_2 = float(input('Insira o segundo valor'))
    operacao = int(input('Escolha 1 para adição, 2 subtração, 3 multiplicação ou 4 para divisão:'))

    if operacao == 1:
        print(valor_1 + valor_2)
    elif operacao == 2:
        print(valor_1 - valor_2)
    elif operacao == 3:
        print(valor_1 * valor_2)
    elif operacao == 4:
        print(valor_1 / valor_2)
    else:
        print('Escolha apenas um número de 1 a 4 para realizar uma operação!')


operacoes()
