def soma():
    i = 1
    cont = 1
    while i <= 10:
        while cont <= 10:
            result = i + cont
            print(f'{i} + {cont} = {result}')
            cont += 1
        
        cont = 1
        i += 1


def div():
    i = 1
    cont = 1
    while i <= 10:
        while cont <= 10:
            result = i / cont
            print(f'{i} / {cont} = {result}')
            cont += 1
        
        cont = 1
        i += 1

def sub():
    i = 1
    cont = 1
    while i <= 10:
        while cont <= 10:
            result = i - cont
            print(f'{i} - {cont} = {result}')
            cont += 1
        
        cont = 1
        i += 1

def mult():
    i = 1
    cont = 1
    while i <= 10:
        while cont <= 10:
            result = i * cont
            print(f'{i} * {cont} = {result}')
            cont += 1

        cont = 1
        i += 1


soma()
sub()
div()
mult()