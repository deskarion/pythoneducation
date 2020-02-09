#Zadanie 1
my_list = ['one', 4, True, 23.4]
element_list = 0
while element_list < len(my_list):
    print(type(my_list[element_list]))
    element_list += 1

#zadanie2
my_range = int(input("Введите значение количества элементов списка от 0  "))
new_spisok = list(range(my_range))
print(new_spisok)
j = 0
for i in range(int(len(new_spisok) / 2)):
    new_spisok[j], new_spisok[j + 1] = new_spisok[j + 1], new_spisok[j]
    j += 2
print(new_spisok)

#zadanie3

#Вариант 1
seasons = dict({'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)})

month = int(input('Введите номер месяца: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)
#Вариант 2

month_list = int(input('Введите номер месяца: '))
if month_list == 1 or month_list == 2 or month_list == 12:
    print ('Зима')
elif month_list == 3 or month_list == 4 or month_list == 5:
    print ('Весна')
elif month_list == 6 or month_list == 7 or month_list == 8:
    print ('Лето')
elif month_list == 9 or month_list == 10 or month_list == 11:
    print ('Осень')
else:
    print ('Неправильный месяц')

#zadanie4

my_dict = input(str("Введите через пробел список"))
numbers = 1
for i in my_dict.split(' '):
    print(numbers,i[0:10])
    numbers = numbers + 1

#zadanie5

nature_list = [7, 5, 3, 3, 2]
new_symbol = int(input('Введите число рейтинга'))
nature_list.append(new_symbol)
nature_list.sort(reverse=True)
print(nature_list)
