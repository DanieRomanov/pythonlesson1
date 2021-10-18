first_letter = input("Введите первую букву: ")
second_letter = input("Введите вторую букву: ")
number_letters = 0

if ord(first_letter) > ord(second_letter):
    number_letters = ord(first_letter) - ord(second_letter) - 1
elif ord(first_letter) < ord(second_letter):
    number_letters = ord(second_letter) - ord(first_letter) - 1
else:
    print('Ошибка')

first_letter_place = ord(first_letter) - 1071
second_letter_place = ord(second_letter) - 1071

print(f'Количество букв в промежутке от {first_letter} до {second_letter} = {number_letters}\n'
      f'Место буквы {first_letter} в алфавите = {first_letter_place}\n'
      f'Место буквы {second_letter} в алфавите = {second_letter_place}')