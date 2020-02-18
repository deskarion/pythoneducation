#Zadanie1
from sys import argv

call_hour, pay_hour, prize = argv

pay = int(call_hour*pay_hour+pize)
print("Заработная плата сотрудника составляет: ", pay)

#zadanie2
my_list = [10, 4, 6, 8]
new_list = []
print(f"Исходный список: {my_list}")
for i in range(1, len(my_list)):
   if int(my_list[i])>int(my_list[i-1]):
       new_list.append(my_list[i])
print(f"Новый список: {new_list}")
#zadanie3

my_result = [el for el in range(20, 240) if (el % 20 == 0)]

#zadanie4

list_big = [2, 4, 6, 6, 8, 9, 9]
from collections import Counter
data= Counter(list_big)
list_litle = list(data)
print(list_litle)

#zadanie5
from functools import reduce
generation_list = [el for el in range(100, 1000) if (el % 2 == 0)]
print(generation_list)
sum_all = reduce(lambda x, y: x + y, generation_list)
print(sum_all)

#zadanie6
#1
a = int(input("Ввести число"))
from itertools import count
for i in count(a):
 print(i)

#2

List_date = [3, 5, 6, 8, 9, 10]
from itertools import cycle
count = 0
for item in cycle(List_date):
    print(item)
    count += 1

#zadanie7

import random
n = random.randint(0, 15)
def fibo_gen(n):
    factorial = 1
    for el in range(1, n +1):
        factorial *= el
        yield el