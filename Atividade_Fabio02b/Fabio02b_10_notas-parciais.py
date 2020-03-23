def main():
    n1, n2 = map(float, input('Digite as duas notas:').split(' '))
    media = (n1 + n2) / 2
    if 9 < media <= 10:
        print(f'Notas: {n1} e {n2}')
        print(f'Média: {media}')
        print(f'Conceito corresponde a "A"')
        print ('Aprovado')
    elif 7.5 < media <= 9:
        print(f'Notas: {n1} e {n2}')
        print(f'Média: {media}')
        print(f'Conceito corresponde a "B"')
        print ('Aprovado')
    elif 6 < media <= 7.5:
        print(f'Notas: {n1} e {n2}')
        print(f'Média: {media}')
        print(f'Conceito corresponde a "C"')
        print ('Aprovado')
    elif 4 < media <= 6:
        print(f'Notas: {n1} e {n2}')
        print(f'Média: {media}')
        print(f'Conceito corresponde a "D"')
        print ('Reprovado')
    elif 0 < media <= 4:
        print(f'Notas: {n1} e {n2}')
        print(f'Média: {media}')
        print(f'Conceito corresponde a "E"')
        print ('Reprovado')

main()
