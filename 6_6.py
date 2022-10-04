#Дан список рандомных чисел, необходимо отсортировать его в виде, сначала четные, потом нечётны

numbers = [1, 6, 9, 11, 5, 34, 7, 56, 78]
for number in numbers:
    if number % 2:
        continue
    print(number)
for number in numbers:
    if not number % 2:
        continue
    print(number)


#numbers = [1, 2, 3, 5, 6, 7, 34, 67, 56, 98, 123, 456]
#numbers = list(filter(lambda x: x % 2, numbers))
#print(numbers)