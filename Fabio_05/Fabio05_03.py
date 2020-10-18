def main():
    a = []
    b = []
    c = []

    n = int(input("Informe a quantidade de elemtentos em A: "))

    nb = int(input("Informe a quantidade de elemtnos em B: "))

    for i in range(n):
        a_element = input("Digite elemento de A: ")
        a.append(a_element)
    
    for i in range(nb):
        b_element = input("Digite elemento de B: ")
        b.append(b_element)

    c = a + b
    print(c)


main()