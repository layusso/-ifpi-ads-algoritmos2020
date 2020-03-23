def digitos():
    numero = int(input('Insira um número inteiro de dois digitos:')) 

    dezena = numero // 10
    unidade = numero % 10

    if dezena == unidade:
        print('O algarismo da dezena é igual ao da unidade')
    else:
        print('Os algarismos são diferentes')


digitos()