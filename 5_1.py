# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

#Десятичное в двоичное
number = int(input())
check = ''
while number > 0:
    check = str(number % 2) + check
    number = number // 2
print(check)


