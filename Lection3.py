text = 'hello\tworld'
text = text.expandtabs(10)
print(text)

text = '----hello----'
print(text.lstrip('-'))

text = 'hello'
print(text.removeprefix('he'))

text = 'world'
print(text.center(10, '_'))

text = 'world'
print(text.zfill(20))

text = 'hello'
print(text.ljust(10, '_'))

#Oper

print(bin(10))
print(bin(12))

print(10 & 12)

print(~15)

text = 'hello'
print(text[2])
print(text[~2])

print(bin(10))
print(bin(10 << 3))

text = 'hello world'
print('world' in text)

a = 5
b = 5
print(a is b)

#Collections

text = 'hello world'
symbols = list(text)
print(symbols)

symbols[text]

numbers = [i for i in range(10)]
print(numbers)
#list comprehensions

numbers = [1, 2, 3]
print(numbers[2])
#print[2] = 'hello'
# не только достать но и заменить

numbers = [2, 3]
number = numbers.pop(2)
#вырезалось из списка и поместилось в переменную. Удаление по индексу

numbers = [2, 3]
numbers.remove('hello')
print(numbers)
#удаляет первое значение которое равно переданному значению

#adding
numbers = [1, 2, 4]
numbers.append([6,7])

numbers = [1, 3]
numbers.sort(reverse=True)
print(numbers)
#сортировка


#Кортежи

numbers = (1, 2, 3, 4, 5, 6, [7, 8, 9])
numbers[6].append(0)
print(numbers)
#поиск по кортежам происходит быстрее чем по спискам. Изменить список внутри кортежа можно, потому что там ссылка на коллекцию)

#Множества
text = 'hello world'
print(set(text))

#Dictionary
user = {
    'name': 'Alex',
    'age': 34
}
user['name'] = Pavel
print(user)
#можно обратиться по несуществущему ключу чтобы обьявить его (добавить)
print(user['phone number'])
print(user.get('key')) #получение значения по ключу, если такого не то вернется зачение по умолчанию

#update
user = {
    'name': 'alex',
    'age': 34
}
new_data = {
    'name': 'pavel',
    'city': 'minsk'
}
new_user = user | new_data
print(user)

father_age = int(input())
son_age = int(input())
result = father_age - son_age * 2
print(result)

number = input()
first = int(number[0])
second - int(number[1])
third = int(number[2])
print(first + second +third)










