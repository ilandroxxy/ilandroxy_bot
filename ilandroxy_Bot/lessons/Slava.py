
# region Домашка: ******************************************************************************

# Тип 1

# Задание 2. Тип 24 № 27686
'''
# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите длину самой длинной последовательности, состоящей из символов X. Хотя бы один символ X находится в последовательности.

print(max(map(len, open('24.txt').readline().replace('Z', ' ').replace('Y', ' ').split())))

print(len(max([i for i in open('24.txt').readline().replace('Z', ' ').replace('Y', ' ').split()])))

f = open('24.txt')
s = f.readline()
s = s.replace('Z', ' ')
s = s.replace('Y', ' ')
M = s.split()
print(len(max(M)))
'''





# Тип 2

# Задание 5. Тип 24 № 27689.
'''
# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите максимальную длину цепочки вида XYZXYZXYZ... (составленной из фрагментов XYZ, последний фрагмент может быть неполным).

f = open('24.5.txt').readline()
count = 0
MaxCount = 0
for i in range(len(f)):
    if (f[i] == 'X' and count%3 == 0) or (f[i] == 'Y' and count%3 == 1) or (f[i] == 'Z' and count%3 == 2):
        count += 1
        MaxCount = max(MaxCount, count)
    elif f[i] == 'X':
        count = 1
    else:
        count = 0
print(MaxCount)
# Ответ: 13
'''





# Тип 3
'''
# Задание 10. Тип 24 № 27694.
# Текстовый файл состоит не более чем из 106 символов A, B и C.
# Определите максимальную длину цепочки вида ABABAB... (составленной из фрагментов AB, последний фрагмент может быть неполным).

f = open('24.10.txt').readline()
count = 0
MaxCount = 0
for i in range(len(f)):
    if (f[i] == 'A' and count%2 == 0) or (f[i] == 'B' and count%2 == 1):
        count += 1
        MaxCount = max(MaxCount, count)
    elif f[i] == 'A':
        count = 1
    else:
        count = 0
print(MaxCount)
# Ответ: 24
'''





# Тип 4
'''
# Задание 18. Тип 24 № 33196.
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще всего встречается в файле сразу после буквы A.

f = open('24.18.txt')
s = f.readline()
a = [0] * 26
maxi = 0
for i in range(len(s) - 1):
    if s[i] == 'A':
        a[ord(s[i + 1]) - 65] += 1
for i in range(26):
    if a[i] > maxi:
        maxi = a[i]
        index = i
print(chr(index + 65))
'''



'''
# Задание 19. Тип 24 № 33494.
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще всего встречается в файле сразу после буквы E.

# Вариант 1
from collections import Counter
f = open('24.19.txt')
s = f.readline()
M = ''
for i in range(len(s)-1):
    if s[i] == 'E':
        M = M + s[i + 1]
print(Counter(M).most_common()[0][0])
Ответ: Y

# Вариант 2
f = open('24.19.txt')
s = f.read()
d = dict()
for i in range(len(s) - 1):
    if s[i] == 'E' and s[i+1] != 'E':
        if s[i + 1] not in d:
            d[s[i + 1]] = 1
        else:
            d[s[i + 1]] += 1
max_key = max(d, key=d.get)
print(max_key)
'''

'''
s = 'ABCDABCDABJHBACBD'
d = {}
for x in s:
    d[x] = s.count(x)
print(d)

print(d['A'])
d['A'] = [1, 2, 3]
print(d)
'''




# Тип 5
'''
# Задание 20. Тип 24 № 33526.
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле между двумя одинаковыми символами.

f = open('24.20.txt')
s = f.readline()
MaxCount = 0
for w in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    count = 0
    for i in range(len(s) - 2):
        if s[i] == s[i+2] and s[i+1] == w:
            count = count + 1
    if count > MaxCount:
        MaxCount = count
        e = w
print(e, MaxCount)
# Ответ: D


# Вариант 2.
f = open('24.20.txt')
s = f.read()
a = [0]*150
count = 0
MaxCount = 0

for i in range(len(s) - 2):
    if s[i] == s[i + 2]:
        a[ord(s[i + 1])] = a[ord(s[i + 1])] + 1

ch = ''
MaxCount = 0
for i in range(0, 150):
    if a[i] > MaxCount:
        MaxCount = a[i]
        ch = chr(i)
print(ch, MaxCount)
'''





# Тип 6
'''
# Задание 21. Тип 24 № 33769.
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще всего встречается в файле после двух одинаковых символов.

f = open('24.21.txt')
s = f.readline()
a = [0] * 26
maxi = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        a[ord(s[i + 2]) - 65] += 1
for i in range(26):
    if a[i] > maxi:
        maxi = a[i]
        index = i
print(chr(index + 65))
# Ответ: K
'''





# Тип 7
'''
# Задание 22. Тип 24 № 35482.
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Необходимо найти строку, содержащую наименьшее количество букв G (если таких строк несколько, надо взять ту, которая находится в файле раньше),
# и определить, какая буква встречается в этой строке чаще всего. Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.

f = open('24.22.txt')
s = f.readlines()
m = 1000000
for i in s:
    if i.count('G') < m:
        m = i.count('G')
        ms = i
a = [0] * 26
for i in range(len(ms)-1):
    a[ord(ms[i])-65] += 1
for i in range(len(a)-1, -1, -1):
    if a[i] == max(a):
        print(chr(i+65))
        break
# Ответ: T
'''

