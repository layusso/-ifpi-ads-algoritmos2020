def main():
    mat = []

    n = int(input("Informe a orgem da matriz: "))
    cont = 0

    for i in range(n):
        linhas = []
        for j in range(n):
            linhas.append(int(input("Digite o valor:")))
        mat.append(linhas)
    

    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != mat[j][i]:
                cont += 1

    if cont > 0:
        print("Não é simétrica!")

    else:
        print("É simétrica!")


main()