#Дан словарь словарей, ключ внешнего словаря - id пользователя, значение -
#словарь с данными о пользователе (имя, фамилия, телефон, почта), вывести
#имена тех, у кого не указана почта (нет ключа email или значение этого ключа -
#пустая строка)

dictionary = {'dictionary1': {'name': 'Anton Bozensky', 'phone': '+375298760543', 'email': 'anton@gmail.com'},
              'dictionary2': {'name': 'Innokentiy Sobolevsky', 'phone': '+375298760423', 'email': 'innokentiy@gmail.com'},
              'dictionary3': {'name': 'Maria Lotz', 'phone': '+37523876542'}
}

for key, val in dictionary.items():
    if not val.get("email"):
        print(val.get("name"))




