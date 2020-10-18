def main():
    a = []
    b = []

    n = int(input("Informe a quantidade de elementos do vetor: "))
    for i in range(n):
        elemento = input(f"Qual o valor do {i} elemento: ")
        a.append(elemento)

    b = a[::-1]

    print(f"Vetor A = {a}")
    print(f"Vetor B = {b}")
main()