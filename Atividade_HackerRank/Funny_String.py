def main():
    s = int(input("Numero de testes: "))
    cont = 1

    while cont <= s:
        palavra = input("Insira a palavra: ")
        palavra_invertida = palavra[::-1]
        
        aD1 = ""
        aD2 = ""

        for i in range(len(palavra) - 1):
             dif1 = ord(palavra[i]) - ord(palavra[i + 1])
             dif2 = ord(palavra_invertida[i]) - ord(palavra_invertida[i+1])

             if dif1 < 0:
                 dif1 * -1
             if dif2 < 0:
                 dif2 * -1
             aD1 += str(dif1)
             aD2 += str(dif2)
            

        if aD1 == aD2:
            print("Funny")

        else:
            print("Not Funny")

        cont += 1


main()
