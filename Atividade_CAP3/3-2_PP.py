def do_twice(f, valor):
    f(valor)
    f(valor) 



def print_spam(arg):
    print(arg)


def print_twice(arg):
    print(arg)
    print(arg)


def do_four(obj, arg):
    do_twice(obj, arg)
    do_twice(obj, arg)

do_four(print_twice, "spam")