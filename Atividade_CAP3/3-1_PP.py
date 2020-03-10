def main():
    palavra = input("Digite a palavra: ")
    right_justify(palavra)


def right_justify(s):
    espacos = 70 - len(s)
    print(" " * espacos + s)


main()

    
    
    

    