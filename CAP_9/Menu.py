arquivo = open("words.txt")

def main():
    print("## Digite um número para solicitar a ação correspondente ## \n" \
        + " 1 - Buscar palavras por tamanho mínimo. \n" \
        + " 2 - Apresentar número de palavras que não contenha as letras: \n" \
        + " 3 - Número de palavras com letras obrigatórias: \n" \
        + " 4 - Palavras cujo as letras estejam em ordem alfabética. \n" \
        + " 0 - Sair. \n")

    opcao = int(input("Digite um número para solicitar a ação correspondente: "))
    while opcao != 0:
        if opcao == 1:
            buscar_palavra(arquivo)
        elif opcao == 2:
            has_no_letter(arquivo)
        elif opcao == 3:
            letras_obrigatorias(arquivo)
        elif opcao == 4:
            ordem_alfabetica(arquivo)
        
        opcao = int(input("Digite um número para solicitar a ação correspondente: "))

    if opcao == 0:
        arquivo.close()


def buscar_palavra(arquivo):
    numero = int(input("Digite o tamanho minimo das palavras: "))
    for linha in arquivo:
        palavra = linha.strip()
        if len(palavra) >= numero:
            print(palavra)


def has_no_letter(arquivo):
    letras_proibidas = input("Digite a sequencia de letras proibidas: ")
    lista_negra = []
    cont = 0
    numero = 0

    for i in range(len(letras_proibidas)):
        lista_negra.append(letras_proibidas[i])

    for linha in arquivo:
        for j in range(len(linha)):
            if linha[j] in lista_negra:
                cont += 1

        if cont == 0:
            numero += 1
        
        elif cont != 0:
            cont = 0

    print(f"Existem {numero} palavras sem as letras: {letras_proibidas}")


def letras_obrigatorias(arquivo):
    letras_obrigatorias = input("Digite a sequencia de letras obrigatórias: ")
    lista = []
    numero = 0

    for i in range(len(letras_obrigatorias)):
        lista.append(letras_obrigatorias[i])

    cont = len(lista)

    for linha in arquivo:
        for j in range(len(linha)):
            if linha[j] in lista:
                cont -= 1

        if cont <= 0:
            numero += 1
            cont = len(lista)

        elif cont > 0:
            cont = len(lista)

    print(f"Existem {numero} palavras com as letras: {letras_obrigatorias}")
    


def ordem_alfabetica(arquivo):
    #Acho que está errada, mas não sei onde estou errando ;-;
    numero = 0
    cont = 0

    for linha in arquivo:
        anterior = linha[0]
        for j in linha:
            if j < anterior:
                cont += 1

            anterior = j

        if cont == 0:
            numero += 1
            cont = 0 

        elif cont != 0:
            cont = 0

    print(f"Existem {numero} palavras em ordem alfabética: ")


main()