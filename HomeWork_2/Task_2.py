# Задача 2. Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5

n = int (input('Введите число N: '))
i = 2
for i in range(2,n+1):
    if n % i == 0:
       print(f'Ответ: {i}')
       break

