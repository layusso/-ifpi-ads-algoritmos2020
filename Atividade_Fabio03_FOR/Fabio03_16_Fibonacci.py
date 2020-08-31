def main(): 
    qtd = int(input("Informe a quantidade de números: "))
    anterior = 0
    atual = 1
    print(anterior, atual, end=" ")

    for i in range(2, qtd+1):
        novo_atual = anterior + atual
        print(novo_atual, end=" ")
        anterior = atual
        atual = novo_atual



main()