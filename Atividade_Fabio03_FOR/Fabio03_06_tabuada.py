def soma():
    for i in range(1, 11):
        for j in range(1, 11):
            result = i + j
            print(f'{i} + {j} = {result}')


def div():
    for i in range(1, 11):
        for j in range(1, 11):
            result = i / j
            print(f'{i} / {j} = {result}')


def sub():
    for i in range(1, 11):
        for j in range(1, 11):
            result = i - j
            print(f'{i} - {j} = {result}')


def mult():
    for i in range(1, 11):
        for j in range(1, 11):
            result = i * j
            print(f'{i} x {j} = {result}')

soma()
sub()
div()
mult()