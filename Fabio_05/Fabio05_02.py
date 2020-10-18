def main():
    a = []
    repetidos = 0

    n = int(input("Informe a quantidade de elementos do vetor: "))
    for i in range(n):
        elemento = input(f"Qual o valor do {i} elemento: ")
        a.append(elemento)
    
    for i in range(len(a)):
        if a.count(a[i]) > 1:
            repetidos += 1

    if repetidos > 0:
        print("Existem elementos repetidos")
    else:
        print("Não existem elementos repetidos")
    
main()