#Zadanie1
a = int(input('Ввести первое число'))
b = int(input('Ввести второе число'))
def first_func(a, b):
    try:
      return (a / b)
    except ZeroDivisionError:
       return 'На ноль делить нельзя'
print(first_func(a,b))
#zadanie2
def second_func(name, family, year, country, email, phone) :
    print(f"name - {name}; family - {family}; year - {year}; country - {country}; email - {email}; phone - {phone}")
second_func(name=input("Введите имя"),
            family=input("Введите фамилию"),
            year=input("Введите возраст"),
            country=input("Введите город"),
            email=input("Введите мейл"),
            phone=input("Введите номер телефона"))
#zadanie3

def next_func(elem_1, elem_2, elem_3):
    min_elem = [elem_1, elem_2, elem_3]
    min_elem.remove(min(elem_1, elem_2, elem_3))
    return print(sum(min_elem))
next_func(76,23, 10)

#zadanie4
#variant1
def my_func(x, y):
    return x ** y
print(my_func(5, -2))
#variant2
def my_func2(x, y):
    step = 1
    for i in range(abs(y)):
        step *= x
        result = 1/step
    return result
my_func2(5, -5)
#zadanie5
def exe_5():
    res = 0
    while True:
        numbers = input('Для вывода суммы введите ентер, для выхода "`" ').split()
        for i in numbers:
            try:
                if i == '``':
                    print(f'Сумма {res}. Выход')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Нажмите ентер или ` для выхода')
        print(f'Сумма {res}')
#zadanie6
# Не осилил =( Прошу подробно разобрать на уроке.