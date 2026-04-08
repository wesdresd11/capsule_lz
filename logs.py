import pandas as pd
import datetime     #дата, время
import uuid         #генератор уникальных id
import getpass      #получим pc_username
import os           #проверим существование файла записи логов, чтоб не пыаться создать уже существующий  


def log(func):                          #создаем декоратор
    def wrapper(*args, **kwargs):       #так можем принять какие угодно обьекты
        now_utc = datetime.datetime.now(datetime.timezone.utc) #узнаем текущие дату и время
        log_data = {            #прописываем какие логи хотим получить
            'id': str(uuid.uuid4()),                #задаем логу id
            'pc_username': getpass.getuser(),           #получаем username
            'function_name': func.__name__,                #получаем имя функции
            'date_utc': now_utc.strftime('%d-%m-%Y'),       #дата в формате дата.месяц.год
            'time': now_utc.strftime('%H:%M:%S'),           #время в формате час:минута:секунда
        }
        df = pd.DataFrame([log_data])                      #превращаем словарь в датафрейм
        log_file = 'logs.csv'        #путь к файлу
        file_exists = os.path.isfile(log_file)            #проверяем существование файла по ранее указанному пути
        df.to_csv(log_file, mode='a', index=False, header=not file_exists, encoding='utf-8')   #записываем файл в csv, записи будут добавляться в конец
        #индексы ставиться не будут, так как мы задали логам свои id, заголовки не будут снова прописываться если файл уже создан
        return func(*args, **kwargs)

    return wrapper