'''
text = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
s = [i for i in text. split()]
base = {}
for i in s:
    base[i] = base.get(i, 0) + 1
print(base)

for i in base:
    if base[i] == max(base.values()):
        base[i] = base[i]

res = sorted(base)
print(res)
result = {0: res[0]}
print(result)
'''
import random
import zipimport

'''


MondayStudents = {683943897: "Tanya.py", 811476623: "Georgie.py", 826004697: 'Nikita.py'}
TuesdayStudents = {1949653479: "Yanina.py", 1208542295: "Sasha.py", 1537718492: "Aleksandr.py"}
ThursdayStudents = {1949653479: "Yanina.py", 1477701439: "Valeria.py", 811476623: "Georgie.py", 799740089: "Bulat.py", 1537718492: "Aleksandr.py"}
FridayStudents = {1314375732: "Vasiliy.py", 644645774: "Stasya.py", 719571990: "Stepan.py", 1029532016: 'Maria.py'}
SaturdayStudents = {871237277: "Vladek.py"}

Students = MondayStudents | ThursdayStudents | ThursdayStudents | FridayStudents | SaturdayStudents
print(Students)

for i in Students:
    print(type(i))

print(Students[1029532016])
'''

'''
try:
    print(5 / 0)
except ZeroDivisionError:
    print("На ноль делить нельзя")

x = 4
NumberForSimple = 4
sumь = x + NumberForSimple
'''

'''
N = [0,0,0,1,0,1,0,1]
while N[0] == 0:
    del N[0]
print(N)
'''

'''
*!*!*?
3
а: 3
н: 2
с: 1
'''

# ПИНЧУК ЕГОР ПЕТРОВИЧ	2.9.1994	ОБЛ. НОВОСИБИРСКАЯ, Г. НОВОСИБИРСК, ПЕР. САДОВЫЙ, ДОМ 3	5014316390	ОУФМС РОССИИ ПО НОВОСИБИРСКОЙ ОБЛ. В СОВЕТСКОМ Р-НЕ
'''
f = open('Priziv1volna.txt', 'r')
s = f.readlines()
print(len(s))


for i in s:
    if 'ОБЛ. НОВОСИБИРСКАЯ, Г. НОВОСИБИРСК' in i:
        if 'БАБЕШКО' in i:
            print(i)
        #if 'ОУФМС РОССИИ ПО НОВОСИБИРСКОЙ ОБЛ. В СОВЕТСКОМ Р-НЕ' in i:
            #print(i)
'''

'''
student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]



result = []


for i in range(0, len(student_names)):
    M = {}
    temp = {}
    temp[student_names[i]] = student_grades[i]
    M[student_ids[i]] = temp
    result.append(M)
print(result)
'''

# Sample Input 1:
#
# 5
# my_pycode.exe W X
# log_n X W R
# ave R
# lucky_m W R
# dnsss.py W
# 6
# execute ave
# read dnsss.py
# write log_n
# execute log_n
# read ave
# write my_pycode.exe
# Sample Output 1:
#
# Access denied
# Access denied
# OK
# OK
# OK
# OK


# Дана программа для Редактора:
#
# НАЧАЛО
# ПОКА нашлось (21)
#     заменить (21, 5)
# КОНЕЦ ПОКА
# КОНЕЦ
#
# Исходная строка содержит десять единиц и некоторое количество двоек,
# других цифр нет, точный порядок расположения единиц и двоек неизвестен.
# После выполнения программы получилась строка с суммой цифр 34.
# Какое наименьшее количество двоек могло быть в исходной строке?
'''
3
Светлана Зуева
Аркадий Белых
Борис Боков
'''

'''
import random

n = int(input())

M = []
for i in range(n):
    s = input()
    M.append(s)

N = M.copy()
#print(M)
for i in range(n):
    n1 = random.choice(M)
    n2 = random.choice(N)
    while n1 == n2:
        n1 = random.choice(M)
        n2 = random.choice(N)

    for i in range(len(M)):
        if M[i] == n1:
            del M[i]
            break

    res = n1 + ' - ' + n2
    print(res)
'''

