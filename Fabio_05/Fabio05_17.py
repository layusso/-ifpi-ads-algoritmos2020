def main():
    mat = []
    maior = 0
    linha_maior = 0


    menor = 3000000000000
    linha_menor = 0

    soma = 0

    n = int(input("Informe a orgem da matriz: "))
    cont = 0

    for i in range(n):
        linhas = []
        for j in range(n):
            linhas.append(int(input("Digite o valor:")))
        mat.append(linhas)
    

    for i in range(len(mat)):
        soma = sum(mat[i])         

        if soma > maior:
            maior = soma
            linha_maior = mat[i]
        
        if soma < menor:
            menor = soma
            linha_menor = mat[i]

    print(f"Linha com maior soma: {linha_maior}")
    print(f"Linha com menor soma: {linha_menor}")



main()