# Тип 24 № 33769
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле после двух одинаковых символов.
# Например, в тексте CCCBBABAABCC есть комбинации CCC, CCB, BBA и AAB.

'''
file = open('24 (1).txt', 'r')
f = file.readline()
# f = "CCCBBABAABCC"
letters = []
maxim = 0
outcome_ind = 0
for i in range(len(f)-2):
    if f[i] == f[i+1]:
        letters.append(f[i+2])
for j in range(len(letters)):
    l = letters.count(letters[j])
    if maxim < l:
        maxim = l
        outcome_ind = j
print(letters[outcome_ind])
'''

# Ответ: K

# Тип 24 № 33494 Добавить в вариант
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле сразу после буквы E.
# Например, в тексте EBCEEBEDDD после буквы E два раза стоит B, по одному разу — E и D.
# Для этого текста ответом будет B.

'''
file = open('24 (2).txt', 'r')
f = file.readline()
# f = "EBCEEBEDDD"
letters = []
maxim = 0
outcome_ind = 0
for i in range(len(f)-1):
    if f[i] == "E":
        letters.append(f[i+1])
for j in range(len(letters)):
    l = letters.count(letters[j])
    if maxim < l:
        maxim = l
        outcome_ind = j
print(letters[outcome_ind])
'''

# Ответ: Y

# Тип 24 № 35913
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Необходимо найти строку, содержащую наименьшее количество букв N
# (если таких строк несколько, надо взять ту, которая находится в файле раньше)
# и определить, какая буква встречается в этой строке чаще всего.
# Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.

# Пример. Исходный файл:
# NINA
# NABLAB
# ANAAA

# В этом примере в первой строке две буквы N, во второй и третьей — по одной.
# Берём вторую строку, т.к. она находится в файле раньше.
# В этой строке чаще других встречаются буквы A и B (по два раза), выбираем букву B, т.к. она позже стоит в алфавите.
# В ответе для этого примера надо записать B.

'''
file = open('24 (3).txt', 'r')
f = file.readlines()
# f = ['NINA', 'NABLAB', 'ANAAA']
minim = 1000
minim_ind = 1000
maxim = 0
maxim_ind = 0
for i in range(len(f)):
    temp_N = []
    temp_N.extend(f[i])
    N_count = temp_N.count('N')
    if minim > N_count:
        minim = N_count
        minim_ind = i
for i in range(len(f[minim_ind])):
    temp = []
    temp.extend(f[minim_ind])
    l = temp.count(temp[i])
    if maxim < l:
        maxim = l
        maxim_ind = i
    elif maxim == l:
        maxim_ind = i
print(temp[maxim_ind])
'''
# Ответ: Y

'''
s = '1213141'
print(s.index('1'), s.rindex('1'))

import string
ALphabet = string.ascii_uppercase
print(ALphabet, type(ALphabet))

M = [i for i in ALphabet]
print(M)
'''


# Тип 24 № 35913
# Текстовый файл содержит строки различной длины. Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Необходимо найти строку, содержащую наименьшее количество букв N (если таких строк несколько, надо взять ту, которая находится в файле раньше)
# и определить, какая буква встречается в этой строке чаще всего.
# Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.

# Пример. Исходный файл:
# NINA
# NABLAB
# ANAAA

# В этом примере в первой строке две буквы N, во второй и третьей — по одной.
# Берём вторую строку, т.к. она находится в файле раньше.
# В этой строке чаще других встречаются буквы A и B (по два раза), выбираем букву B, т.к. она позже стоит в алфавите.
# В ответе для этого примера надо записать B.

'''
import string
ALphabet = string.ascii_uppercase

file = open('24.txt', 'r')
f = file.readlines()
#f = ['NINA', 'NABLAB', 'ANAAA']

mini = 99999
S = ''
for STR in f:
    if mini > STR.count('N'):
        mini = STR.count('N')
        S = STR
print(S)

maxi = -9999
for i in ALphabet:
    if maxi <= S.count(i):
        maxi = S.count(i)
        print(S.count(i), i)
'''

