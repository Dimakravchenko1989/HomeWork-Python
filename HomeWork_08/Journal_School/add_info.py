# Сохранение фамилии, предмета и оценок в отельный файл

def save_file():
    predmet = input('Введите данные ученика в формате: Фамилия, Имя, предмет, оценки: ')
    with open('journal_data.csv', 'a', encoding='utf-8') as file:
        file.write(predmet + '\n')
        