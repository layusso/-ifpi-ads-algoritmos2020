def main():
    a = []
    b = []

    n = int(input("Informe a quantidade de elementos do vetor: "))
    for i in range(n):
        elemento = input(f"Qual o valor do {i} elemento: ")
        a.append(elemento)

    for i in range(len(a)):
        if int(a[i]) % 2 == 0:
            b.append(0)
        else:
            b.append(1)
    
    print(a)
    print(b)

main()