"""
import string
ALphabet = string.ascii_uppercase

file = open('24.txt', 'r')
f = file.readlines()
#f = ['NINA', 'NABLAB', 'ANAAA']

mini = 99999
S = ''
for STR in f:
    if mini > STR.count('N'):
        mini = STR.count('N')
        S = STR
print(S)

# SET = set()
DICT = {}
for i in ALphabet:
    DICT[S.count(i)] = i
print(DICT)


print(max(DICT), DICT[max(DICT)])
"""


# Тип 24 № 33526
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле между двумя одинаковыми символами.
#
# Например, в тексте CBCABABACCC есть комбинации CBC, ABA (два раза), BAB и CCC.
# Чаще всего — 3 раза — между двумя одинаковыми символами стоит B, в ответе для этого случая надо написать B.
#
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

'''
f = open('24.txt', 'r')
s = f.readline()

M = []
for i in range(0, len(s)-2):
    if s[i] == s[i+2]:
        M.append(s[i+1])

import string
Alphabet = string.ascii_uppercase

DICT = {}
for i in Alphabet:
    DICT[M.count(i)] = i
print(DICT[max(DICT)])
'''









# Тип 24 № 35998
'''
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# В строках, содержащих менее 25 букв A, нужно определить и вывести максимальное расстояние между
# одинаковыми буквами в одной строке.
#
# Пример. Исходный файл:
# GIGA
# GABLAB
# NOTEBOOK
# AGAAA
#
# В этом примере во всех строках меньше 25 букв A.
# Самое большое расстояние между одинаковыми буквами – в третьей строке между буквами O, расположенными
# в строке на 2-й и 7-й позициях.
# В ответе для данного примера нужно вывести число 5.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

f = open('24.txt', 'r')
s = f.readlines()

import string
Alphabet = string.ascii_uppercase
print(len(s))

M = []
for i in s:
    if i.count('A') < 25:
        M.append(i)
print(len(M))

for i in M:
    maxi = -9999
    for j in Alphabet:
        if maxi < i.rindex(j) - i.index(j):
            maxi = i.rindex(j) - i.index(j)
    print(maxi)
'''











# Тип 24 № 47228
'''
# Текстовый файл состоит из символов A, C, D, F и O.

# Определите максимальное количество идущих подряд пар символов вида
#
# согласная + гласная.
#
# Для выполнения этого задания следует написать программу.

import random
M = ['A', 'O', 'C', "D", "F"]
N = 'AOCDF'
s = ''
for i in range(0, 1000000):
    s += random.choice(N)


#f = open('24.txt', 'r')
#s = f.readline()
print(s)

s1 = 'AO'
s2 = 'CDF'
count = 0
MaxCount = 0
for i in range(0, len(s)-1):
    if (s[i] in s1 and s[i+1] in s2) or (s[i] in s2 and s[i+1] in s1):
        count += 1
        if MaxCount < count:
            MaxCount = count
    else:
        count = 0
print(MaxCount)
'''



# Тип 24 № 36037
'''
# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

f = open('24.txt', 'r')
s = f.readline()
# s =  FHX ZZYJDOWDKXZZ Y
s = s.replace('XZZY', "*")
M = [len(i) for i in s.split('*')]
print(max(M) + 6)
'''
# Ответ 1713


# Тип 24 № 27689

# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите максимальную длину цепочки вида XYZXYZXYZ... (составленной из фрагментов XYZ, последний фрагмент может быть неполным).
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

f = open('24.txt', 'r')
s = f.readline()
s = s.replace('XYZ', '*')
s = s.replace('*XY', '+')
s = s.replace('*X', '-')
s = s.replace('X', ' ')
s = s.replace('Y', ' ')
s = s.replace('Z', ' ')

M = [i for i in s.split()]
A = []
res = 0
for i in M:
    for j in i:
        if j == '*':
            res += 3
        if j == '+':
            res += 5
        if j == '-':
            res += 4
    A.append(res)
print(A)
print(max(A))
