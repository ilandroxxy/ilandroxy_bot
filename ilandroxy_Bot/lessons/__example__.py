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










