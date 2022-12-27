# Задача 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform

n = int(input('Введите размер списка: '))
list = []
for i in range(n):
    list.append(round(uniform(0, 9),2))

print('Наш список: ', list)

min = 1
max = 0
for el in list:
    if el - int(el) > max:
        max = el - int(el)
    if el - int(el) < min:
        min = el - int(el)
difference = round((max - min),2)
print(round(max,2),round(min,2))
print('Разница дробной части: ', difference)