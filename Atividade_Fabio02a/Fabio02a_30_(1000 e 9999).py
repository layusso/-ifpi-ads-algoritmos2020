def caracteristica():
    numero = int(input('Digite um valor inteiro entre 1000 e 9999'))
    divisão = numero // 100
    resto numero % 100
    soma = divisão + resto
    if soma**(1/2) == numero:
        print('Faz parte da característica')
    else:
        print('Não faz parte da característica')

caracteristica()