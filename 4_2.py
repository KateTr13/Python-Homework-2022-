# Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число

try:
    Number1 = int(input('Введите первое число'))
    Action = input('Введите действие (+, -, /, *)')
    Number2 = int(input('Введите второе число'))
    if Action == '+':
        print(Number1+Number2)
    elif Action == '-':
        print(Number1-Number2)
    elif Action == '/':
        print(Number1/Number2)
    elif Action == '*':
        print(Number1*Number2)
except ValueError:
    print('Это не символ/Это не число')
except Exception:
    print('Попробуйте еще раз')


