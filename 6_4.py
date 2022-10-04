#Дан список содержащий в себе различные типы данных, отфильтровать таким
#образом, чтобы остались только строки, использование дополнительного списка
#незаконно

the_list = [1, 3, 'word', 'dog', 5, 43, 'banana']
result = [i for i in the_list if isinstance(i, str)]
print(result)

#the_list = [1, 3, 'word', 'dog', 5, 43, 'banana']
#new_result = filter(lambda i: isinstance(i, str), the_list)
#print(list(new_result))

#the_list = [1, 3, 'word', 'dog', 5, 43, 'banana']
#new_list = list() #еще один список
#for i in the_list:
#    if isinstance(i, str):
#        new_list.append(i)
#print(new_list)