"""
Students = {1208542295: ['Sasha.py', 3200/2],
            799740089: ["Bulat.py", 2280],
            811476623: ["Georgie.py", 3040],  # 2
            1949653479: ['Yanina.py', 4080],  # 2
            826004697: ['Nikita.py', 3040],
            1537718492: ['Aleksandr.py', 5760], # 2
            1314375732: ['Vasiliy.py', 6800/2],
            683943897: ["Tanya.py", 3600],
            871237277: ['Vladek.py', 6800/2],
            1477701439: ["Valeria.py", 3200],
            644645774: ['Stasya.py', 5760/2],
            719571990: ['Stepan.py', 6800/2],
            1029532016: ['Maria.py', 3600],
            1649389148: ['Slava.py', 6800/2],
            789322200: ['Katya.py', 6800/2],
            824782347: ['Daniel', 3600],
            804184353: ['Islam.py', 3600],
            5148819382: ['Tatyana.py', 3600],
            1000000001: ['_______.py', 3600],
            1000000002: ['_______.py', 3600],
            1000000003: ['_______.py', 3600],
            1000000004: ['_______.py', 3600],
            1000000005: ['_______.py', 3600],
            1000000006: ['_______.py', 3600],
            1000000007: ['_______.py', 3600],
            1000000008: ['_______.py', 3600],
            1000000009: ['_______.py', 3600],
            1000000010: ['_______.py', 3600],
            1000000011: ['_______.py', 3600],
            1000000012: ['_______.py', 3600],
            1000000013: ['_______.py', 3600],
            1000000014: ['_______.py', 3600],
            1000000015: ['_______.py', 3600],
            1000000016: ['_______.py', 3600]}


n = len(Students)+3
summ1 = 0
summ2 = 0
for key in Students:
    if Students[key][0] != '_______.py':
        summ1 += Students[key][1]
    summ2 += Students[key][1]
print(summ1, summ2)


print(8*5*3600, 8*5-n)
print(7*5*3600, 7*5-n)
print(6*5*3600, 6*5-n)
"""

'''
import random
import string

n, m = int(input()), int(input())

def generate_password(length):

    flag1 = False
    flag2 = False
    flag3 = False

    numbers = '23456789'
    n = [i for i in numbers]
    letters = 'abcdefghjkmnpqrstuvwxyz'
    l = [i for i in letters]
    LETTERS = 'ABCDEFGHJKMNPQRSTUVWXYZ'
    L = [i for i in LETTERS]

    BadSymbols = 'iIlL0oO1'
    password = ''

    while len(password) != length:
        x = random.randint(1,3)
        if x == 1:
            flag1 = True
            password += random.choice(n)
        if x == 2:
            flag2 = True
            password += random.choice(l)
        if x == 3:
            flag3 = True
            password += random.choice(L)

    if flag1 == True and flag2 == True and flag3 == True:
        print(password)
    else:
        generate_password(length)


def generate_passwords(count, length):
    for i in range(count):
        generate_password(length)

generate_passwords(n, m)
'''

"""
MondayStudents = {811476623: ["Georgie.py", '20:00'], 826004697: ['Nikita.py', '22:00']}

print(f"{MondayStudents[826004697][0]} время урока: {MondayStudents[826004697][1]}")

Students = {}
M = [1,2,3,4 ]
Students[int(M[1])] = [M[2], M[3]]
print(Students)
"""

# Типы данных
x = 4  # переменная - предоставляет доступ к данным (4) по имени (x)
y = 7 / 2
my_list = [1, 2, 3]
# Типы данных переменных
'''
a = 4  # int (integer) - целочисленный тип данных
print(type(a))

b = 4.0  # float (число с плавающей точкой) - по факту дроби
print(7/2, type(7/2))

c = '4', 'Hello', "Как дела?", " "  # str (string) - строковый тип данных, хранит: символы, цифры, буквы, слова ...

h1 = 'Hello'
h2 = 'Tanya'
print(h1 + ' ' + h2)


d1 = True  # bool (boolean) - Булева алгебра или основы математической логики
d2 = False
print(4 > 10)


M = [a, b, c, d1, d2, 3+4, 7/2, '4' * 8, 4 < 10]
for i in M:
    print(i, '  <--->  ', type(i))
'''

