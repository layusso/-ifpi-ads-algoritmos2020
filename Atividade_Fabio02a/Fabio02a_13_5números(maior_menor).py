def mair_menor():
    n1 = float(input('Insira o primeiro número:'))
    n2 = float(input('Insira o segundo número:'))
    n3 = float(input('Insira o terceiro número:'))
    n4 = float(input('Insira o quarto número:'))
    n5 = float(input('Insira o quinto número:'))

    if n1 > n2 and n1 > n3 and n1> n4 and n1 > n5:
        print(f'{n1} é o maior número')
    elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        print(f'{n2} é o maior número.')
    elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        print(f'{n3} é o maior número.')
    elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
        print(f'{n4} é o maior número.')
    elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
        print(f'{n5} é o maior número.')

    if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
        print(f'{n1} é o menor número')
    elif n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
        print(f'{n2} é o menor número.')
    elif n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
        print(f'{n3} é o menor número.')
    elif n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
        print(f'{n4} é o menor número.')
    elif n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
        print(f'{n5} é o menor número.')


mair_menor()
    

