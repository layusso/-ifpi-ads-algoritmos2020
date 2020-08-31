def main():
    n = int(input("Digite o número de cadastros que deseja realizar"))
    maior = 0
    maior_inscrito = 0
    menor_inscrito = 0
    menor = 300000000


    for i in range(1, n+1):
        nome = input('Informe o nome: ')
        inscricao = int(input("Digite o número de inscrição; "))
        peso = float(input("Informe o peso: "))

        if peso > maior:
            maior = peso
            maior_inscrito = inscricao
        
        if peso < menor:
            menor = peso
            menor_inscrito = inscricao
        

    

    print(f"Maior peso: {maior} Inscrição {maior_inscrito}")
    print(f"Menor peso: {menor} Inscrição {menor_inscrito}")


main()