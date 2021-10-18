year = int(input('Введите год: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Это високосный год')
        else:
            print('Это невисокосный год')
    else:
        print('Это високосный год')
else:
    print('Это невисокосный год')