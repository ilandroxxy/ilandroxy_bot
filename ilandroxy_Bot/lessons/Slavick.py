# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ********************************************************************

# Обычная задача:
# AxxxxxxAxxxxxxxAxxxxxxxA
# AxxxxxxA
# AxxxxxxxA
# AxxxxxxxA

# Наша задача:
# Axxxxxx
# xxxxxxxAxxxxxxx
# xxxxxxxA

# Тип 24 №38958
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых не более одной буквы A.
'''
s = open('24.txt').readline().split('A')
maxi = 0
for i in range(len(s)-1):
    r = s[i] + 'A' + s[i+1]
    maxi = max(maxi, len(r))
print(maxi)
'''
import ast

# Тип 24 №46982
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество групп из идущих подряд не менее 12 символов, которые начинаются
# и заканчиваются буквой E и не содержат других букв E (кроме первой и последней) и букв F.
'''
s = open('24.txt').readline()
s = s.replace('E', 'E E')
print(len([x for x in s.split() if 'F' not in x and len(x) >= 12]))
'''
# Ответ: 9655


# КЕГЭ № 5496 (Уровень: Средний)
# Текстовый файл содержит только буквы A, C, D, F, O.
# Определите длину самой длинной цепочки символов, которая начинается и заканчивается буквой D,
# а между двумя последовательными буквами D содержит не более двух букв O и произвольное количество других букв.
'''
s = open('24.txt').readline().split('D')
count = 1
maxi = 0
for x in s:
    if x.count('O') <= 2:
        count += len(x) + 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''

# Определите максимальную подстроку, содержащую 3 символов "T".
s = 'xxxxxxTxxxxxTxxxxxxxxxTxxxxTxxxxxxTxxxxTxxxxxxxTxxxxxxx'
# ['xxxxxx', 'xxxxx', 'xxxxxxxxx', 'xxxx', 'xxxxxx', 'xxxx', 'xxxxxxx', 'xxxxxxx']
# xxxxxxTxxxxxTxxxxxxxxxTxxxx 27
# xxxxxTxxxxxxxxxTxxxxTxxxxxx 27
# xxxxxxxxxTxxxxTxxxxxxTxxxx 26
# xxxxTxxxxxxTxxxxTxxxxxxx 24
# xxxxxxTxxxxTxxxxxxxTxxxxxxx 27
'''
s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    # r = s[i] + 'T' + s[i+1] + 'T' + s[i+2] + 'T' + s[i+3]
    r = 'T'.join(s[i:i+4])
    maxi = max(maxi, len(r))
print(maxi)
'''

# Определите минимальную подстроку, содержащую 3 символов "T".
s = 'xxxxxxTxxxxxTxxxxxxxxxTxxxxTxxxxxxTxxxxTxxxxxxxTxxxxxxx'
# ['xxxxxx', 'xxxxx', 'xxxxxxxxx', 'xxxx', 'xxxxxx', 'xxxx', 'xxxxxxx', 'xxxxxxx']
# TxxxxxxTxxxxxT 14
# TxxxxxTxxxxxxxxxT 17
# TxxxxxxxxxTxxxxT 16
# TxxxxTxxxxxxT 13
# TxxxxxxTxxxxT 13
# TxxxxTxxxxxxxT 14
# TxxxxxxxTxxxxxxxT 17
'''
s = s.split('T')
mini = 10**9
for i in range(len(s)-1):
    r = 'T' + 'T'.join(s[i:i+2]) + 'T'
    mini = min(mini, len(r))
print(mini)
'''

# Тип 24 №59702
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ Y встречается не более 150 раз.
'''
s = open('24.txt').readline().split('Y')
maxi = 0
for i in range(len(s)-150):
    r = 'Y'.join(s[i:i+151])
    maxi = max(maxi, len(r))
print(maxi)
'''
# Ответ: 244


# Тип 24 №59790
# Текстовый файл состоит не более чем из 106 символов латинского алфавита.
# Определите минимальную подстроку, содержащую 210 символов "T".
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline().split('T')
mini = 10**9
for i in range(len(s)-208):
    r = 'T' + 'T'.join(s[i:i+209]) + 'T'
    mini = min(mini, len(r))
print(mini)
'''
# Ответ: 3844


# Тип 24 №33196
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле сразу после буквы A.
'''
s = open('24.txt').readline()
M = []
for i in range(len(s)-1):
    if s[i] == 'A':
        M.append(s[i+1])

for a in set(M):
    print(a, M.count(a))
'''

'''
s = open('24.txt').readline()
M = []
for i in range(len(s)-1):
    if s[i] == 'A':
        M.append(s[i+1])

R = []
for a in set(M):
    R.append([M.count(a), a])

print(max(R))
print(max(R)[1])
'''


# Тип 24 №33103
# Текстовый файл содержит строки различной длины. Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
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


# Тип 24 №35998
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# В строках, содержащих менее 25 букв A, нужно определить
# и вывести максимальное расстояние между одинаковыми буквами в одной строке.
'''
s = open('24.txt').readlines()
maxi = 0
for x in s:
    if x.count('A') < 25:
        for a in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            maxi = max(maxi, x.rindex(a) - x.index(a))
print(maxi)
'''
# Ответ: 1004


'''
# i    2  5  8
s = '01A34A67A9'
print(s.index('A'))  # 2
print(s.rindex('A'))  # 8
'''


# Тип 24 №55641
# Текстовый файл содержит строки различной длины, содержащие только заглавные буквы латинского алфавита (ABC…Z).
# В каждой строке файла определяется буква, которая чаще всего стоит сразу после буквы T, эта буква
#
# заносится в отдельный список. Если несколько разных букв встречаются в строке сразу после Т одинаковое
# максимальное количество раз, в список заносятся все эти буквы.
#
# Определите, сколько раз встретится в этом списке самая частая в нём буква.
'''
s = open('24.txt').readlines()
R = []
for x in s:
    M = []
    for i in range(len(x)-1):
        if x[i] == 'T':
            M.append(x[i+1])

    maxi = 0
    for a in set(M):
        maxi = max(maxi, M.count(a))

    for a in set(M):
        if M.count(a) == maxi:
            R.append(a)

B = []
for a in set(R):
    B.append(R.count(a))
print(max(B))
'''
# Ответ: 82


# endregion Урок: *************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Славик = [2, 5, 6, 8, 9, 12, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
