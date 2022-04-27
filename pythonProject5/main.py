calculator = []

while True:
    w = int(input('yozin'))
    k = input('keyingisi')
    h = int(input('nima qlasiz'))

    if  k  == '-':
        print(w - h)
    elif k  == '+':
        print(w + h)
    elif k  == '/':
        print(w / h)
    elif k  == '*':
        print(w * h)
    elif k  == '%':
        print(w % h)
    else:
        print('no togri')