# Вариант 2
'''
import string
Alphabet = string.ascii_uppercase

f = open('24.txt')
s = f.readlines()

mini = 99999
r = ''
for x in s:
    if mini > x.count('G'):
        mini = x.count('G')
        r = x

maxi = 0
for x in Alphabet:
    if maxi <= r.count(x):
        maxi = r.count(x)
        print(maxi, x)
'''





'''
# Задание 23. Тип 24 № 35913.
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Необходимо найти строку, содержащую наименьшее количество букв N (если таких строк несколько, надо взять ту, которая находится в файле раньше),
# и определить, какая буква встречается в этой строке чаще всего. Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.

f = open('24.23.txt')
s = f.readlines()
a = [0] * 26
min = 100000000
maxi = 0
for i in range(len(s)):
    str = s[i]
    if str.count('N') < min:
        min = str.count('N')
        s1 = str
for i in range(len(s1) - 1):
    a[ord(s1[i]) - 65] += 1
for i in range(26):
    if a[i] >= maxi:
        maxi = a[i]
        index = i
print(chr(index + 65))
# Ответ: Y
'''





# Тип 8
''' 
# Задание 26. Тип 24 № 36879.
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# В строках, содержащих менее 25 букв G, нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.

f = open('24.txt')
s = f.readlines()
Max = 0
M = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for j in s:
    for i in M:
        if j.rindex(i) - j.index(i) > Max:
            if j.count("G") < 25:
                Max = j.rindex(i) - j.index(i)
print(Max)
'''
# Ответ: 1001






# Тип 9
# Задание 25. Тип 24 № 36037.
''' 
# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.

f = open('24.txt', 'r')
s = f.readline()

# s = s.replace('XZZY', ' ')
M = [len(i) for i in s.split('XZZY')]
print(max(M)+6)  # XZZY + s + XZZY ответ будет ZZY + s + XZZ
# Ответ: 1713
#
#  
# XZZY ABCD XZZY
# ABCD
# ZZY ABCD XZZ
'''






# Тип 10
''' 
# Задание 28. Тип 24 № 37159.
# Текстовый файл состоит не более, чем из 10**7 строчных букв английского алфавита.
# Найдите максимальную длину подстроки, в которой символы «a» и «d» не стоят рядом.

f = open('24.txt')
s = f.readline()
s = s.replace('ad', 'a d')
s = s.replace('da', 'd a')
M = [len(i) for i in s.split()]
print(max(M))

# w = list(map(len, s.split()))
# print(max(w))
'''
# Ответ: 2252






# Тип 11

# Задание 31. Тип 24 № 39253.
'''
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых не более одной буквы D.

f = open('24.txt')
s = f.readline()

M = []
Max = 0

for i in range(0, len(s)):
    if s[i] == 'D':
        M.append(i)
print(M)

for i in range(len(M) - 2):
    c = M[i + 2] - M[i] - 1
    Max = max(Max, c)
print(Max)
'''
# Ответ: 354





# Тип 12
'''
# Задание 32. Тип 24 № 40740.
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC...Z).
# Определите максимальное количество идущих подряд символов, среди которых нет ни одной буквы A и при этом не менее трёх букв E.

f = open('24.32.txt').read().split('A')

MaxCount = 0
for i in f:
    if i.count('E') >= 3:
        MaxCount = max(len(i), MaxCount)
print(MaxCount)
# Ответ: 282
'''





# Тип 13
# Задание 34. Тип 24 № 45258.
'''
# Текстовый файл состоит из символов A, B и C.
# Определите максимальное количество идущих подряд пар символов AB или CB в прилагаемом файле.

f = open('24.txt')
s = f.read()
s = s.replace('AB', 'x')
s = s.replace('CB', 'x')
count = 0
MaxCount = 0
for i in range(len(s)):
    if s[i]=='x':
        count += 1
        MaxCount = max(MaxCount, count)
    else:
        count = 0
print(MaxCount)
# Ответ: 65

f = open('24.txt')
s = f.read()
s = s.replace('AB', 'x')
s = s.replace('CB', 'x')
s = s.replace('A', ' ')
s = s.replace('B', ' ')
s = s.replace('C', ' ')
M = [len(i) for i in s.split()]
print(max(M))
'''





# Тип 14
'''
# Задание 35. Тип 24 № 46982.
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество групп из идущих подряд не менее 12 символов, которые начинаются и заканчиваются буквой E
# и не содержат других букв E (кроме первой и последней) и букв F.

# Вариант 2
f = open('24.txt')
M = f.readline().split('E')
A = [i for i in M if len(i) >= 10 and 'F' not in i]
print(len(A))

# Вариант 1
f = open('24.txt').read().split('E')
count = 0
for i in f:
    if len(i) < 10:
        continue
    if 'F' in i:
        continue
    count += 1
print(count)
# Ответ: 9655
'''







# Тип 15
'''
# Задание 37. Тип 24 № 47228.
# Текстовый файл состоит из символов A, C, D, F и O.
# Определите максимальное количество идущих подряд пар символов вида
# согласная + гласная.

f = open('24.37.txt')
s = f.readline().replace('C', 'S').replace('D', 'S').replace('F', 'S')
s = s.replace('A', 'G').replace('O', 'G')
s = s.replace('SG', '*')
count = 0
MaxCount = 0
for i in s:
    if i == '*':
        count += 1
        MaxCount = max(count, MaxCount)
    else:
        count = 0
print(MaxCount)
# Ответ: 95
'''









# endregion Домашка:  ******************************************************************************



# region Урок:  ******************************************************************************




# endregion Урок:  ******************************************************************************


# todo: Слава = [2, 5, 6, 8, 12, 14+, 15, 16, 17, 23, 24], на следующем уроке: