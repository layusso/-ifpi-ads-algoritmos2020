def main():
    lista = []

    print("1 - Inserir valores. \n" \
          "2 - Mostrar valor na posição x. \n" \
          "3 - Mostrar todos os valores. \n" \
          "4 - Remover valor final. \n" \
          "5 - Remover valor do inicio. \n"\
          "6 - Remover valor da posição x. \n" \
          "7 - Inserir valores em posição específica. \n" \
          "8 - Contagem geral(Pares, Impares, Zerados). \n" \
          "9 - Média dos valores. \n" \
          "10 - Contar ocorrências de um valor. \n" \
          "11 - Transformar valores(Em manutenção xD). \n" \
          "0 - Sair")

    opcao = int(input("Digite a operação desejada: "))
    while opcao != 0:
        if opcao == 1:
            inserir_valores(lista)
            opcao = int(input("Digite a operação desejada: "))

        elif opcao == 2:
            mostrar_valor_posicao(lista)
            opcao = int(input("Digite a operação desejada: "))

        elif opcao == 3:
            mostrar_valores(lista)
            opcao = int(input("Digite a operação desejada: "))

        elif opcao == 4:
            remover_final(lista)
            opcao = int(input("Digite a operação desejada: "))

        elif opcao == 5:
            remover_inicio(lista)
            opcao = int(input("Digite a operação desejada: "))

        elif opcao == 6:
            remover_posicao(lista)
            opcao = int(input("Digite a operação desejada: "))

        elif opcao == 7:
            inserir_valor_posicao(lista)
            opcao = int(input("Digite a operação desejada: "))

        elif opcao == 8:
            contagem_geral(lista)
            opcao = int(input("Digite a operação desejada: "))

        elif opcao == 9:
            media(lista)
            opcao = int(input("Digite a operação desejada: "))

        elif opcao == 10:
            contagem_ocorrencias(lista)
            opcao = int(input("Digite a operação desejada: "))

        elif opcao == 11:
            transformar(lista)
            opcao = int(input("Digite a operação desejada: "))

        elif opcao == 0:
            break

        else:
            print("Opção inválida!")


def inserir_valores(lista):
    qtd_valores = int(input("Quantos valores deseja adicionar?: "))
    for i in range(qtd_valores):
        valor = float(input(f"Digite o {i} valor: "))
        lista.append(valor)
    

    input("<enter> para continuar...")


def mostrar_valor_posicao(lista):
    posicao = int(input("Informe a posição que deseja consultar: "))

    if len(lista) >= posicao:
        print(f"O valor da posição {posicao} é: ", lista[posicao])
        input("<enter> para continuar...")

    else:
        print("Essa posição não existe!")
        input("<enter> para continuar...")


def mostrar_valores(lista):
    if lista == []:
        print("Não existe nenhum valor")
        input("<enter> para continuar...")
    else:
        for i in lista:
            print(i)
        input("<enter> para continuar...")


def remover_final(lista):
    lista.remove(lista[-1])
    print("Valor final removido!")
    input("<enter> para continuar...")


def remover_inicio(lista):
    lista.remove(lista[0])
    print("Valor inicial removido!")
    input("<enter> para continuar...")


def remover_posicao(lista):
    posicao = int(input("Informe a posição: "))

    if len(lista) >= posicao:
        lista.remove(lista[posicao])

        print(f"Valor na posição {posicao} removido!")
        input("<enter> para continuar...")
    else:
        print("Posição inválida!")
        input("<enter> para continuar...")


def inserir_valor_posicao(lista):
    posicao = int(input("Informe a posição: "))
    valor = float(input("Digite o valor: "))
    if len(lista) >= posicao:
        lista[posicao] = valor

        print(f"Valor adicionado na posição {posicao}!")
        input("<enter> para continuar...")
    else:
        print("Posição inválida!")
        input("<enter> para continuar...")    


def contagem_geral(lista):
    pares = 0
    impares = 0
    zerados = 0

    for i in lista:
        if i == 0:
            zerados += 1
        elif i % 2 == 0:
            pares += 1
        elif i % 2 != 0:
            impares += 1


    print(f"Existem {pares} numeros pares, {impares} impares, e {zerados} zeros")
    input("<enter> para continuar...")


def media(lista):
    soma = 0
    for i in lista:
        soma += i
    
    media = soma // len(lista)
    print(f"A média dos valores é de {media}")
    input("<enter> para continuar...")


def contagem_ocorrencias(lista):
    valor = int(input("Digite o valor a ser consultado: "))
    ocorrencia = 0

    for i in lista:
        if i == valor:
            ocorrencia += 1
    
    print(f"O valor ocorre {ocorrencia} vezes")
    input("<enter> para continuar...")



def transformar(lista):
    '''Problemas:
    Por algum motivo as opções 2 e 3 não são lidas.
    A função não está modificando a lista principal.'''
    
    print("Selecione o que deseja transformar \n" \
         "1 - Dobrar valores \n" \
         "2 - Apagar todos os valores \n" \
         "3 - Dobrar valores multiplos de n \n" \
         "0 - voltar...")

    opcao = int(input("Digite o valor da operação: "))
    while opcao == True:
        if opcao == 1:
            lista = dobrar(lista)
            
            print("Os valores foram dobrados!")
            opcao = int(input("Digite o valor da operação: "))

        elif opcao == 2:
            lista = []
            print("Valores apagados!")
            opcao = int(input("Digite o valor da operação: "))

        if opcao == 3:
            n = int(input("Informe o valor de n: "))
            lista = dobrar_multiplos(lista, n)
            print(lista)
            print("Valores dobrados!")
            opcao = int(input("Digite o valor da operação: "))

        if opcao == 0:
            break


def dobrar(lista):
    nova_lista = []
    for i in lista:
        nova_lista.append(i*2)
    
    return nova_lista


def dobrar_multiplos(lista, n):
    nova_lista = []
    for i in lista:
        if i % n == 0:
            nova_lista.append(i*2)
        else:
            nova_lista.append(i)
    
    return nova_lista


main()
