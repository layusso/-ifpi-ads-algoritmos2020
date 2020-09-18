def main():
    n = int(input("Numero de caracteres: "))
    password = input("Digite a senha: ")
    contador = 6
    numero_letras = 0
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    for i in range(len(password)):
        numero_letras += 1
    
    if numero_letras < contador:
        contador -= numero_letras
        print(contador)
    
    else:
        contador = 4
        condicao = 0
        for i in range(len(password)):
            if password[i] in numbers:
                condicao += 1
        
        if condicao != 0:
            contador -= 1
            condicao = 0
        
        for i in range(len(password)):
            if password[i] in lower_case:
                condicao += 1
        
        if condicao != 0:
            contador -=1
            condicao = 0
        
        for i in range(len(password)):
            if password[i] in upper_case:
                condicao += 1
        
        if condicao != 0:
            contador -= 1
            condicao = 0

        for i in range(len(password)):
            if password[i] in special_characters:
                condicao += 1
        
        if condicao != 0:
            contador -= 1
            condicao = 0
             
        print(contador)

main()