from datetime import datetime as dt

def add_data_logger(data):
    time = dt.now()
    with open('log.txt', 'a', encoding='utf-8') as log:
        log.write('{}; добавлены данные; {}\n'
                    .format(time, data))

def find_data_logger(data):
    time = dt.now()
    with open('log.txt', 'a', encoding='utf-8') as log:
        log.write('{}; поиск по данным ; {}\n'
                    .format(time, data))