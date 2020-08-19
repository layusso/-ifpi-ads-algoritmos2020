def main(): 
    qtd = int(input("Informe a quantidade de números: "))
    qtd_atual = 2
    anterior = 0
    atual = 1
    print(anterior, atual, end=" ")

    while qtd_atual < qtd:
        novo_atual = anterior + atual
        print(novo_atual, end=" ")
        anterior = atual
        atual = novo_atual
        qtd_atual += 1



main()