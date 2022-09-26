# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры

text = int(input())
see = {i: {'name': input(), 'email': input()} for i in range(0, text)}
print(see)




n = int(input('n: '))
users = {
    i: {
        'name': input(f'{i} name: '),
        'email': input(f'{i} email: ')
    } for i in range(n)
}
print(users)