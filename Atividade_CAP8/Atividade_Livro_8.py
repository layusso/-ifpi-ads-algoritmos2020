def main():
    string = input("Digite uma palavra ou letra: ")
    numero = int(input("Indique o número de rotação: "))
    print(rotate_word(string, numero))


def rotate_word(texto, numero):
    palavra = ""
    for i in range(len(texto)):
        nova_letra = chr(ord(texto[i]) + numero)
        palavra += nova_letra

    return palavra


main()