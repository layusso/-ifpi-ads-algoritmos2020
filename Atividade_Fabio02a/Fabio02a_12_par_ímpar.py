def par_impar():
    numero = float(input('Insira um número'))
    
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é impar')


par_impar()