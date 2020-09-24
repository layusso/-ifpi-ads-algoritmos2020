def main():
    qnt_numeros = int(input("Digite quantos números pretende digitar: "))
    vetor = [-1] * qnt_numeros

    for i in range(qnt_numeros):
        valor = int(input("Insira o valor: "))
        vetor[i] = valor
    
    contador(vetor)
    contador(modificando(vetor))
    media(modificando(vetor), qnt_numeros)


def contador(vetor):
    positivos = 0
    negativos = 0
    pares = 0
    impares = 0

    for i in vetor:
        if i > 0:
            positivos += 1
        if i < 0:
            negativos += 1
        if i % 2 == 0:
            pares += 1
        if i % 2 != 0:
            impares += 1

    print(f"Existem {positivos} positivos, {negativos} negativos , {pares} pares e {impares} impares")


def modificando(vetor):
    for i in range(len(vetor)):
        if i > 0:
            vetor[i] = vetor[i] * 2
        if i < 0:
            vetor[i] = vetor[i] // 2 

    return vetor


def media(vetor, qnt_numeros):
    total = 0
    for i in vetor:
        total += i

    media = total / qnt_numeros
    print(f"A média dos valores é de {media:.2f}")


main()