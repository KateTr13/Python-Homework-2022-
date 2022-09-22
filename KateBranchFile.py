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
#удаляет первое значение




