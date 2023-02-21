# region Домашка:  ******************************************************************************

'''
# Тип 24 № 46982 Добавить в вариант
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество групп из идущих подряд не менее 12 символов,
# которые начинаются и заканчиваются буквой E и не содержат других букв E (кроме первой и последней) и букв F.
# Для выполнения этого задания следует написать программу. Ниже приведён файл,
# который необходимо обработать с помощью данного алгоритма.
s = open('24.txt').readline()
s = s.replace('E', ' ')
M = [i for i in s.split() if len(i) >= 12-2 and 'F' not in i]
print(len(M))
# ответ: 9655
'''

'''
# Тип 24 № 38602 Добавить в вариант
# Текстовый файл состоит из символов P, Q, R и S.
# Определите максимальное количество идущих подряд символов в прилагаемом файле,
# среди которых нет идущих подряд символов P.
s = open('24.txt').readline()
count = 1
max_count = 0
for i in range(0, len(s)-1):
    if s[i] == 'P' and s[i-1] == 'P':
        count = 1
    else:
        count += 1
        max_count = max(max_count, count)
print(max_count)
# ответ: 188
'''

'''
# Тип 24 № 36037 Добавить в вариант
# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.
# Для выполнения этого задания следует написать программу
# . Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
s = open('24.txt').readline()
count = 3
max_count = 0
for i in range(0, len(s)-3):
    if s[i:i+4] == 'XZZY':
        count = 3
    else:
        count += 1
        max_count = max(max_count, count)
print(max_count)
# ответ: 1713
'''

# endregion Домашка:  ******************************************************************************



# region Урок:  ******************************************************************************

# Тип 24 № 29672 i
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# Определите количество строк, в которых буква E встречается чаще, чем буква A.
'''
# Вариант 1
S = open('24.txt').readlines()
count = 0
for x in S:
    if x.count('E') > x.count('A'):
        count += 1
print(count)

# Вариант 2
print(len([x for x in open('24.txt').readlines() if x.count('E') > x.count('A')]))
'''
# Ответ: 467


# Тип 24 № 35998
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# В строках, содержащих менее 25 букв A, нужно определить и
# вывести максимальное расстояние между одинаковыми буквами в одной строке.
'''
# Вариант 1
S = open('24.txt').readlines()
M = []
for x in S:
    if x.count('A') < 25:
        M.append(x)

alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'.upper()
maxi = -99999
for x in M:
    for a in alphabet:
        maxi = max(maxi, x.rindex(a)-x.index(a))  # расстояние между одинаковыми буквами
print(maxi)

# Вариант 2
S = open('24.txt').readlines()
maxi = -99999
alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'.upper()
for x in S:
    if x.count('A') < 25:
        for a in alphabet:
            maxi = max(maxi, x.rindex(a) - x.index(a))
print(maxi)
'''
# Ответ: 1004


# Тип 24 № 35482 i
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# Необходимо найти строку, содержащую наименьшее количество букв G
# (если таких строк несколько, надо взять ту, которая находится в файле раньше),
# и определить, какая буква встречается в этой строке чаще всего.
# Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.
'''
S = open('24.txt').readlines()
mini = 99999
r = ''
for x in S:
    if mini > x.count('G'):
        mini = x.count('G')
        r = x

alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'.upper()
maxi = -99999
for a in alphabet:
    if maxi <= r.count(a):
        maxi = r.count(a)
        print(maxi, a)
'''
# Ответ: T





# endregion Урок:  ******************************************************************************


# todo: Екатерина = [2, 3, 5, 8, 9.1, 12, 14+, 15+, 16, 17, 22, 23, 25.2]
# на прошлом уроке: Катя сама прорешала 3 и 22 номера.
# на следующем уроке:


