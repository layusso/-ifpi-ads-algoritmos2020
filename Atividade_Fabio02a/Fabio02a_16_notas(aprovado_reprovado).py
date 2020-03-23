def nota():
    nota_1 = float(input('Insira a primeira nota:'))
    nota_2 = float(input('Insira a segunda nota:'))
    media = (nota_1 + nota_2) / 2

    if media >= 7.0:
        print('Aprovado!')
    elif media < 7.0:
        nota_final = float(input('Insira a nota do exame final:'))
        media_final = (media + nota_final) / 2
        if media_final >= 5.0:
            print('Aprovado!')
        else:
            print('Reprovado!') 


nota()
