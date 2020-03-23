def inteiros():
    x = int(input('Digite o primeiro valor:'))
    y = int(input('Digite o segundo valor:'))
    soma = x + y

    if x % y == 1:
        print(soma + 1)

    elif x % y == 2:
        if x % 2 == 0:
            print('O primeiro valor é par')
        else:
            print('O primeiro valor é ímpar')
        if y % 2 == 0:
            print('O segundo valor é par')
        else:
            print('O segundo valor é ímpar')

    elif x % y == 3:
            print(soma * x)
    elif x % y == 4:
        if y != 0:
            print(soma / y) 
    else:
        print(x**2)
        print(y**2)

inteiros()
               
