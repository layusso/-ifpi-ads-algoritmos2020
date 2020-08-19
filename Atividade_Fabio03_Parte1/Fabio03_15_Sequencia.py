def main():
    n = int(input("Digite a quantidade de termos: "))
    cont = 1
    i = 2
    j = 1
    print(1, end=" ")
    while cont < n:
        sequencia = j + i
        cont += 1
        j = sequencia
        i += 1
        print(sequencia, end=" ")

main()