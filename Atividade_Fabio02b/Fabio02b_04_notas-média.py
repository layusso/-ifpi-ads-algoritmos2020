def main():
    nota = input('Digite as duas notas:').split(' ')
    media = (float(nota[0]) + float(nota[1])) / 2
    if media < 7:
        print('Reprovado')
    elif media == 10:
        print('Aprovado com Distinção')
    elif media >= 7:
        print('Aprovado')


main()
