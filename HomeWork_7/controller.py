from add_contact import save_contact, save_file
from user_interface import choice
from logger import reading_all, view

# Запуск основного меню программы

def start():
    while(True):
        button = choice()    
        if button == 1:
            print('Вносим нового абонента')
            contact = save_contact()
            save_file(contact)

        elif button == 2:
            print('\nПоказать всех абонентов\n')
            reading_all(view())
        
        elif button == 3:
            print('Работа окончена')
            break