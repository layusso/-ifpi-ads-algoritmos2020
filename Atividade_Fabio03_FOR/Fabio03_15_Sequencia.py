def main():
    n = int(input("Digite a quantidade de termos: "))
    j = 1
    print(1, end=" ")
    for i in range(2, n+1):
        sequencia = j + i
        j = sequencia
        print(sequencia, end=" ")

main()