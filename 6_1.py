# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

#Десятичное в двоичное
#number = int(input())
#check = ''
#while number > 0:
#    check = str(number % 2) + check
#    number = number // 2
#print(check)


def decimal_to_bunary(number: int) -> str:
    binary = ''
    while number > 1:
        binary += str(number % 2)
        number = //= 2
    binary += str(number)
    return binary[::-1]


def binary_to_decimal(number: str) -> int:
    number = 0
    for i in binary:
        number *= 2
        number += int(i)
    return(number)

return(binary_to_decimal('1111'))



