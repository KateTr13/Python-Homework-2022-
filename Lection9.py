#Работа с файлами
import csv

#абсолютный путь - как в винде, от корня к файлу. Относительный  - относительно проекта (где в проекте
# лежит файл)
file = open('KatePythonStart/Lection9.py', 'r', encoding='utf-8')

file.close()
# нужно будет закрыть файл. Иначе будет висеть в оперативной памяти

# with.. as открывает а потом сам закрывает файл
with file = open('KatePythonStart/Lection9.py', 'r', encoding='utf-8') as file:
    pass

with file = open('KatePythonStart/Lection9.py', 'r', encoding='utf-8') as file, open() as file2:

#Чтение и запись
with file = open('KatePythonStart / Lection9.py', 'r', encoding='utf-8') as file:
    text = file.read()
print(text)

with file = open('KatePythonStart / Lection9.py', 'r', encoding='utf-8') as file:
    print(file.readline())
#readline итератор который возвращает каждый раз по одной строке

with file = open('KatePythonStart / Lection9.py', 'r', encoding='utf-8') as file:
    lines = file.readlines()
#   lines = [line.strip() for line in file]
print(lines)     # readlines считывает список строк

with file = open('KatePythonStart / Lection9.py', 'r', encoding='utf-8') as file:
    lines = []
    for line in file:
        if line.strip().isdigit():
            lines.append(int(line.strip()))
print(lines)

#Запись
text = ['text', 'is', 'here']
with file = open('KatePythonStart / Lection9.py', 'w', encoding='utf-8') as file:
    file.write('\n'.join(text))
#так как это список строк то обьединяю через джоин с любым указанным разделителем и записываю в файл
#r чтение, w перезаписать файл, a добавить новое к содержимому файла

#Дан файл с числами через запятую (могут быть пробелы)
# прочитать файл в список списков чисел (int)
with open('path', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip().replace(' ', '') #убираем пробелы
#        numbers = line.split(',') #делим строку на части по запятым
#намберс теперь нужно из списка строк к списку чисел
        numbers = list(map(int, line.split(',')))
        print(numbers)
#теперь списки чисел нужно собрать в один список
    lines = []
    for line in file:
        line = line.strip().replace(' ', '')
        numbers = list(map(int, line.split(',')))
        lines.append(numbers)
print(lines)

#Дан файл с текстом, нужно сказать сколько слов и букв в в каждой строке данного файла
#Результат аписать в файл output.txt в формате: в 1 строке n слов и n букв

with open('path', 'r', encoding='utf-8') as file, open('output.txt', 'w', encoding='utf-8'):
    for line in file:
        space_count = line.count(' ')
        if space_count:
            space_count += 1 #считаем пробелы и переходим к следующему
        print(space_count)
        letter_count = 0
        for letter in line.strip():
            if letter.isalpha():
                letter_count += 1
        result.append(
            f'B {i} строке {space_count} слов и {letter_count} букв'
        )
        i += 1 #для перехода со строки на строку
#print(result)
    file.write('\n'.join(result)) #\n обьединяет строки


#JSON

import json
#создаем json файл. Открываем.
with open('input.json', 'r', encoding='utf-8') as file:
    print(file.read())
#Если хочется превратить содержимое файла в полноценный словарь:
print(data)
print(type(data))
#Если содержимое файла не виде словаря а в виде строки:
    data = json.loads(file.read()) #метод рид вернет строку с json, лоадс переделает это

#Записать инфо в json файл
data = {
    'name': 'pavel',
    'age': 56
}
with open('input.json', 'r', encoding='utf-8') as file:
    json.dump(data, file, indent=2) #indent=2 формтаирует чтобы все было не в одну строку, будет словарь


#Pydantic

data = {
    'name': 'pavel',
    'age': 56,
    'is_human': True,
    'languages': ['ru', 'en']
}

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    age: int
    is_human: bool
    languages: list[str]

user = User(**user)
print(user.age)
print(user.languages[1])


#CSV

class User(BaseModel):
    name: str
    age: int
    is_human: bool
    languages: list[str]
#создаем csv файл, первая строка это заголовок и будет ключами если будет считывать как словарь
with open('users.csv', 'r', encoding='utf-8') as file:
    data = csv.reader(file, delimeter=';') #delimeter разделит слипшийся текст по знакму в указанному в кавычках
    for user in data:
        print(user)
#однако при изменении осн.файла вся логика лсоваемся, поэтому вместо
# csv.reader лучше использовать csv.DictReader. Первую строку видит как ключи и порядок уже не важен


class User(BaseModel):
    name: str
    age: int
    email: EmailStr

data = []

with open('users.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimeter=';')
    for user in reader:
        try:
            data.append(User(**user))
        except Exception as e:
            print(e)
            print(user, 'is not valid')
print(data)


#Pandas
# Excel
#Для анализа данных и работы с таблицами

users = {
    'name': ['alex', 'pavel', 'maria'],
    'age': [13, 67, 54],
    'email': ['info1@gmail.com', 'info2@gmail.com', 'info3@gmail.com']
}
from pandas import DataFrame, read_excel

frame = DataFrame(users)
print(frame[frame['age'] > 23])


frame = DataFrame(users)
for user in frame.loc:
    print(user['email'])


frame.to_excel('users.xlsx', sheet_name='users', index=False)


frame = read_excel('users.xlsx', sheet_name='users')
print(frame)








