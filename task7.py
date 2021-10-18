a = int(input('Введите сторону AB: '))
b = int(input('Введите сторону BC: '))
c = int(input('Введите сторону CA: '))

if a + b > c and a + c > b and b + c > a:
    if (a==b or a==c or b==c):
        if a==b and b==c:
            print('Это равносторонний треугольник')
        else:
            print('Это равнобедренный треугольник')
    else:
        print('Это разносторонний треугольник')
else:
    print('Ошибка')