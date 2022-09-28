# Вывести четные числа от 2 до N по 5 в строку

N_numbers = int(input())
numbers = [i for i in range(2, N_numbers) if i % 2 == 0]
numbers = str(numbers)
