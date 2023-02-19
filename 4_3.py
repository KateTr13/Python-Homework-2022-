# Вывести четные числа от 2 до N по 5 в строку

n = int(input())
for i in range(2, n+1, 10):
    for j in range(i, i+9, 2):
        if j > n:
            break
        print(j, end=' ')
    print()


