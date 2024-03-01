# region Домашка: ***************************************************************


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************

# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ T встречается ровно 3 раза.

# 'TxxxxxxxxxTxxxxTxxxxxxxTxxxxTxxxxxxTxxxxxTxxxxxTxxxxxxxxxxxxxT'
# ['', 'xxxxxxxxx', 'xxxx', 'xxxxxxx', 'xxxx', 'xxxxxx', 'xxxxx', 'xxxxx', 'xxxxxxxxxxxxx', '']
# TxxxxxxxxxTxxxxTxxxxxxx 23
# xxxxxxxxxTxxxxTxxxxxxxTxxxx 27
# xxxxTxxxxxxxTxxxxTxxxxxx 24
# xxxxxxxTxxxxTxxxxxxTxxxxx 25
# xxxxTxxxxxxTxxxxxTxxxxx 23
# xxxxxxTxxxxxTxxxxxTxxxxxxxxxxxxx 32
# xxxxxTxxxxxTxxxxxxxxxxxxxT 26
'''
s = 'TxxxxxxxxxTxxxxTxxxxxxxTxxxxTxxxxxxTxxxxxTxxxxxTxxxxxxxxxxxxxT'
s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    # r = s[i] + 'T' + s[i+1] + 'T' + s[i+2] + 'T' + s[i+3]
    r = 'T'.join(s[i:i+4])
    if maxi < len(r):
        maxi = len(r)
        print(r, len(r))
print(maxi)
'''

# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле минимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ T встречается ровно 3 раза.

# 'TxxxxxxxxxxxxxTxxxxTxxxxxxxTxxxxTxxxxxxTxxxxxTxxxxxTxxxxxxxxxxxxxT'
# ['', 'xxxxxxxxx', 'xxxx', 'xxxxxxx', 'xxxx', 'xxxxxx', 'xxxxx', 'xxxxx', 'xxxxxxxxxxxxx', '']
'''
s = 'TxxxxxxxxxxxxxTxxxxTxxxxxxxTxxxxTxxxxxxTxxxxxTxxxxxTxxxxxxxxxxxxxT'
s = s.split('T')
mini = 999999999
for i in range(len(s)-1):
    r = 'T'.join(s[i:i+2])
    if mini > len(r):
        mini = len(r)
        print(r, len(r))
print(mini + 2)
'''


# Тип 24 №60266
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ T встречается ровно 100 раз.
'''
s = open('24.txt').readline()
s = s.split('T')
maxi = 0
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    if maxi < len(r):
        maxi = len(r)
print(maxi)
'''
# Ответ: 133


# Тип 24 №59794
# Текстовый файл состоит не более чем из 10**6 символов латинского алфавита.
# Определите минимальную длину подстроки, содержащую ровно 110 символов "U".
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline()
s = s.split('U')
mini = 999999999
for i in range(len(s)-108):
    r = 'U'.join(s[i:i+109])
    if mini > len(r):
        mini = len(r)
print(mini + 2)
'''
# Ответ: 1765


# Тип 24 №35913
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# Необходимо найти строку, содержащую наименьшее количество букв N
# (если таких строк несколько, надо взять ту, которая находится в файле раньше),
# и определить, какая буква встречается в этой строке чаще всего.
# Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.
'''
import string
alphabet = string.ascii_uppercase
s = open('24.txt').readlines()
mini = 99999
r = ''
for x in s:
    if mini > x.count('N'):
        mini = x.count('N')
        r = x

R = []
for a in alphabet:
    R.append([r.count(a), a])
print(max(R))
'''
# Ответ: Y


# Тип 24 №36879
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# В строках, содержащих менее 25 букв G, нужно определить
# и вывести максимальное расстояние между одинаковыми буквами в одной строке.
'''
import string
alphabet = string.ascii_uppercase
s = open('24.txt').readlines()
maxi = 0
for x in s:
    if x.count('G') <= 25:
        for a in alphabet:
            maxi = max(maxi, x.rindex(a) - x.index(a))
print(maxi)
'''
# Ответ: 1001


# Тип 24 №33103
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

# Вариант 2
print(len([x for x in open('24.txt').readlines() if x.count('A') > x.count('E')]))
'''
# Ответ: 485


# Тип 24 №33494
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле сразу после буквы E.
'''
import string
alphabet = string.ascii_uppercase
s = open('24.txt').readline()
M = []
for i in range(len(s)-1):
    if s[i] == 'E':
        M.append(s[i+1])

R = []
for a in alphabet:
    R.append([M.count(a), a])

print(max(R))
'''
# Ответ: Y


# Тип 24 №55611
# Текстовый файл содержит строки различной длины, содержащие только заглавные буквы латинского алфавита (ABC…Z).
# В каждой строке файла определяется буква, которая чаще всего стоит сразу после буквы A,
# эта буква заносится в отдельный список. Если несколько разных букв встречаются в строке сразу
# после A одинаковое максимальное количество раз, в список заносятся все эти буквы.
# Определите, сколько раз встретится в этом списке самая частая в нём буква.
'''
import string
alphabet = string.ascii_uppercase

R = []
s = open('24.txt').readlines()
for x in s:
    M = []
    maxi = 0
    for i in range(len(x)-1):
        if x[i] == 'A':
            M.append(x[i+1])
    for a in alphabet:
        maxi = max(maxi, M.count(a))
    for a in alphabet:
        if M.count(a) == maxi:
            R.append(a)

A = []
for a in alphabet:
    A.append(R.count(a))

print(max(A))
'''


# 23 № 13099 (Уровень: Базовый)
# A. Вычесть 1
# B. Умножить на 2
# C. Умножить на 3
# Сколько существует программ, которые преобразуют исходное число 3
# в число 15 и при этом не содержат двух команд A подряд?

# 3 *3 = 9 -1 = 8 *2 = 16 -1 = 15
'''
def F(a, b, f):
    if a > b+1:
        return 0
    if a == b:
        return 1
    if f == 'A':
        return F(a * 2, b, 'B') + F(a * 3, b, 'C')
    return F(a-1, b, 'A') + F(a*2, b, 'B') + F(a*3, b, 'C')


print(F(3, 15, 0))
'''
# Ответ: 6

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Марго = [2.1, 5.1, 6.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 17.1, 23.1, 24.1]
# КЕГЭ  = []
# на следующем уроке: Разобрать 25 номера
