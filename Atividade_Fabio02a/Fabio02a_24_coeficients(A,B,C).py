def raizes():
    a = float(input('Digite o valor de a:'))
    b = float(input('Digite o vaor de b:'))
    c = float(input('Digitie o valor de c:'))
    delta = b**2 - 4*a*c
    x1 = ((-b) + delta**(1/2)) / (2*a)
    x2 = ((-b) - delta**(1/2)) / (2*a)
    if a == 0 :
        print('O valor de a precisa ser diferente de 0!')
    elif delta < 0:
        print('Delta negativo, não existe raízes reais')
    else:
        print(f'As raízes são {x1} e {x2}')


raizes()
