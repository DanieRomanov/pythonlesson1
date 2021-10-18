number_letter = int(input('Введите номер буквы в алфавите: '))
number_letter += ord('a') - 1

letter = chr(number_letter)

print(f'Ваша буква: {letter}')