def main():
    n = int(input("Digite o número de cadastros que deseja realizar"))
    maior = 0
    maior_inscrito = 0
    menor_inscrito = 0
    menor = 300000000

    cont = 0

    while cont < n:
        nome = input('Informe o nome: ')
        inscricao = int(input("Digite o número de inscrição; "))
        peso = float(input("Informe o peso: "))

        if peso > maior:
            maior = peso
            maior_inscrito = inscricao
        
        if peso < menor:
            menor = peso
            menor_inscrito = inscricao
        

        cont += 1

    

    print(f"Maior peso: {maior} Inscrição {maior_inscrito}")
    print(f"Menor peso: {menor} Inscrição {menor_inscrito}")


main()