# Задача 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и вывести многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 
# k = 6
# ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h
# a, b, c, d, e, h - рандом


import random as rand
k = int(input('Введите степень: '))

string = ''

for i in range(k, 1,-1):
    string += str(rand.randint(1, 99)) + 'x^' + str(i) + ' + ' 
result = string + str(rand.randint(1, 99)) + 'x + ' + str(rand.randint(1, 99))

print(result)
