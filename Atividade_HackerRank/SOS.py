def main():
    s = input("Mensagem recebida: ")
    mensagem_correta = "SOS" * (len(s)//3)
    erros = 0


    for i in range(len(s)):
        if s[i] != mensagem_correta[i]:
            erros += 1
    
    print(f"Existem {erros} letras afetadas")

main()