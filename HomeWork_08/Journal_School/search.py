# Поиск ученика, просмотр оценок

def student_search():
    name = input('Введите фамилию ученика: ')
    print('\n')
    with open('journal_data.csv', 'r', encoding='utf-8') as data:
        info_list = data.read().splitlines()
        for person in info_list:
            if name in person:
                print(person)
                

