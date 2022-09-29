#Вывести первые N чисел кратные M и больше K

Number = int(input('Enter numberN'))
Mult = int(input('Enter numberM'))
K_lesser = int(input('Enter numberK'))
numbers = []
while Number:
      if not K_lesser % Mult:
          numbers.append(K_lesser)
          Number -= 1
      K_lesser += 1
print(numbers)





