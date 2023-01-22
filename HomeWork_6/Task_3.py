# Задача 3. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите вещественное число: ')
digit = filter(lambda x: x.isdigit(), str(number))
sum_number = sum(map(int, digit))

print('Сумма цифр в числе равна: ',sum_number)
