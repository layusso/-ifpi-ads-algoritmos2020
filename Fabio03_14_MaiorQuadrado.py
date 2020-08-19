def main():
    n = int(input("Digite o valor de n: "))
    cont = 0

    while cont <= n:
        if cont ** 2 <= n:
            maior = cont ** 2

        cont += 1    
    

    print(f"O maior quadrado é de {maior}")

main()