# Типы данных коллекций
'''
print()
A = [[1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 'один', 2: 'два', 3: 'три'}]
for i in A:
    print(i, '  <--->  ', type(i))
'''

# Можно ли менять типа данных? Да, можно
# Из int и float можно легко переводить в другие типы данных
# Из str можно переводить в int и float, если строка состоит только лишь из цифр
'''
temp = 5
print(temp, '  <---->  ', type(temp))

temp = str(temp)
print(temp, '  <---->  ', type(temp))

temp = float(temp)
print(temp, '  <---->  ', type(temp))

temp = int(temp)
print(temp, '  <---->  ', type(temp))

print()
A = [1, 2, 3]
print(A, '  <---->  ', type(A))

A = tuple(A)
print(A, '  <---->  ', type(A))

A = set(A)
print(A, '  <---->  ', type(A))

A = list(A)
print(A, '  <---->  ', type(A))
'''

# Ввод с клавиатуры
'''
name = input('Введите переменную name: ')  # просто input() - получает строку с клавиатуры
print('Hello, ' + name + '!')

x = int(input('x: '))
print(x, '  <---->  ', type(x))

y = float(input('y: '))
print(y, '  <---->  ', type(y))
'''

'''
text = input()
symbol = '!,.?-+=:*&^%$##$@'

M = [i for i in text]
print('M: ', M)
A = []
for i in range(0, len(M)):
    if M[i] not in symbol:
        A.append(M[i])
print('А: ', A)
res = ''.join(A)
print('res: ', res)
result = [i for i in res.split()]
print('result: ', result)
'''

# Базова арифметика
'''
a = 7
b = 2

print(f'{a} + {b} = {a + b}\n{a} - {b} = {a - b}\n{a} * {b} = {a * b}')
print()
print(f'Возведение {a} в степень {b}: {a ** b}')
print(f'Корень квадратный от 16: {16 ** (1/2)}')
print(f'Корень кубический от 27: {27 ** (1/3)}')
print('\n')
print(f'Вещественное деление: {a} / {b} = {a / b}\n'
      f'Целая часть от деления (без округления): {a} // {b} = {a // b}\n'
      f'Остаток от деления (от обыкновенной дроби): {a} % {b} = {a % b}')
'''

"""
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n-1)

print(F(2023)/F(2020))
"""

# Тип 6 № 47403
# В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат.
# Черепахе был дан для исполнения следующий алгоритм:
#
# Повтори 4 [Вперёд 12 Направо 90]
# Направо 30
# Повтори 3 [Вперёд 8 Направо 60 Вперёд 8 Направо 120]
#
# Определите, сколько точек с целочисленными координатами будут находиться внутри области,
# ограниченной линией, заданной данным алгоритмом: Повтори 4 [Вперёд 12 Направо 90]
#
# И находиться вне области, ограниченной линией, заданной данным алгоритмом:
# Повтори 3 [Вперёд 8 Направо 60 Вперёд 8 Направо 120].
# Точки на линии учитывать не следует.

# Тип 6 № 47403
'''
import turtle as t  #1
t.left(90)  #2
n = 30  #3

for _ in range(4):  #4
    t.forward(12 * n)  #5
    t.right(90)
t.right(30)
t.color('red') #5
for _ in range(3):
    t.forward(8 * n)
    t.right(60)
    t.forward(8 * n)
    t.right(120)

t.color('blue')
t.pu()  #6
for x in range(13):  #7
    for y in range(13):
        t.goto(x * n, y * n)  #8
        t.dot(3)  #9
t.done()  #10
# Ответ: 73
'''

