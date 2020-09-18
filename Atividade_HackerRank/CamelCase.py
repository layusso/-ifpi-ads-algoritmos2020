def main():
    s = input("Insira o texto: ")
    palavras = 1

    for i in range(len(s)):
        if 65 <= ord(s[i]) <= 90:
            palavras += 1


    print(f"Existe {palavras} palavra(s)")
main()