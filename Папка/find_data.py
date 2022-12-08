import csv
import user_interface as ui
import os.path
import logger as log

def find_id(id):
    if os.path.exists('students.csv'):
        with open('students.csv', 'r', encoding='utf-8') as stud:
            reader = csv.reader(stud)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if id == item[0]:
                    ui.view_data(item)
                    log.find_data_logger(item)
                    count+=1
            if count == 0:
                ui.view_data(f'{id} не найден!')
    else:
        ui.view_data('Файл не найден!')

def find_surname(surname):
    if os.path.exists('students.csv'):
        with open('students.csv', 'r', encoding='utf-8') as stud:
            reader = csv.reader(stud)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if surname == item[1]:
                    ui.view_data(item)
                    log.find_data_logger(item)
                    count+=1
            if count == 0:
                ui.view_data(f'{surname} не найден!')
    else:
        ui.view_data('Файл не найден!')