# Номер 8
'''
print(7 ** 11)
s = 'НИКОЛАЙ'
s2 = 'НИКОЛА'
count = 0
for a1 in s2:
    for a2 in s:
        for a3 in s:
            for a4 in s:
                for a5 in s:
                    for a6 in s:
                        for a7 in s:
                            for a8 in s:
                                for a9 in s:
                                    for a10 in s:
                                        for a11 in s:
                                            temp = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11
                                            if temp.count('И') == 1 and temp.count('О') == 1 and temp.count('А') == 1:
                                                count += 1
print(count)
'''



# def fancy(length, char1='-', char2='*'):
#     return (char1 + char2) * length + char1
#
#
# print(fancy(char2='!'))




# Тип 14 № 27242
'''
# Значение арифметического выражения: 49**6 + 7**19 − 21 — записали в системе счисления с основанием 7.
# Сколько цифр «0» содержится в этой записи?

x = 49**6 + 7**19 - 21
M = []
while x > 0:
    M.append(x % 7)  # .append() - это метод списков: добавление переменной в конец списка
    x //= 7
M.reverse()   # Метод переворачивающий список
print(M, M.count(0))  # метод .count() возвращает кол-во вхождений элемента в список
'''
# Метод - это функция которая направлена на объект определенного типа данных


# Тип 8 № 13737
'''
# Все 4-буквенные слова, составленные из букв Д, Е, К, О, Р, записаны в алфавитном порядке и пронумерованы, начиная с 1.
# Ниже приведено начало списка.
# 1. ДДДД
# 2. ДДДЕ
# 3. ДДДК
# 4. ДДДО
# 5. ДДДР
# 6. ДДЕД

# Под каким номером в списке идёт первое слово, которое начинается с буквы K?

s = 'ДЕКОР'
count = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                temp = a + b + c + d
                if a == 'К':
                    print(count, temp)
                    exit()
                count += 1
'''
# 251 КДДД



# Тип 24 № 33103
'''
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество строк, в которых буква A встречается чаще, чем буква E.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

f = open('24.txt')
M = f.readlines()

count = 0
for s in M:
    if s.count('A') > s.count('E'):
        count += 1
print(count)
'''
# Ответ: 485



# region Пост: Способы получить сумму цифр строки
'''
# Способы получить сумму цифр строки
s = '11122233344'

# Вариант 1
M = [int(i) for i in s]  # разобьем строку на список целочисленных значений
summ1 = sum(M)  # через встроенную функцию sum() получим сумму строки
print(summ1)  # выводим полученную сумму цифр строки


# Вариант 1
summ2 = 0  # создаем счетчик для подсчета суммы
for i in s:  # пробегаем строку по переменной i
    summ2 += int(i)  # добавляем в счетчик переводя string цифру i в целочисленное int число
print(summ2)  # выводим полученную сумму цифр строки
# аналогичный трюк можно провернуть с индексным циклом for


# Вариант 3
summ3 = s.count('1') + s.count('2') * 2 + s.count('3') * 3 + s.count('4') * 4
print(summ3)  # у каждой цифры есть свой вес - считаем кол-во цифр и умножаем на ее вес


# Вариант 4
summ4 = 0  # создаем счетчик для подсчета суммы
n = int(s)  # переводим строку в число используя функцию int()
while n > 0:  # пока n не станет нулем производим следующие действия:
    summ4 += n % 10  # к счетчику добавляем остаток от деления числа на 10
    n //= 10  # делим число на 10, чтобы избавиться от этого остатка
print(summ4)  # выводим полученную сумму цифр строки
'''
# endregion Пост: Способы получить сумму цифр строки


# region Пост: Сравнение решения 14 номера с РЕШУ ЕГЭ и через списки

