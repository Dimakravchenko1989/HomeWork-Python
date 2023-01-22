# Задача 1. Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]
# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

list1 = [12,'sadf',5643,'sdlkjs', 14593, 'jkdl', 23847]
print(list)

result1 = list(filter(lambda x: type(x) == int, list1))
result2 = list(filter(lambda x: type(x) == str, list1))

print('Список чисел: ',result1)
print('Список букв: ',result2)