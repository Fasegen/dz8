def choise():
    print('\nВыберите действие:\n\
        1 - добавить данные о учениках\n\
        2 - поиск ученика в базе\n\
        0 - выход\n\
            ')

    ch = input('Введите цифру: ')
    return ch

def view_data(data):
    print(data)