# Два варианта решений 14 номера (старого типа) через строки и списки
'''
# Тип 14 № 29662
# Значение выражения 81**17 + 3**24 − 45 записали в системе счисления с основанием 9.
# Сколько цифр «8» содержится в этой записи?

x = 81 ** 17 + 3 ** 24 - 45  # посчитали значение выражения
s = ""  # создали пустую строку для сбора остаток от деления
while x != 0:  # пока x не занулится будем делать следующие действия:
    s += str(x % 9)  # в строку добавляем остаток от деления x на систему счисления 9 переводя его в строку
    x //= 9  # обязательно получаем частное от деления, чтобы не нарушать алгоритм
s = s[::-1]  # через срезы пробегаем всю строку в обратном порядке - переворачиваем остатки от делений
print(s.count("8"))  # через универсальный метод .count() выводим кол-вол 8-ок в строке s


x = 81 ** 17 + 3 ** 24 - 45  # посчитали значение выражения
M = []  # создали пустой список для сбора остаток от деления
while x > 0:  # пока x не занулится будем делать следующие действия:
    M.append(x % 9)   # через метод списков .append() добавляем остаток от деления
    x //= 9  # обязательно получаем частное от деления, чтобы не нарушать алгоритм
M.reverse()  # через метод списков .reverse() переворачиваем остатки от делений
print(M.count(8))  # через универсальный метод .count() выводим кол-вол 8-ок в списке M
'''
# endregion Пост: Сравнение решения 14 номера с РЕШУ ЕГЭ и через списки



# Тип 5 № 14767
# Автомат получает на вход четырёхзначное число (число не может начинаться с нуля).
# По этому числу строится новое число по следующим правилам.
#
# 1. Складываются отдельно первая и вторая, вторая и третья, третья и четвёртая цифры заданного числа.
# 2. Наименьшая из полученных трёх сумм удаляется.
# 3. Оставшиеся две суммы записываются друг за другом в порядке неубывания без разделителей.
#
# Пример. Исходное число: 1984. Суммы: 1 + 9 = 10, 9 + 8 = 17, 8 + 4 = 12.
# Удаляется 10. Результат: 1217.
#
# Укажите наименьшее число, при обработке которого автомат выдаёт результат 613.

# Вариант 1
'''
for n in range(1000, 10000):
    M = [int(i) for i in str(n)]

    a = M[0] + M[1]
    b = M[1] + M[2]
    c = M[2] + M[3]

    maxi = max(a, b, c)
    sred = (a + b + c) - (max(a, b, c) + min(a, b, c))

    r = str(sred) + str(maxi)
    if r == '613':
        print(n)
        break
'''

# Вариант 1
'''
s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for x1 in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for x2 in s:
        for x3 in s:
            for x4 in s:
                a = x1 + x2
                b = x2 + x3
                c = x3 + x4

                maxi = max(a, b, c)
                sred = (a + b + c) - (max(a, b, c) + min(a, b, c))

                r = str(sred) + str(maxi)
                if r == '613':
                    print(x1, x2, x3, x4)
                    exit()
'''
# Ответ: 1067





# Тип 5 № 25836
# На вход алгоритма подаётся натуральное число N. Алгоритм строит по нему новое число следующим образом.
#
# 1) Строится двоичная запись числа N.
# 2) К этой записи дописываются справа ещё два разряда по следующему правилу:
# если N чётное, в конец числа (справа) дописываются два нуля,
# в противном случае справа дописываются две единицы.
#
# Укажите максимальное число N, для которого результат работы алгоритма будет меньше 134.
# В ответе это число запишите в десятичной системе счисления.

# Вариант1 через списки
'''
for n in range(1, 10000):
    x = n

    M = []
    while x > 0:
        M.append(x % 2)
        x //= 2
    M.reverse()

    if n % 2 == 0:
        M.append(0)
        M.append(0)
    else:
        M.append(1)
        M.append(1)

    r = 0
    M.reverse()
    for i in range(0, len(M)):
        r += M[i] * 2 ** i

    if r < 134:
        print(n)
'''

# Вариант2 через строки
'''
for n in range(1, 10000):
    s = bin(n)[2:]  # перевод в двоичную систему счисления (получаем строку)

    if n % 2 == 0:
        s += '00'
    else:
        s += '11'

    r = int(s, 2)  # перевод из двоичной системы счисления в 10-ную

    if r < 134:
        print(n)
'''
# Ответ: 32











