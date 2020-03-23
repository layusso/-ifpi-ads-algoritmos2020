def main():
    turno = input('Digite a letra correspondente ao turno que você estuda(M, V, N):')

    if turno == 'M':
        print('Bom dia!')
    elif turno == 'V':
        print('Boa tarde!')
    elif turno == 'N':
        print('Boa Noite!')
    else:
        print('Turno inválido')



main()