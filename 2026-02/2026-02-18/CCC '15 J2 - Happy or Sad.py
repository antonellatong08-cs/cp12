c = input()
sad = c.count(':-(')
happy = c.count(':-)')
if sad == 0 and happy == 0:
    print('none')
elif sad > happy:
    print('sad')
elif sad < happy:
    print('happy')
else:
    print('unsure')