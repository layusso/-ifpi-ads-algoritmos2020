def lados():
    lado_1 = float(input('Insira o valor do primeiro lado:'))
    lado_2 = float(input('Insira o valor do segundo lado:'))
    lado_3 = float(input('Insira o valor do terceiro lado:'))
    
    if lado_1 == 0 or lado_2 == 0 or lado_3 == 0:
        print('Não existe lado de tamanho 0')
    elif lado_1 + lado_2 < lado_3 or lado_2 + lado_3 < lado_1 or lado_3 + lado_1 < lado_2:
        print('Não forma um triângulo.')
    elif lado_1 == lado_2 == lado_3:
        print('Forma um triângulo equilátero')
    elif lado_1 == lado_2 != lado_3 or lado_2 == lado_3 != lado_1 or lado_3 == lado_2 != lado_1:
        print('Forma um triângulo isoceles.')
    elif lado_1 != lado_2 != lado_3:
        print('Forma triângulo escaleno.')

lados()
