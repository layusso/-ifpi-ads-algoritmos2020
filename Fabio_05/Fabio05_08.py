def main():
    a = []
    maior = 0
    menor = 100000000000
    n = int(input("Informe a quantidade de elementos do vetor: "))
    for i in range(n):
        elemento = int(input(f"Qual o valor do {i} elemento: "))
        a.append(elemento)
    
    for i in range(len(a)):
        if a[i] > maior:
            maior = a[i]
        elif a[i] < menor:
            menor = a[i]

    maximo = a.index(maior)
    minimo = a.index(menor)

    print(a)
    print("Maior elemento: ", maior, "Index: ", maximo)
    print("Menor elemento: ", menor, "Index: ", minimo)

main()