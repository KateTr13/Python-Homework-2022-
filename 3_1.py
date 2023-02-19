#Заполнить список степенями числа 2 (от 2^1 до 2^n)

text = int(input('Введите число'))
thelist = [2 ** x for x in range(1, text)]
print(thelist)
