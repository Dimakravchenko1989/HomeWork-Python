# Задача 1. Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

from random import randint

candies_total = 120
max_take = 28
player_1 = input('\nКак тебя зовут?: ')
player_2 = 'Компьютер'
players = [player_1, player_2]

while candies_total > 0:
    a = int(input(f'{player_1} введите количество конфет '))
    if a > 28 or a < 0:
        print(f'По правилам можно взять только {max_take} конфет')
    elif a < 29 and a > 0:
        if candies_total - a == 0:
            print(f'Победил {player_1}')
            break
        elif candies_total - a <= 0:
            raise ValueError('Неверный ход')
        else:
            candies_total = candies_total - a
            print(f'Осталось {candies_total} конфет')
    if candies_total > 28:
        b = randint(1,28)
        candies_total = candies_total - b
        print(f'{player_2} забрал {b} конфет')
        print(f'Осталось {candies_total} конфет')
    elif candies_total - b == 0:
        print(f'Победил {player_2}')
        break
    elif candies_total < 28:
        b = randint(1,candies_total)
        print(f'{player_2} забрал {b} конфет')
        candies_total = candies_total - b
        print(f'Осталось {candies_total} конфет')
    elif candies_total - b <= 0:
        print('Неверный ход')
    else:
        candies_total = candies_total - b
        print(f'Осталось {candies_total} конфет')
