# Задача 3. Задайте последовательность чисел. Напишите программу, которая выведет список элементов, 
# которые не имели повторов в исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1


from random import randint

N = int(input('Введите размер списка: '))
list = []
for i in range(0, N):
    a = randint(0,N+1)
    list.append(a)
print(list)

newlist = []
for i in list:
    if list.count(i) == 1:
        newlist.append(i)
print('Элементы, которые не имели повторов',newlist)

