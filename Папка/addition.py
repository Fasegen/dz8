import csv
import logger as log

def add_stud():    
    with open ('students.csv', 'w', encoding='utf-8') as stud:
        writer = csv.writer(stud, delimiter=';')
        writer.writerow(('id', 'surname', 'name', 'grade', 'info'))

    id = 1
    exit = None

    while exit !='q':
        list_info = [id, input('Фамилия ученика: '), input('Имя ученика: '),
        input('Класс в котором учиться: '), input('Доп. информация: ')]
        id +=1

        log.add_data_logger(list_info)

        with open('students.csv', 'a', encoding='utf-8') as stud:
            writer = csv.writer(stud, delimiter=';')
            writer.writerow(list_info)

        exit = input('"Enter" - продолжить вводить данные\n"q"- выйти в главное меню\n')