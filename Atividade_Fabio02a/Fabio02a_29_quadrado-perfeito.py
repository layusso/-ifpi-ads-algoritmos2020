def quadradoperfect():
    numero = int(input('Digite um número inteiro de 4 dígitos:'))
    raiz = numero**(1/2)
    divisão = numero // 100
    resto = numero % 100
    soma = divisão + resto
    if raiz == soma:
        print('Esse número é um quadrado perfeito')
    else:
        print('Esse número não é um quadrado perfeito')

quadradoperfect()