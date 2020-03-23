def media():
    n1 = int(input('Digite o primeiro número:'))
    n2 = int(input('Digite o segundo número:'))
    n3 = int(input('Digite o terceiro número:'))
    n4 = int(input('Digire o quarto número:'))
    n5 = int(input('Digite o quinto número:'))
    media = (n1 + n2 + n3 + n4 + n5) / 5

    if n1 > media:
        print(f'{n1} é maior que a média {media}')
    if n2 > media:
        print(f'{n2} é maior que a média {media}')
    if n3 > media:
        print(f'{n3} é maior que a média {media}')
    if n4 > media:
        print(f'{n4} é maior que a média {media}')
    if n5 > media:
        print(f'{n5} é maior que a média {media}')
    else:
        print(f'A média é de {media}')

media()