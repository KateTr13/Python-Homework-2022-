text = '''
iPhone 14 Pro Max

ru from 1 1800

ru from 5 1700

en from 1 1600

iPhone 14 Pro

ru from 50 1500

en from 5 1400

en from 20 1300
'''

text = text.replace('From ', 'From_')
text = list(filter(lambda x: x, text.split('\n')))
countries = ['ru', 'en']
data = {}
flag = ''
for line in text:
    if line[:2] not in countries: #лайн до второго символа (первых два)
        data[line] = {} #в дата обьявляем строку как ключ с вложенным словарем
        flag = line
    else:
        line = line.split() #мы избавились от пробела в flag, теперь всего триэ лемента: цена, страна, количество
        if line[0] not in data[flag]: #если во вложенном словаре нет к устройству такой страны
            data[flag] = {line[0]: {line[1]: int(line[2])}} #в дата флаг определяем вложенный словарь у которого ключом будет страна со значением "сложенный словарь" где ключом будет флаг1. то есть from 10' или 'from 20' а значением для него флаг2. т.е. цена
        else: #если страна уже есть
            data[flag][line[0]].update({line[1]: int(line[2])})




print(data)

