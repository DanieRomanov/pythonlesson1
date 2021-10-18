from random import randint, uniform


data_type = input("Введите тип данных 1(Целые числа)|2(Дробные числа)|3(Буквы): ")
start = input("Введите начальную цифру/букву: ")
end = input("Введите конечную цифру/букву: ")

if data_type == '1':
    r = randint(int(start), int(end))
elif data_type == '2':
    r = uniform(float(start), float(end))
elif data_type == '3':
    r = chr(randint(ord(start), ord(end)))
else:
    r = f"Ошибка (Неверно выбран тип данных)"

print(f"Случайное значение в выбранном диапазоне = {r}")