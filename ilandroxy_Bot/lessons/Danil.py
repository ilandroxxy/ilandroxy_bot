# region Домашка: ******************************************************************

# КЕГЭ № 6636 Пробник ИМЦ СПб (Уровень: Базовый)
#
# Текстовый файл состоит из цифр 1, 2, 3, 4 и 5.
# Определите максимальное количество идущих подряд пар символов вида: четная цифра + нечетная цифра в прилагаемом файле.
'''
s = open('24.txt').readline()
s = s.replace('4', '2').replace('3', '1').replace('5', '1')
s = s.replace('21', '*')
s = s.replace('1', ' ').replace('2', ' ')
print(max([len(x) for x in s.split()]))
'''


# КЕГЭ № 6094 /dev/inf 02.2023 (Уровень: Средний) (А. Рогов)
# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд пар символов
# вида согласная + гласная среди которых нет подстроки XYZY.
'''
s = open('24.txt').readline()
s = s.replace('XY', '*').replace('ZY', '+')
for a in 'XYZ':
    s = s.replace(a, ' ')
s = s.replace('*+', '* +')
print(max([len(x) for x in s.split()]))
'''
'''
s = open('24.txt').readline()
s = s.replace('XY', '*').replace('ZY', '+')
for a in 'XYZ':
    s = s.replace(a, ' ')
print(max([len(x) for x in s.replace('*+', '* +').split()]))
'''
# Ответ: 8

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# Тип 24 №40740
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC...Z).
# Определите максимальное количество идущих подряд символов,
# среди которых нет ни одной буквы A и при этом не менее трёх букв E.
'''
s = open('24.txt').readline().split('A')
print(max([len(x) for x in s if x.count('E') >= 3]))


s = open('24.txt').readline()
s = s.replace('A', ' ')
print(max([len(x) for x in s.split() if x.count('E') >= 3]))
'''
# Ответ: 282


# Тип 24 №38958
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов,
# среди которых не более одной буквы A
'''
s = open('24.txt').readline().split('A')
maxi = 0
for i in range(len(s)-1):
    r = s[i] + 'A' + s[i+1]
    maxi = max(maxi, len(r))
print(maxi)
'''
# Ответ: 337


# Тип 24 №61404
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых ровно
# по одному разу встречаются буквы X и Y.
'''
s = open('24.txt').readline()
s = s.replace('X', 'X ').replace('Y', 'Y ').split()
maxi = 0
for i in range(len(s)-2):
    r = s[i] + s[i + 1] + s[i+2][:-1]
    if r.count('X') == 1 and r.count('Y') == 1:
        maxi = max(maxi, len(r))
print(maxi)
'''
# Ответ: 224


# № 13100 (Уровень: Средний)
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите максимальное количество идущих подряд символов, среди которых
# каждая из букв C и D встречается не более двух раз.
'''
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

# Максимальное количество идущих подряд символов, среди которых символ T встречается ровно 3 раза
'''
s = 'xxxxxxxTxxxxTxxTxxxxTxxxxTxxxxxxTxxxxxxxxxTxxxxxxxxxx'.split('T')
# ['xxxxxxx', 'xxxx', 'xx', 'xxxx', 'xxxx', 'xxxxxx', 'xxxxxxxxx', 'xxxxxxxxxx']
# xxxxxxxTxxxxTxxTxxxx 20
# xxxxTxxTxxxxTxxxx 17
# xxTxxxxTxxxxTxxxxxx 19
# xxxxTxxxxTxxxxxxTxxxxxxxxx 26
# xxxxTxxxxxxTxxxxxxxxxTxxxxxxxxxx 32
maxi = 0
for i in range(len(s)-3):
    # r = s[i] + 'T' + s[i+1] + 'T' + s[i+2] + 'T' + s[i+3]
    r = 'T'.join(s[i:i+4])
    print(r, len(r))
    maxi = max(maxi, len(r))
print(maxi)
'''
# 32


# Минимальное количество идущих подряд символов, среди которых символ T встречается ровно 3 раза
'''
s = 'xxxxxxxTxxxxTxxTxxxxTxxxxTxxxxxxTxxxxxxxxxTxxxxxxxxxx'.split('T')
# ['xxxxxxx', 'xxxx', 'xx', 'xxxx', 'xxxx', 'xxxxxx', 'xxxxxxxxx', 'xxxxxxxxxx']
# TxxxxxxxTxxxxT 14
# TxxxxTxxT 9
# TxxTxxxxT 9
# TxxxxTxxxxT 11
# TxxxxTxxxxxxT 13
# TxxxxxxTxxxxxxxxxT 18
# TxxxxxxxxxTxxxxxxxxxxT 22
mini = 99999
for i in range(len(s)-1):
    r = 'T' + s[i] + 'T' + s[i+1] + 'T'
    print(r, len(r))
    mini = min(mini, len(r))
print(mini)
'''

# № 10105 Демоверсия 2024 (Уровень: Средний)
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


# № 11954 (Уровень: Средний)
# (PRO100 ЕГЭ) Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле минимальное количество идущих подряд
# символов (длину непрерывной подпоследовательности), среди которых
# символ X встречается не менее 500 раз, а символ Y не встречается совсем.
'''
s = open('24.txt').readline().split('X')
mini = 99999
for i in range(len(s)-498):
    r = 'X' + 'X'.join(s[i:i+499]) + 'X'
    if 'Y' not in r:
        mini = min(mini, len(r))
print(mini)
'''
# Ответ: 68500


# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Данил = [2, 5, 6, 8, 9, 12, 14, 15, 16, 17, 23, 24]
# КЕГЭ  = []
# на следующем уроке: Разобрать 25 и 13 номера
