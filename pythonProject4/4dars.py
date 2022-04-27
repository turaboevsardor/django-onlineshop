#names = []

#while True:



name = []
numbers = []
xizmatlar = []

while True:
    nima = input('nimani qoshamiz ')

    if nima == 'nomerlar':
        number = input('nomerni yozin ')
        numbers.append(number)
        print(numbers)

    elif nima == 'ismingiz':
        y = input('ismingiz ')
        name.append(y)
        print(name)

    elif nima == 'xizmatlar':
        r = input('nima xizmat ')
        xizmatlar.append(r)
        print(xizmatlar)
