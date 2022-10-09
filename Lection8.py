#ООП, объектно ориентированное программирование
import email

import self as self


class User(object):
    def __init__(self, name: str, email: str) -> None:
        self.email = email.lower()
        self.name = name.title()

    def __str__(self):
        return f'User: {self.name = } {self.email}'

class Manager(User):

    def __init__(self, name: str, email: str, age: int) -> None:
        super().__init__(name,email) #ф-я супер позволяет вызывать метод или атрибут родительского класса
        self.age = age

vasya = Manager('vasya', 'info@gmail.com', 34)
print(vasya)


#Множественное наследование

class Manager(User):

    def __init__(self, name: str, email: str, age: int) -> None:
        super().__init__(name,email) #ф-я супер позволяет вызывать метод или атрибут родительского класса
        self.age = age

class Boss(Manager):
    def __init__(self, name: str, email: str, age: int) -> None:
        super().__init__(name, email, age) #если здесь обратиться к атрибуту или еще чему-то то обращение будет к Менеджер (от которого идет Босс)

vasya = Manager('vasya', 'info@gmail.com', 34)
print(vasya)


#Наследование

class A:
    def __init__(self):
        self.name = 'A'

class B:
    def __init__(self):
        self.name = 'B'

class C(A, B):
    def __init__(self):
        super().__init__()

c = C()
print(c.name)


#Полиморфизм

class Manager(User):

    def __init__(self, name: str, email: str, age: int) -> None:
        super().__init__(name,email) #ф-я супер позволяет вызывать метод или атрибут родительского класса
        self.age = age

    def __str__(self):
        return f'Manager': {self.name=} {self.email=} {self.age=}'
#Переопределен родительский метод. Вызывая метод стр у дочернего класса то будет вызываться метод из этого дочернего класса, не из родительского
vasya = Manager('vasya', 'info@gmail.com', 34)
print(vasya)

#Сокрытие
#Внутри родительского класса есть метод который нам не нужен
    def foo(self):
        print('foo')
#Скрываем, теперь в дочернем классе при вызове этого метода будет ошибка, а в родительском метод будет на месте
    def foo(self):
        raise AttributeError

#Утиная типизация

class A:
#    def get_a(self):
    def get(self):
        print('get A')

class B:
#    def get_b(self):
    def get(self):
        print('Get B')

a = A()
b = B()

def foo(c: object):
#    if isinstance(c, A):
#        c.get_a()
#    elif isinstance(c, B):
#        c.get_b()
    c.get()

foo(a)
foo(b)
#Если использовать закомменченное то пришлось бы конкретизировать что именно мы вызываем. Но если цтиная типизация то не важно оббьект какого
# класса. Мы уверены что там есть метод get, этого достаточно.

#В ПИТОНЕ ИНТЕРФЕЙСОВ НЕТ!

#Квалификаторы доступа.
#public можем менять , private _ можем менять но не надо, protected __ не можем менять

class A:
    def __init__(self):
        self.__name = '1234 5678 9012 4567'

    @property
    def name(self):
        return self.__name[-4:]

    @name_setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('argument 'value' must be a string')
        in not value.replace(' ', '').isdigit():
            raise ValueError('argument value must be digit')
        self.__name = value

a = A()
print(a.name)
#пользователь может изменить атрибут, но при условии что значение которое он вводит пройдет проверки


#Абстрактные классы

from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def change_name(self, value):
        pass

vasya = User('vasya')
#Нелья создать экземпляр такого класса. Это не полноценный класс а набросок, чертеж. От абстр.класса можно только наследоваться:
class MyUser(User):

    def __init__(self, name):
        super().__init__(name)
#С этим нельзя работать пока не определим абстрактный метод в родительском классе.
    def change_name(self, value):
        self.name = value

vasya = MyUser('vasya')


#Dataclasses
# Классы для хранения информации, в противовес именованному кортежу и т.д.
from dataclass import dataclass

@dataclass
class User:
    name: str #Нужно всегда писать аннотацию типа
    age: int
    email: str

vasya = User(name='vasya', age=34, email='info@gmail.com')
print(vasya.name)
print(vasya.email)
print(vasya.age)
print(vasya.__dict__) #превратить вывод в словарь


#Enum
#"Именованный список значений", нужен для повышения читаемости
from enum import Enum

class Status(int, Enum):
    Unpaid: int = 1
    Paid: int = 2
    Revoke: int = 3
    Cancelled: int = 4

status = 2
if status == Status.Paid:
    print('оплата прошла успешно')

from enum import IntEnum

statuses = [('Unpaid', 1), ('Paid', 2), ('Revoke', 3), ('Cancelled', 4)]
Status = IntEnum('Status', statuses)
if 2 == Status.Paid:
    print('OK')


#Метаклассы

def __str__(self):
    return f'{self.name=} {self.age+}'

def birthday(self):
    self.age = +1

User = type('User', (), {'name': None, 'age': None, 'birthday': birthday, __str__})

vasya = User()
vasya.name = 'vasya'
vasya.age = 34
vasya.birthday()
print(vasya)

#Реализовать метод filter, принимающий строку и возвращающий тру или фолс если это строка данного обьекта
class CallbackData(object):

    def __init__(self, prefix: str, *args) -> None:
        self.prefix = prefix
        self.agrs = tuple(map(str, args))

    def new(self, *args: tuple) -> str:
        if len(args) != len(self.args):
            raise ValueError
        return self.prefix + ':' + ':'.join(map(str, args))

user_cb = CallbackData('user', 'target', 'action', 'id')
print(user_cb.new('category', 'all', 0))
#метод нью строку возвращает

#Реализовать метод serialize возвращающий список списков словарей

class InlineButton(object):

    def __init__(self, text: str, callback_data: str) -> None:
        if not isinstance(text, str):
            raise TypeError('argument 'text' must be string')
            if not isinstance(callback_data, str):
                raise TypeError('argument 'text' must be string')

        self.text = text
        self.callback_data = callback_data

    def dict(self) -> dict:
        return {'text': self.text, 'callback_data': self.callback_data} #будет возвращаться словарь

class InlineMarkup(object):
    def __init__(self, inline_keyboard: list) -> None:
        if not isinstance(inline_keyboard, list):
            raise TypeError('argument 'inline_keyboard' must be list')

        for line in inline_keyboard:
            if not isinstance(line, list):
                raise TypeError
        for button in line:
            if not isinstance(button, InlineButton):
                raise TypeError

        self.inline_keyboard = inline_keyboard

    def dict(self) -> List[List[dict]]:
        markup = []
        for line in self.inline_leyboard:
            lst = []
            for button in line:
                lst.append(button.dict())
            markup.append(lst)
        return markup

buttons = [InlineButton(text='text', callback_data='data') for i in range(10)]
markup = InlineMarkup(inline_keyboard=[buttons])
print(markup.dict())



