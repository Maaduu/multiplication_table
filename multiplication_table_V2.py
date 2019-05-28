number = 5
continuer = 'y'

while continuer == 'y':
    number = input('Enter a number: ')

    for i in range(1, 11):
        print('{0} X {1} = {2}'.format(number, i, int(number) * i))
    continuer = input('Do you want to continue? y/n')

print('fin du script.')
