def main():

    a = []
    n = int(input("Digite a quantidade de elementos: "))
    for i in range(n):
        elemento = int(input(f"Qual o valor do {i} elemento: "))
        a.append(elemento)

    print(a)
    print(sorted(a))


main()