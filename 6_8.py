#Дан словарь, ключ - Название страны, значение - список городов, на вход
#поступает город, необходимо сказать из какой он страны

city = input()
country_dict = {
    'Belarus': ['Minsk', 'Grodno', 'Vitebsk'],
    'United Kingdom': ['London', 'Aberdeen', 'Bradford'],
    'United Arab Emirates': ['Sharjah', 'Al Ain', 'Ajman']
}
for k, v in country_dict.items():
#       if city in v:
#        print(k)
        for i in v:
            if city == i:
                print(k)


