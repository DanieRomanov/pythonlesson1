a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if b < a < c or c < a < b:
    print(f'Среднее число: {a}')
elif a < b < c or c < b < a:
    print(f'Среднее число: {b}')
else:
    print(f'Среднее число: {c}')