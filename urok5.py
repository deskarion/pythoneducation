#Zadanie1
f = open("file.txt", "w")
while True:
    s = input()
    if s == '': break
    f.write(s+'\n')
f.close()

#zadanie2
lines = 0
words = 0
for line in open("schet.txt", 'r'):
    lines += 1
    flag = 'вне слова'
    for letter in line:
        if letter != ' ' and flag == 'вне слова':
            words += 1
            flag = 'в слове'
        elif letter == ' ':
            flag = 'вне слова'
print("Строк:", lines)
print("Слов:", words)
#zadanie3

with open('man.txt', 'r', encoding='utf-8') as f:
    workers = {}
    for line in f:
        key, value = line.split()
        workers[key] = value
        if int(value) < 20000:
            print(f'{key}: зарплата меньше 20000')


#zadanie4
#Думаю со словарем было бы изящнее, но делал уже под ночь.. В общим правильно на мой взгляд через словарь)
my_f = open("data.txt", "r",encoding='utf-8')
open('data2.txt', 'tw', encoding='utf-8')
while True:
    content = my_f.read(1024)
    print(content)
    out_f = open("data2.txt", "r+")
    content = content.replace("One", "Один")
    content = content.replace("Two", "Два")
    content = content.replace("Three", "Три")
    content = content.replace("Four", "Четыре")
    content = content.replace("Five", "Пять")
    out_f.writelines(content)
    out_f.close()
    if not content:
        break

#zadanie5
with open('summa.txt','r') as file:
    s = file.readline()
    s = list(map(int, s.split()))
    print(sum(s))

#zadanie6 и 7 неуспел, но в общим то решение видится через словари+ работа с файлами