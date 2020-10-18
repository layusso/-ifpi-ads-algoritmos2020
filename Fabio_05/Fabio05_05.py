def main():
    a = []
    s = 0
    for i in range(20):
        elemento = input(f"Qual o valor do {i} elemento: ")
        a.append(elemento)

    for i in range(len(a)):
        s += (int(a[i]) - int(a[-(i+1)]))**0.5 

    print(s)

main()