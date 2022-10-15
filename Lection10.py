#Встроенные модули и пакеты
from random import getrandbits
from typing import List

    from .main import foo, bar, baz

    __all_: List[str] = [
        'foo',
        'bar',
        'baz'
]
#List чтобы указать аннотацию типа чтобы показать суть переменной олл
#Когда будем тестить нужно олл, иначе будет ругаться на ниит файл типа импорты нигде не используются

#Абсолютный импорт: from mypackage import *
#Относительный импорт: . (из этой же папки где лежит инит файл)
# или .. (на папку выше, в родительской папке)

#Импорт с другим именем. Псевдонимы
# from mypackage import randint as myrandint
#и потом обращаться к этому по псевдониму внутри файла.

#Два файла, в одном есть ф-я которая нужна.
from main import foo
#Но этот вызов не нужен. Значит нужна точка входа.
if __name__ = '__main__':
    foo()
#теперь эта ненужная функуция не будет вызываться в других местах когда не нужна


#RegExp, Регулярные выражения

#Copy, Copy and Deepcopy

#IterTools - фильтрация

#Math - улучшенная математика

#Random - для генерации всего что генерируется
from randon getrandbits

print(getrandbits(20))

#OS - для работы с осью, если пишешь приложение для операционки. Создает папки, открывает папки, запускает файлы

#Pathlinb - работа с путями операционной системы
from pathlib import Path
import os

BASE_DIR = Path(__file__).parent
STATIC_URL = 'static\\'
print(os.path.join(BASE_DIR, STATIC_URL))

#Sys - набор ф-й для определния как python работает с операционной системой
#какая версия питона, параметры командной строки, т.д.

from pathlib import Path
import os

print(os.getcwd()) #найти папку, если нет то сгенерировать

#Datetime
from datetime import datetime, timedelta

delta = timedelta(days=5)
start_date = datetime(
    year=2023,
    month=4,
    day=24,
)
print(start_date + delta)


print(datetime.now().strftime('%A %d %B %Y %H:%M'))
date = '23.4.2019 12-25'
print(datetime.strptime(date, '%d.%m.%Y %H-%M'))

#Dataclasses - классы для хранения информации

#Enum

#Argparse - передаем аргументы в момент запуска чего-либо, ти значения можно передавать в наш код
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    '-p', '--port',
    help='Порт запуска'
)

#Logging
import logging


logging.basicConfig(
    filename='log.log',
    filemode='a',
    level=logging.DEBUG,
    format=[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
)

logging.error('ошибко')
logging.info('ok')

try:
    4 / 0
except ZeroDivisionError as e:
    logging.error(e)


#Базы данных No SQL
#Реляционнаые и нереляционные.
#Реляционная - таблицы и связи между ними.
#Нереляционная - nosql, этот язык не применяется.

