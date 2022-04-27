calkulator = []

while True:
    w = int(input('yozin'))
    k = input('nima qlamz')
    h = int(input('keyingisi'))
    if w  == '-':
        print(w-k)
    elif w == '%':
        print(w%k)
    elif w  == '+':
        print(w+k)
    elif w == '*':
        print(w*k)
    elif w == '/':
        print(w/k)
    