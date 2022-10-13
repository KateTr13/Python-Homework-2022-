# Операторы ветвления, циклы, исключения

number = int(input())
if number % 2:
    print('odd')
elif number < 0:
    print('lower than 0')
else:
    print('even')

...
number = int(input())
if number % 2:
    is_even = 'No'
else:
    is_venv = 'Yes'
is_even = 'No' if number % 2 else 'Yes'

...
number = int(input())
numbers = [i for i in range(number) if i % 5]
print(numbers)

...
x = True
y = False
z = False
if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)

#Подсчитать буквы во фразе
text = 'hello world'
for i, j in enumerate(text):
    print(i, j)
...
data = {
    'name': 'vasua',
    'email': 'vasua@info.com',
    'city': 'Minsk'
}
for key in data:
    print(key)

#for val in data.values():
#    print(val)

#for val in data.items():
#    print(key, val)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number % 2:
        continue
    print(number)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 6:
        break
    print(number)
else:
    print('finish')

#Заполнить список четными числами в квадрате от 1 до n
n = int(input())
numbers = []
for i in range(2, n, 2):
    numbers.append(i**2)
# numbers = [i**2 for i in range (2, n, 2) if not i % 2]
print(numbers)

#Цикл while

#Спрашивать у пользователя инфо с клавиатуры пока он не введет число
number = input('enter number')
while not number.isdigit():
    number = input('try again')

#В строке определить количество не пересекающихся пар одинаковых символов
text = input()
c = 0
i = 0
while i < len(text) - 1:
    if text[i] == text[i+1]:
        c += 1
        i += 1
    i +=1
print(c)

#Дано целое положительное число n, вывести максимальную степень числа 2, в котором 2 не превышает
# N=34, 2^5=32 (2 в степени5), 32<=34
n = int(input()) #34
i = 0
while 2 ** i <= n: #i == 6
    i += 1
print(i -1)

#Ошибки

try:
    a = int(input())
    b = int(input())
    c = a / b
except ValueError:
    print('вы ввели не число')
except Exception:
    print('общее действие')
except ZeroDivisionError:
    b = 1
    c = a / b
else:
    print('ошибок нет')


def is_palindrome(text):
    if not isinstance(text, str):
        raise TypeError('argument `text` must be string')
    return text.lower() == text.lower()[::-1]

