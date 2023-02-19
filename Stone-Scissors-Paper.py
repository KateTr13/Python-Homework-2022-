
try:
    Player1 = input('Первый игрок. Выберите из: камень, ножницы, бумага')
    Player2 = input('Второй игрок. Выберите из: камень, ножницы, бумага')
    if Player1 == 'камень' and Player2 == 'камень':
            print('ничья')
    if Player1 == 'камень' and Player2 == 'бумага':
                print('Камень побеждает')
    if Player1 == 'камень' and Player2 == 'ножницы':
                print('Камень побеждает')
    if Player1 == 'ножницы' and Player2 == 'камень':
                print('Камень побеждает')
    if Player1 == 'ножницы' and Player2 == 'бумага':
                print('Ножницы побеждают')
    if Player1 == 'ножницы' and Player2 == 'ножницы':
                print('Ничья')
    if Player1 == 'ножницы' and Player2 == 'камень':
                print('Камень побеждает')
    if Player1 == 'бумага' and Player2 == 'камень':
                print('Камень побеждает')
    if Player1 == 'бумага' and  Player2 == 'ножницы':
                print('Ножницы побеждают')
    if Player1 == 'бумага' and Player2 == 'бумага':
                print('Ничья')
except ValueError:
    print('Это не символ/Это не число')
except Exception:
    print('Попробуйте еще раз')
