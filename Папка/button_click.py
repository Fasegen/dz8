import user_interface as ui
import addition as add
import find_data as fd

def start():
    choise = ui.choise()
    if choise == '1':
        add.add_stud()
        ui.choise()
    elif choise == '2':
        search_by = input(' 1 - поиск по id\n 2 - поиск по фамилии\n')
        if search_by == '1': fd.find_id(input('Введите номер id: '))
        if search_by == '2': fd.find_surname(input('Введите фамилию: '))
        ui.choise()

start()