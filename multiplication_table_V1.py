number = 5
continuer = 'y'

while continuer == 'y':
    number = input('Enter a number: ')

    for i in range(1, 11):
        print(number * i)
    continuer = input('Do you want to continue? y/n')

print('fin du script.')
