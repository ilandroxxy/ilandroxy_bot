# region Домашка: ******************************************************************


# endregion Домашка: *****************************************************************


# region Урок: ******************************************************************


# Тип 24 №39253
# Текстовый файл содержит только заглавные буквы латинского алфавита
# (ABC…Z). Определите максимальное количество идущих подряд символов,
# среди которых не более одной буквы D.
'''
s = open('24.txt').readline().split('D')
maxi = 0
for i in range(len(s)-1):
    r = s[i] + 'D' + s[i+1]
    maxi = max(maxi, len(r))
print(maxi)
'''
# Ответ: 354


# Тип 24 №61404
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите максимальное
# количество идущих подряд символов, среди которых ровно по одному разу встречаются буквы X и Y.
'''
s = open('24.txt').readline()
s = s.replace('X', 'X ').replace('Y', 'Y ').split()
maxi = 0
for i in range(len(s)-2):
    r = s[i] + s[i+1] + s[i+2][:-1]
    maxi = max(maxi, len(r))
print(maxi)
'''


# Тип 24 №63073
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z). Определите максимальное к
# оличество идущих подряд символов, среди которых каждая из букв C и D встречается не более двух раз.
'''
s = open('24.txt').readline()
s = s.replace('C', 'C ').replace('D', 'D ').split()
maxi = 0
for i in range(len(s)-4):
    # r = s[i] + s[i+1] + s[i+2] + s[i+3] + s[i+4]
    r = ''.join(s[i:i+5])[:-1]
    if r.count('C') == 2 and r.count('D') == 2:
        maxi = max(maxi, len(r))
print(maxi)

#
s = open('24.txt').readline()
s = s.replace('C', 'C ').replace('D', 'D ').split()
maxi = 0
for i in range(len(s)-4):
    r = s[i] + s[i+1] + s[i+2] + s[i+3] + s[i+4][:-1]
    if r.count('C') == 2 and r.count('D') == 2:
        maxi = max(maxi, len(r))
print(maxi)
'''
# Ответ: 253


# максимальное количество идущих подряд символов среди которых символ "T' встречается ровно 3 раза
'''
s = 'xxxxxxxxxxxxxTxxxxxTxxxxxxxTxxxxxTxxxTxxxxxxxxxxxTxxxxxxxxxxTxxxxxxxxxx'
# ['xxxxxxxxxxxxx', 'xxxxx', 'xxxxxxx', 'xxxxx', 'xxx', 'xxxxxxxxxxx', 'xxxxxxxxxx', 'xxxxxxxxxx']
# xxxxxxxxxxxxxTxxxxxTxxxxxxxTxxxxx 33
# xxxxxTxxxxxxxTxxxxxTxxx 23
# xxxxxxxTxxxxxTxxxTxxxxxxxxxxx 29
# xxxxxTxxxTxxxxxxxxxxxTxxxxxxxxxx 32
# xxxTxxxxxxxxxxxTxxxxxxxxxxTxxxxxxxxxx 37
s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    # r = s[i] + 'T' + s[i+1] + 'T' + s[i+2] + 'T' + s[i+3]
    r = 'T'.join(s[i:i+4])
    print(r, len(r))
    maxi = max(maxi, len(r))
print(maxi)
'''


# Тип 24 №60266
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ T встречается ровно 100 раз.
'''
s = open('24.txt').readline().split('T')
maxi = 0
for i in range(len(s)-100):
    r = 'T'.join(s[i:i+101])
    maxi = max(maxi, len(r))
print(maxi)
'''
# Ответ: 133


# минимальное количество идущих подряд символов среди которых символ "T' встречается ровно 3 раза
'''
s = 'xxxxxxxxxxxxxTxxxxxTxxxxxxxTxxxxxTxxxTxxxxxxxxxxxTxxxxxxxxxxTxxxxxxxxxx'
# ['xxxxxxxxxxxxx', 'xxxxx', 'xxxxxxx', 'xxxxx', 'xxx', 'xxxxxxxxxxx', 'xxxxxxxxxx', 'xxxxxxxxxx']
# TxxxxxxxxxxxxxTxxxxxT 21
# TxxxxxTxxxxxxxT 15
# TxxxxxxxTxxxxxT 15
# TxxxxxTxxxT 11
# TxxxTxxxxxxxxxxxT 17
# TxxxxxxxxxxxTxxxxxxxxxxT 24
# TxxxxxxxxxxTxxxxxxxxxxT 23

s = s.split('T')
mini = 99999
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    print(r, len(r))
    mini = min(mini, len(r))
print(mini)

'''


# Тип 24 №59793
# Текстовый файл состоит не более чем из 106 символов латинского алфавита.
# Определите минимальную подстроку, содержащую 120 символов "V".
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline().split('V')
mini = 999999
for i in range(len(s)-118):
    r = 'V' + 'V'.join(s[i:i+119]) + 'V'
    mini = min(mini, len(r))
print(mini)
'''
# Ответ: 1820


# Тип 24 №29672
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество строк, в которых буква E встречается чаще, чем буква A.
'''
s = open('24.txt').readlines()
cnt = 0
for x in s:
    if x.count('E') > x.count('A'):
        cnt += 1
print(cnt)
'''
# Ответ: 467


# Тип 24 №35998
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# В строках, содержащих менее 25 букв A, нужно определить и вывести максимальное
# расстояние между одинаковыми буквами в одной строке.

s = open('24.txt').readlines()
maxi = 0
for x in s:
    if x.count('A') < 25:
        for a in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            maxi = max(maxi, x.rindex(a) - x.index(a))
print(maxi)





# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Дмитрий = [2, 5, 8, 9, 12, 13, 14, 15, 16, 17, 23, 24.1, 25]
# КЕГЭ  = []
# на следующем уроке: На следующем уроке рассматриваем сложыне 24 номера
