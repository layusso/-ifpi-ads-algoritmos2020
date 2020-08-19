def main():
    n = int(input("Digite um número inteiro: "))
    cont = 0

    while cont <= n:
        if cont % 2 == 0:
            print(cont)
        
        cont+= 1

main()