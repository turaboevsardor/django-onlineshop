from random import choice
computer_choice = choice(['tosh','qaychi','qogoz'])
my = input('(enter player 1 choice ')
if my =='tosh' and computer_choice == 'qaychi':
    print('man yutdim')
elif my == 'tosh' and computer_choice == 'qogoz':
    print('computer yutdi')
elif my == computer_choice:
    print('durrang')
elif my == 'qaychi' and computer_choice == 'qogoz':
    print('man yutdim')
elif my == 'qaychi' and computer_choice == 'tosh':
    print('computer yutdi')
elif my == 'qogoz' and computer_choice == 'qogoz':
    print('durrang')
else:
    print('oyin tugadi')

