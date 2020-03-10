def do_three(f):
    f()
    f()
    f()

def do_six(f):
    do_three(f)
    do_three(f)

def print_beam():
    print('+ - - - -', end=' ')

def print_post():
    print('|        ', end=' ')

def print_beams():
    do_three(print_beam)
    print('+')

def print_posts():
    do_three(print_post)
    print('|')

def print_row():
    print_beams()
    do_six(print_posts)

def print_grid():
    do_three(print_row)
    print_beams()

print_grid()
    