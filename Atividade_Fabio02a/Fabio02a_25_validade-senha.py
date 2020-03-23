def senha():
    senha = input('Digite a senha:')
    password = str(1234)
    if senha == password:
        print('Acesso autorizado!')
    else:
        print('Senha incorreta, tente novamente!')

senha()
