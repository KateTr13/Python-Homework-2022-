#ФУНКЦИИ И АРГУМЕНТЫ

LIFO - last in first out #убираем последнее в списке
FIFO - frst in first out #убираем первое в списке

def foo():
    print('foo')
foo()

...

text = 'hello'
def is_palindrome(text):
    print(text.lower() == text.lower()[::-1])
res1 = is_palindrome('шалаш')
res2 = is_palindrome('вапукпукп')
print(res)

...
#Аргументы функции

def multiply(a, b):
    return a * b
print(multiply(4, 8)) # а и б позиционные, а это 4 а б это 8 и местами их не поменять. Но можно сделать
# (b=8 a=4)

#Неопределенное количество аргументов *args

def my_sum(*args):
    print(args)
my_sum(1, 4, 6, 8, 34)

def my_sum(*args):
    print(sum(args))
my_sum(1, 4, 6, 8, 34)

#Kwargs, произвольноое количество
def my_sum(**kwargs):
    print(kwargs)
my_sum(a=1, b=4, c=6, d=8, e=34)

#Порядок указания!!!
1.Позиционные аргументы
2. Аргументы со значением по умолчанию (имя=значение)
3. *args
4. Аргументы, которые должны передаваться только по ключевым словам (имя=значение)
5. **kwargs

#Области видимости, LEGB когда интерпретатор ищет переменные
a = 5

def foo():
    a = 4 #интерпретатор найдет эту а
    def bar():
        print(a)
///
def foo():
    a = 4 #интерпретоатор найдет эту а
    def bar():
        global a
        print(a)

#Locals Globals
a = 5

print(globals().get('a'))

#Lambda лямбда функция - анонимная функция выраженная одним действием
def multiply(a, b):
    return a * b
#равно
multiply = lambda a, b: a * b
print(multiply(4,5))

#Функция map  принимает два аргумента: функцию и последовательность
numbers = [1, 2, 4, 6, 7]
numbers = map(int, numbers) #к каждому элементу коллекции numbers независимо друг от друга будет применена
#функция int
print(numbers)

#Filter функция которая принимает два аргумента: функцию и последовательность. Фильтрует указанную
# последовательность на основании указанной функции
numbers = [1, 2, 4, 5, 7, 8, 9,]
numbers = list(filter(lambda x: x % 3, numbers))
print(numbers) #числа которые не кратны трем
#равно
result = []
for x in numbers:
    if x % 3:
        result.append(x)

data = {
    'a':1,
    'b':2,
    'c':3,
}
result = dict(list(filter(lambda x: x[1] % 2, data,items())))
print(result)

#Функция zip  - обьединяет в кортежи элементы из последователньостей переданных в качестве аргументов.
#Выключается когда достигнут конец самой короткой последовательности
#Еще есть zip_longest
text = 'ergergeg'
numbers = [1, 3, 6, 8]
tup = (True, False)

result = list(zip(text, numbers, tup))
print(result)

#Вводится многозначное число, используя map, lambda сформировать список цифр введенного числа
#чтобы все цифры в получившемся списке были int
number = input()
numbers = list(map(lambda x: int(x), number))
#Вводится текст из нескольких предложений, кжадое предложение разбито '.'. Сколько слов в каждом
#предложении
text = input().split('.')
word_count = list(map(lambda x: x.count(' ') +1, text))
print(word_count)
#В строке все что угодно, нужно просуммировать цифры из этой строки
text = 'ergret45yrtbtrhrt45y54'
numbers = filter(lambda x: x.isdigit(), text)
numbers = map(int, numbers)
print(sum(numbers))
#Вводится число, суммировать цифры до тех пор пока не поулчится однозначное число
def get_numbers():
    for i in range(2):
        yield 1

a = get_numbers()
print(next(a))
print(next(a))

#Генератор - класс функций который помогает создавать свои итераторы (последователньости).
# Как ф-я, но вместо return будет yield. yield может быть несколько
def get_numbers():
    for i in range(2)
        yield i

print(next(a))
print('основной поток')
print(next(a))
print('основной поток')

#Рекурсия - ф-я кот.содержит код вызова самой себя для создания циклического процесса.
numbers = [1, 3, 6 [5,7,8 [6, 8, 9]]]
def recursive_sum(numbers):
    result = 1
    fir i in numbers:
    if isinstance(i, (int, float)):
        result *= i
    elif isinstance(i, (list, tuple)):
        result = recursive_sum(i)
    return result

print(recursive_sum(numbers))

#Замыкание. Ф-я которая динамически генерируется другой ф-ей и они обе могут изменять и запоминать
# значения переменных, созданных вне функции. Внешняя ф-я возвращает ссылку на вложенную ф-ю.
def foo(a):
    def bar(b):
        return a * b
    return bar

a = foo(5)
b = foo(4)
print(a)
print(a(4))
print(a(6))
print(a(7))

#Декоратор
def my_decorator(func): #ф-я поступает как аргумент на внешнюю ф-ию(func)
    def wrapper(a, b): #а и б поступают не напрямую а через враппер. Получается предобработка
        res = func(a, b) #а и б сначала попадут во враппер и к ним добавится +=1, и в осн. ф-ю попадут
        a += 1 #не 4 и 5 а 5 и 6
        b += 1
        return res
    return wrapper

@my_decorator
def multiply(a, b):
    return a * b

print(multiply(4, 5))

#Аннотация типов
a: int = 5
text: str = 'hello'

def multiply(a: int, b: int) -> int:
    return a * b

multiply()