# Тип 5 № 46963
# Алгоритм получает на вход натуральное число N>1 и строит по нему новое число R следующим образом:
#
# 1. Строится двоичная запись числа N.
# 2. Вычисляется количество единиц, стоящих на чётных местах в двоичной записи числа N без ведущих нулей,
# и количество нулей, стоящих на нечётных местах.
# Места отсчитываются слева направо (от старших разрядов к младшим, начиная с единицы).
# 3. Результатом работы алгоритма становится модуль разности полученных двух чисел.
#
# Пример. Дано число N = 39. Алгоритм работает следующим образом:
# 1. Строится двоичная запись: 39_10 = 100111_2.
# 2. Выделяем единицы на чётных и нули на нечётных местах: 100111. На чётных местах стоят две единицы, на нечётных — один ноль.
# 3. Модуль разности равен 1.
# Результат работы алгоритма R = 1.
#
# При каком наименьшем N в результате работы алгоритма получится R = 5?

# Вариант 1
'''
for n in range(2, 100000+1):
    s = bin(n)[2:]

    k1 = 0
    k0 = 0
    for i in range(0, len(s)):
        if i % 2 == 0 and s[i] == '1':
            k1 += 1
        if i % 2 != 0 and s[i] == '0':
            k0 += 1


    r = abs(k0 - k1)

    if r == 5:
        print(n)
        break
'''

# Вариант 2
'''
for n in range(2, 100000 + 1):
    s = bin(n)[2:]

    k1 = [s[i] for i in range(0, len(s)) if i % 2 == 0].count('1')
    k0 = [s[i] for i in range(0, len(s)) if i % 2 != 0].count('0')

    if abs(k0 - k1) == 5:
        print(n)
        break
'''
# Ответ: 511










# Тип 5 № 16882
# Автомат обрабатывает натуральное число N (0 ≤ N ≤ 255) по следующему алгоритму:
#
# 1. Строится восьмибитная двоичная запись числа N.
# 2. Все цифры двоичной записи заменяются на противоположные (0 на 1, 1 на 0).
# 3. Полученное число переводится в десятичную запись.
# 4. Из нового числа вычитается исходное, полученная разность выводится на экран.
#
# Пример. Дано число N = 13. Алгоритм работает следующим образом.
#
# 1. Восьмибитная двоичная запись числа N: 00001101.
# 2. Все цифры заменяются на противоположные, новая запись 11110010.
# 3. Десятичное значение полученного числа 242.
# 4. На экран выводится число 242 − 13 = 229.
#
# Какое число нужно ввести в автомат, чтобы в результате получилось 111?

# Вариант 1
'''
for n in range(0, 255+1):
    s = bin(n)[2:]

    while len(s) != 8:
        s = '0' + s

    z = ''
    for x in s:
        if x == '0':
            z += '1'
        else:
            z += '0'

    r = int(z, 2) - n

    if r == 111:
        print(n)
'''

# Вариант 2
'''
for n in range(0, 255+1):
    s = bin(n)[2:]

    while len(s) != 8:
        s = '0' + s

    s = s.replace('0', '*')
    s = s.replace('1', '0')
    s = s.replace('*', '1')

    r = int(s, 2) - n

    if r == 111:
        print(n)
'''

# Вариант 2
'''
for n in range(0, 255+1):
    x = n

    M = []
    while x > 0:
        M.append(x % 2)
        x //= 2
    M.reverse()

    while len(M) != 8:
        M.reverse()
        M.append(0)
        M.reverse()

    for i in range(0, len(M)):
        if M[i] == 0:
            M[i] = 1
        else:
            M[i] = 0

    sum = 0
    M.reverse()
    for i in range(0, len(M)):
        sum += M[i] * 2 ** i

    r = sum - n

    if r == 111:
        print(n)
'''
# Ответ: 72
