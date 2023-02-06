from user_interfase import choice, teacher, student
from add_info import save_file
from search import student_search

# Запуск основного меню программы

def start():
    while(True):
        button = choice()    
        if button == 1:
            button = teacher()
            if button == 1:
                save_file()
                print('\n')
            elif button == 2:
                print('Работа окончена')
                break
    
        elif button == 2:
            button = student()
            if button == 1:
                student_search()
                print('\n')
            elif button == 2:
                print('Работа окончена')
                break
        elif button == 3:
            print('Работа окончена')
            break
            



