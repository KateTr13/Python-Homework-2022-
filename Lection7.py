#Классы и объекты

class Person:

    def __init__(self, name: str, age: int): #аргументы в скобках существуют только в рамках ф-ии
#        pass #пишем пасс если нужны аргументы только в рмаках ф-ии
        self.name = name.title() #это атрибуты объекта, характеристики vasya
        self.age = age

    def birthday(self):
        self.age += 1

    @classmethod
    def change_city(cls, city):
        cls.city = new_city.title

    @staticmethod
    def multiply(a, b):
        return a * b

vasya = Person('vasya', 25)
petya = Person('petya', 46)
print(vasya.name)
print(vasya.age)
vasya.birthday()

#Методы представления (см.предыдущий код)

def __str__(self) -> str:
    return f'{self.name=} {self.age=}'

#Достать атрибут по строковому названию

def __getitem__(self, item):
    return getattr(self, item) #селф и имя в виде строки
#Если надо еще переопределять таким же образом, то
def __setitem__(self, key, value):
    setattr(self, key, value) #сетаттр аккратно, им можно обьявлять несуществующие атрибуты
petya['age'] = 25
print(petya)


def __gt__(self, other): #при сравнении больше чем
    return self.age > other.age

def __ge__(self, other): #больше равно
    return self.age >= other.age

def __lt__(self, other): #меньше
    return self.age < other.age

def __le__(self, other): #меньше либо равно
    return self.age <= other.age

def __eq__(self, other): #сравнение ==
    return self.age == other.age

def __ne__(self, other): # неравно !=
    return self.age != other.age

vasya = Person('vasya', 25, 1500)
petya = Person('petya', 35, 600)
print(vasya == petya)


#Итератор. Менеджер контекста

def __iter__(self): #iter возращает обект
    return self

def __next__(self): #должен вызывать нечто новое
    self.i += 1
    if self.i < len(self.name):
        return self.name[self.i]
    else:
        raise StopIteration

for i in vasya:
    print(i)


#Строки документации

def is_palindrome(text: str) -> bool:
    """

    :param text: текст для проверки
    :return: True если текст палиндром, False если нет
    """
    return text.lower() == text.lower()[::-1]
is_palindrome()


#Классы и объекты

