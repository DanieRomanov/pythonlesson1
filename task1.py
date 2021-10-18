num = int(input('Введите трёхзначное число'))
a = num // 100
b = (num % 100) // 10
с = num % 10
sum = a + b + с
multiply = a * b * с

print(f'сумма цифр: {sum}\n'
      f'произведение цифр: {multiply}')