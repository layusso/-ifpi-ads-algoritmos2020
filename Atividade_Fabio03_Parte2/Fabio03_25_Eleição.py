def main():
    n = int(input("Informe a quantidade de eleitores"))
    cand_A = 0
    cand_B = 0
    cand_C = 0
    nulo = 0
    branco = 0
    cont = 0

    while cont < n:
        voto = int(input("1-A  2-B   3-C  9-Nulo  0-Branco: "))

        if voto == 1:
            cand_A += 1
        elif voto == 2:
            cand_B += 1
        elif voto == 3:
            cand_C += 1
        elif voto == 9:
            nulo += 1
        elif voto == 0:
            branco += 1
        
        cont += 1
    

    if cand_A > cand_B and cand_A > cand_C:
        print("Candidato A venceu!")
    elif cand_B > cand_A and cand_B > cand_C:
        print("Candidato B venceu!")
    elif cand_C > cand_B and cand_C > cand_A:
        print("Candidato C venceu!")


    print(f"Total de votos:  A:{cand_A} votos, B:{cand_B} votos, C:{cand_C} votos.")
    print(f"Nulos:{nulo} votos,  Branco:{branco} votos")


main()