# region Домашка: ************************************************************


# endregion Домашка: ************************************************************

# region Урок: ************************************************************

# Максимальное количество идущих подряд символов, среди которых символ T встречается ровно 100 раза
s = 'xxxxxxTxxxxxTxxxxxxTxxxxxTxxxxTxxxxxxTxxxxxTxxxxxxxxx'
# ['xxxxxx', 'xxxxx', 'xxxxxx', 'xxxxx', 'xxxx', 'xxxxxx', 'xxxxx', 'xxxxxxxxx']
# xxxxxxTxxxxxTxxxxxxTxxxxx 25
# xxxxxTxxxxxxTxxxxxTxxxx 23
# xxxxxxTxxxxxTxxxxTxxxxxx 24
# xxxxxTxxxxTxxxxxxTxxxxx 23
# xxxxTxxxxxxTxxxxxTxxxxxxxxx 27
'''
s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    # r = s[i] + 'T' + s[i+1] + 'T' + s[i+2] + 'T' + s[i+3]
    r = 'T'.join(s[i:i+4])
    print(r, len(r))
    maxi = max(maxi, len(r))
print(maxi)
'''

# Минимальное количество идущих подряд символов, среди которых символ T встречается ровно 3 раза
'''
s = 'xxxxxxTxxxxxTxxxxxxTxxxxxTxxxxTxxxxxxTxxxxxTxxxxxxxxx'
# ['xxxxxx', 'xxxxx', 'xxxxxx', 'xxxxx', 'xxxx', 'xxxxxx', 'xxxxx', 'xxxxxxxxx']

s = s.split('T')
mini = 10**9
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    print(r, len(r))
    mini = min(mini, len(r))
print(mini)
'''


# Тип 24 №60266
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ T встречается ровно 100 раз.
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline().split('T')
maxi = 0
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    maxi = max(maxi, len(r))
print(maxi)
'''
# Ответ: 133


# Тип 24 №59792
# Текстовый файл состоит не более чем из 10**6 символов латинского алфавита.
# Определите минимальную подстроку, содержащую 100 символов "Т".
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline().split('T')
mini = 10**9
for i in range(len(s)-98):
    r = 'T' + 'T'.join(s[i:i+99]) + 'T'
    mini = min(mini, len(r))
print(mini)
'''
# Ответ: 1523


# Тип 24 №33494
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле сразу после буквы E.
'''
s = open('24.txt').readline()
M = []
for i in range(len(s)-1):
    if s[i] == 'E':
        M.append(s[i+1])

R = []
for a in set(M):
    R.append([M.count(a), a])

print(R)
print(max(R))
print(max(R)[1])
'''


# Тип 24 №33526
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле между двумя одинаковыми символами.
'''
s = open('24.txt').readline()
M = []
for i in range(len(s)-2):
    if s[i] == s[i+2]:
        M.append(s[i+1])

R = []
for a in set(M):
    R.append([M.count(a), a])

print(R)
print(max(R))
print(max(R)[1])
'''
# Ответ: D


# Тип 24 № 33103
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество строк, в которых буква A встречается чаще, чем буква E.
'''
s = open('24.txt').readlines()
cnt = 0
for x in s:
    if x.count('A') > x.count('E'):
        cnt += 1
print(cnt)
'''
# Ответ: 485


# Тип 24 №36879
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# В строках, содержащих менее 25 букв G, нужно определить и вывести максимальное
# расстояние между одинаковыми буквами в одной строке
'''
import string
alphabet = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

s = open('24.txt').readlines()
maxi = 0
for x in s:
    if x.count('G') < 25:
        for a in alphabet:
            maxi = max(maxi, x.rindex(a) - x.index(a))
print(maxi)

# Ответ: 1001

x = 'xxxAxxxxxAxxxxxAx'
print(x.rindex('A'), x.index('A'))  # 15 3
print(x.rindex('A') - x.index('A'))  # 12
'''


# Тип 24 №35482
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# Необходимо найти строку, содержащую наименьшее количество букв G (если таких строк несколько,
# надо взять ту, которая находится в файле раньше), и определить, какая буква встречается в этой строке чаще всего.
# Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.
'''
import string
alphabet = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ

s = open('24.txt').readlines()
mini = 10**9
r = ''
for x in s:
    if mini > x.count('G'):   # >= которая находится в файле позже
        mini = x.count('G')
        r = x
        print(mini, r)

maxi, b = 0, ''
for a in alphabet:
    # print(a, r.count(a))
    if maxi <= r.count(a):
        maxi, b = r.count(a), a

print(b)
'''
# Ответ: T

s = open('24.txt').readlines()
n = []
for x in s:
    m = []
    for i in range(len(x) - 1):
        if x[i] == 'T':
            m.append(x[i + 1])

    maxi = 0
    for j in set(m):
        maxi = max(maxi, m.count(j))

    for j in set(m):
        if m.count(j) == maxi:
            n.append(j)

print(n)

# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# todo разобрать Тип 24 №63073 Олеся
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых каждая из букв C и D встречается
# не более двух раз.
'''
s = open('24-181.txt').readline()

l = 0 # левый указатель подстроки
m = 0 # максимальная длина последовательности
k = 0 # количество " . "

for r in range(len(s)):
    if s[r] == '.' : 
        k += 1
    while k > 4:
        if s[l] == '.' :
            k -= 1
        l += 1
    m = max(m, r - l + 1)
print(m)
'''

# todo разобрать Тип 24 №63040 Олеся
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых каждая из букв A и B
# встречается не более двух раз.


# todo разобрать  Тип 24 №61370 Олеся
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых ровно по одному разу встречаются буквы A и B.


# endregion Разобрать: *************************************************************


# Олеся = [1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 14, 16, 17, 18, 19-21 (кодом), 24, 25]
# КЕГЭ = []
# на следующем уроке: Разбираем сложыне 24 номера на строки и кол-во
