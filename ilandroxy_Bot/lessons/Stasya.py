
# region Домашка: **********************************************************


# endregion Домашка: **********************************************************


# region Урок: **********************************************************

# Тип 24 № 36879
'''
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# В строках, содержащих менее 25 букв G, нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.

# Вариант 1
import string
S = open('24.txt').readlines()

M = []
for x in S:
    if x.count('G') < 25:
        M.append(x)

alphabet = string.ascii_uppercase
maxi = 0
for x in M:
    for a in alphabet:
        maxi = max(maxi, x.rindex(a) - x.index(a))
print(maxi)


# Вариант 2

S = open('24.txt').readlines()

M = []
for x in S:
    if x.count('G') < 25:
        M.append(x)

alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
maxi = 0
for x in M:
    for a in alphabet:
        maxi = max(maxi, x.rindex(a) - x.index(a))
print(maxi)
'''
# Ответ 1001


'''
alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
alphabet = sorted([i for i in 'QWERTYUIOPASDFGHJKLZXCVBNM'])
alphabet = ''.join(sorted([i for i in 'QWERTYUIOPASDFGHJKLZXCVBNM']))
print(alphabet)
'''


# Тип 24 № 35482
'''
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# Необходимо найти строку, содержащую наименьшее количество букв G (если таких строк несколько, надо взять ту, которая находится в файле раньше),
# и определить, какая буква встречается в этой строке чаще всего.
# Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.

# Вариант 1
S = open('24.txt').readlines()

mini = 99999
r = ''
for x in S:
    if x.count('G') < mini:
        mini = x.count('G')
        r = x

alphabet = sorted([i for i in 'QWERTYUIOPASDFGHJKLZXCVBNM'])
maxi = 0
result = ''
for a in alphabet:
    if maxi <= r.count(a):
        maxi = r.count(a)
        result = a
        print(a, maxi)

# Вариант 2
S = open('24.txt').readlines()

mini = 99999
r = ''
for x in S:
    if x.count('G') < mini:
        mini = x.count('G')
        r = x

alphabet = sorted([i for i in 'QWERTYUIOPASDFGHJKLZXCVBNM'])
my_dict = {}  # dict()
for a in alphabet:
    my_dict[r.count(a)] = a
print(max(my_dict.items()))


# Вариант 3
S = open('24.txt').readlines()

mini = 99999
r = ''
for x in S:
    if x.count('G') < mini:
        mini = x.count('G')
        r = x

alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
my_dict = {}  # dict()
for a in alphabet:
    my_dict[a] = r.count(a)
print(sorted(my_dict.items()))
'''
# Ответ: T



# Тип 24 № 29672
'''
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество строк, в которых буква E встречается чаще, чем буква A.

# Вариант 1
S = open('24.txt').readlines()

count = 0
for x in S:
    if x.count('E') > x.count('A'):
        count += 1
print(count)

# Вариант 2
f = open('24.txt')
count = 0
for x in f:
    if x.count('E') > x.count('A'):
        count += 1
print(count)
'''
# Ответ: 467


# Тип 24 № 47228 i
# Текстовый файл состоит из символов A, C, D, F и O.
#
# Определите максимальное количество идущих подряд пар символов вида
#
# согласная + гласная.
#
# Для выполнения этого задания следует написать программу.

# Вариант 1
'''
s = open('24.txt').readline()

sogl = 'CDF'  # CA CO DA DO FA FO
glas = 'AO'
count = 0
maxi = 0
for i in range(0, len(s)-1):
    if (s[i] in sogl and s[i+1] in glas) or (s[i+1] in sogl and s[i] in glas):
        count += 1
        maxi = max(maxi, count)
    else:
        count = 0
print(maxi / 2)
'''

# Вариант 2
'''
s = open('24.txt').readline().replace('CA', '*').replace('CO', '*').replace('DA', '*').replace('DO', '*').replace('FA', '*').replace('FO', '*')
s = s.replace('A', ' ').replace('O', ' ').replace('C', ' ').replace('D', ' ').replace('F', ' ')
M = [len(i) for i in s.split()]
print(max(M))
'''
# Ответ: 95


# Тип 9 № 47213
'''
# Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.

# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# — в строке только одно число повторяется ровно два раза, остальные числа различны;
# — среднее арифметическое неповторяющихся чисел строки не больше суммы повторяющихся чисел.
#
# В ответе запишите только число.

count = 0
for x in open('9.txt'):
    M = [int(i) for i in x.split()]
    if len(set(M)) == 5:  # — в строке только одно число повторяется ровно два раза, остальные числа различны;
        DUB = sum(M) - sum(set(M))  # число повторяется
        if ((sum(set(M)) - DUB) / 4) <= DUB*2:
            count += 1
print(count)
'''
# Ответ: 9


# Тип 9 № 45243
'''
# Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел.

# Определите количество строк таблицы, в которых квадрат суммы максимального и минимального чисел в строке больше суммы квадратов трёх оставшихся.

count = 0
for x in open('9.txt'):
    M = sorted([int(i) for i in x.split()])
    if (M[0] + M[4]) ** 2 > (M[1]**2 + M[2]**2 + M[3]**2):
        count += 1
print(count)
'''
# Ответ: 2640



# Тип 9 № 27406
'''
# Откройте файл электронной таблицы, содержащей вещественные числа — результаты ежечасного измерения температуры воздуха на протяжении трёх месяцев.
#
# Найдите разность между максимальным значением температуры и её средним арифметическим значением. В ответе запишите только целую часть получившегося числа.

A = []
for x in open('9.txt'):
    M = [float(i) for i in x.replace(',', '.').split()]
    A += M

print(round(max(A) - (sum(A)/len(A)), 3))
'''
# Ответ: 14



# endregion Урок: **********************************************************


# todo: Стася = [2, 5, 6, 8, 9, 12, 14+, 15, 16, 17, 23, 24, 25.2]
# на прошлом уроке: Прорешали 24 номера на несколько строк, затем разобрали несколько 9 задач на Excel.
# на следующем уроке:

