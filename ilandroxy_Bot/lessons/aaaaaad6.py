# region Домашка: ******************************************************************

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


# Тип 24 №52195
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
# Ответ: 255
# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 24 №33196
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле сразу после буквы A.
'''
s = open('24.txt').readline()
R = []
for i in range(len(s)-1):
    if s[i] == 'A':
        R.append(s[i+1])

M = []
for x in set(R):
    M.append([R.count(x), x])

print(max(M))  # [1555, 'G']
print(max(M)[1])  # G
'''
# Ответ: G


# Тип 24 №36879
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# В строках, содержащих менее 25 букв G, нужно определить
# и вывести максимальное расстояние между одинаковыми буквами в одной строке.
'''
s = open('24.txt').readlines()
maxi = 0
for x in s:
    if x.count('G') < 25:
        for a in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            maxi = max(maxi, x.rindex(a) - x.index(a))
print(maxi)
'''
# Ответ: 1001


# Тип 24№35913
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# Необходимо найти строку, содержащую наименьшее количество букв N
# (если таких строк несколько, надо взять ту, которая находится в файле раньше),
# и определить, какая буква встречается в этой строке чаще всего.
# Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.
'''
s = open('24.txt').readlines()
mini = 999999999
r = ''
for x in s:
    if mini > x.count('N'):
        mini = x.count('N')
        r = x

for a in sorted('QWERTYUIOPASDFGHJKLZXCVBNM'):
    print(a, r.count(a))
'''
# Ответ: Y


# Тип 24 №33769
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле после двух одинаковых символов.
'''
s = open('24.txt').readline()
R = []
for i in range(len(s)-2):
    if s[i] == s[i+1]:
        R.append(s[i+2])

M = []
for a in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    M.append([R.count(a), a])

print(max(M))
'''
# Ответ: K


# Тип 24 №60266
# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ T встречается ровно 3 раз.


# xxxTxxxxxTxxxxxTxxxxxxTxxxxTxxxTxxxxTxxxxTxxxxT
# ['xxx', 'xxxxx', 'xxxxx', 'xxxxxx', 'xxxx', 'xxx', 'xxxx', 'xxxx', 'xxxx', '']
# 1. xxxTxxxxxTxxxxxTxxxxxx 22
# 2. xxxxxTxxxxxTxxxxxxTxxxx 23
# 3. xxxxxTxxxxxxTxxxxTxxx 21
# 4. xxxxxxTxxxxTxxxTxxxx 20
# 5. xxxxTxxxTxxxxTxxxx 18
# 6. xxxTxxxxTxxxxTxxxx 18
# 7. xxxxTxxxxTxxxxT 15

'''
s = 'xxxTxxxxxTxxxxxTxxxxxxTxxxxTxxxTxxxxTxxxxTxxxxT'
s = s.split('T')
maxi = 0
for i in range(len(s)-3):
    maxi = max(maxi, len('T'.join(s[i:i+4])))
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
    maxi = max(maxi, len('T'.join(s[i:i+101])))
print(maxi)
'''
# Ответ: 133


# Тип 24 №59790
# Текстовый файл состоит не более чем из 106 символов латинского алфавита.
# Определите минимальную подстроку, содержащую 3 символов "T".
# Для выполнения этого задания следует написать программу.

# xxxTxxxxxTxxxxxTxxxxxxTxxxxTxxxTxxxxTxxxxTxxxxT
# ['xxx', 'xxxxx', 'xxxxx', 'xxxxxx', 'xxxx', 'xxx', 'xxxx', 'xxxx', 'xxxx', '']
# xxxTxxxxx 11
# xxxxxTxxxxx 13
# xxxxxTxxxxxx 14
# xxxxxxTxxxx 13
# xxxxTxxx 10
# xxxTxxxx 10
# xxxxTxxxx 11
# xxxxTxxxx 11

'''
s = 'xxxTxxxxxTxxxxxTxxxxxxTxxxxTxxxTxxxxTxxxxTxxxxT'
s = s.split('T')
mini = 99999999
for i in range(len(s)-2):
    r = 'T'.join(s[i:i+2])
    print(r, len(r) + 2)
    mini = min(mini, len('T'.join(s[i:i+2])) + 2)
print(mini)
'''

# Тип 24 №59790
# Текстовый файл состоит не более чем из 106 символов латинского алфавита.
# Определите минимальную подстроку, содержащую 210 символов "T".
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline().split('T')
mini = 99999999
for i in range(len(s)-209):
    mini = min(mini, len('T'.join(s[i:i+209])) + 2)
print(mini)
'''
# Ответ: 3844


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


# Тип 24 №55641
# Текстовый файл содержит строки различной длины, содержащие только заглавные
# буквы латинского алфавита (ABC…Z). В каждой строке файла определяется буква,
# которая чаще всего стоит сразу после буквы T, эта буква
# заносится в отдельный список.
#
# Если несколько разных букв встречаются
# в строке сразу после Т одинаковое максимальное количество раз, в список заносятся все эти буквы.
# Определите, сколько раз встретится в этом списке самая частая в нём буква.
'''
s = open('24.txt').readlines()
alphabet = sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
R = []
for x in s:
    maxi = 0
    M = []
    for i in range(len(x)-1):
        if x[i] == 'T':
            M.append(x[i+1])
    for a in alphabet:
        maxi = max(maxi, M.count(a))
    for a in alphabet:
        if M.count(a) == maxi:
            R.append(a)

for a in alphabet:
    print(R.count(a), a)
'''


# endregion Урок: ******************************************************************


# Лера = [2.1, 5.1, 6.1, 8.1, 9.1, 12.1, 14.1. 15.1, 16.1, 17.1, 23.1, 24.1, 25.1]
# КЕГЭ  = []
# на следующем уроке:
