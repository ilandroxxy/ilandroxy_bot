# region Домашка: ************************************************************


# endregion Домашка: ************************************************************

# region Урок: ************************************************************
"""
from string import *
alphabet = digits + ascii_uppercase

'''
def convert(number, system):
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    result = ''
    while number > 0:
        result += alphabet[number % system]
        number //= system
    return result[::-1]
'''

def convert(number, system):
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    result = ''
    while number > 0:
        result = alphabet[number % system] + result
        number //= system
    return result


print(convert(8, 2))
"""

# Задание 5
'''
def convert(number, system):
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    result = ''
    while number > 0:
        result = alphabet[number % system] + result
        number //= system
    return result


R = []
for n in range(1, 1000):
    s = convert(n, 3)
    if n % 3 == 0:
        s += s[-2:]
    else:
        x = (n % 3) * 5
        s += convert(x, 3)
    r = int(s, 3)
    if r < 242:
        R.append(r)
print(max(R))
'''


# Задание 12
'''
for n in range(4, 10000):
    s = '5' + '2' * n
    while '72' in s or '522' in s or '2222' in s:
        if '72' in s:
            s = s.replace('72', '22', 1)
        if '522' in s:
            s = s.replace('522', '25', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
    summa = sum([int(x) for x in s if x.isdigit()])
    if summa == 63:
        print(n)
        break
'''

# Поиск суммы цифр строки:
'''
s = 'ferjikfg12345'
summa = sum([int(x) for x in s if x.isdigit()])
print(summa)
'''

# Задание 9
'''
cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    if len([x for x in M if M.count(x) == 2]) == 4:  # те числа, которые имеют пару
        if M.count(max(M)) > 1:
            cnt += 1
print(cnt)
'''
# Ответ: 88


# Вариант 17
'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if abs(x) % 10 == 3 and len(str(abs(x))) == 4]
cnt = 0
maxi = 0
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if sum([abs(p) % 10 == 3 for p in [x, y, z]]) <= 2:
        if (x + y + z) >= min(A):
            cnt += 1
            maxi = max(maxi, x + y + z)
print(cnt, maxi)


M = [int(x) for x in open('17.txt')]
A = [x for x in M if abs(x) % 10 == 3 and len(str(abs(x))) == 4]
R = []
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if sum([abs(p) % 10 == 3 for p in [x, y, z]]) <= 2:
        if (x + y + z) >= min(A):
            R.append(x + y + z)
print(len(R), max(R))
'''
# Ответ: 4335 186619


# Вариант 24

# 'xxxxYxxxxxYxxxxxYxxxxxYxxxxxYxxxxxYxxxxx'  не более 3 раз
# xxxxYxxxxxYxxxxxYxxxxx - максимальное

'''
s = open('24.txt').readline().split('Y')
maxi = 0
for i in range(len(s)-150):
    r = 'Y'.join(s[i:i+151])
    maxi = max(maxi, len(r))
print(maxi)
'''
# Ответ: 1605

# YxxxxxYxxxxxY - минимальное
# _xxxxx_xxxxx_  .split('Y')
# _xxxxxYxxxxx_  'Y'.join(s[i:i+2])
'''
s = open('24.txt').readline().split('Y')
mini = 999999
for i in range(len(s)-148):
    r = 'Y'.join(s[i:i+149])
    mini = min(mini, len(r))
print(mini + 2)
'''
# Ответ: 780


# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# todo № 6091 /dev/inf 02.2023 (Уровень: Базовый)

# Тип 24 №55611 Никита2  и Тип 24 №56552
# Текстовый файл содержит строки различной длины, содержащие только заглавные буквы латинского алфавита (ABC…Z).
# В каждой строке файла определяется буква, которая чаще всего стоит сразу после буквы A,
# эта буква заносится в отдельный список. Если несколько разных букв встречаются в строке сразу после A одинаковое
# максимальное количество раз, в список заносятся все эти буквы.
# Определите, сколько раз встретится в этом списке самая частая в нём буква.
'''
s = open('24.txt').readlines()
alphabet = sorted('QWERTYUIOPASDFGHJKLZXCVBNM')
R = []  # складываем подходящие символы (самые популярные в строке после буквы A)
for x in s:  # пробегаем каждую строку файла
    maxi = 0  # число самого часто встречаемого символы
    M = []  # складываем все символы, стоящие за буквой A
    for i in range(len(x)-1):
        if x[i] == 'A':
            M.append(x[i+1])
    for a in alphabet:
        maxi = max(maxi, M.count(a))
    for a in alphabet:
        if M.count(a) == maxi:
            R.append(a)

B = []
for a in alphabet:
    B.append(R.count(a))

print(max(B))
'''
# Ответ: 82


# endregion Разобрать: *************************************************************

# Никита = [3.1, 5.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 17.1, 19-21.1, 22.1, 23.1, 24.1, 25.1]
# КЕГЭ = []
# на следующем уроке: На следующем уроке рассмотрим 18 номер
