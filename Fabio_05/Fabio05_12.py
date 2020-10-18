def main():
    mat = []

    n = int(input("Informe a orgem da matriz: "))

    for i in range(n):
        linhas = []
        for j in range(n):
            linhas.append(int(input("Digite o valor:")))
        mat.append(linhas)

    for i in range(len(mat)):
        