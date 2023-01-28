# region Домашка: ************************************************************

# Тип 15 № 39244
# Обозначим через m & n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Так, например, 14 & 5 = 1110_2 & 0101_2 = 0100_2 = 4.
# Для какого наименьшего неотрицательного целого числа А формула (x & 105 = 0) → ((x & 58 ≠ 0) → (x & А ≠ 0))
# тождественно истинна (т.е. принимает значение 1 при любом неотрицательном целом значении переменной x)?

# Вариант 1
'''
def F(x, A):
    # return (x & 105 == 0) <= ((x & 58 != 0) <= (x & A != 0))
    return (x & 105 != 0) or ((x & 58 == 0) or (x & A != 0))

for A in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break
'''

# Вариант 2
'''
for A in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        F = (x & 105 == 0) <= ((x & 58 != 0) <= (x & A != 0))
        if F == False:
            flag = False
            break
    if flag == True:
        print(A)
        break
'''

# Вариант 3
'''
def F(x):
    # return (x & 105 == 0) <= ((x & 58 != 0) <= (x & A != 0))
    return (x & 105 != 0) or ((x & 58 == 0) or (x & A != 0))

for A in range(0, 1000):
    if all(F(x) for x in range(0, 1000)):
        print(A)
        break
'''

# Вариант 4
'''
for A in range(0, 1000):
    flag = True
    for x in range(0, 1000):
        flag = flag and ((x & 105 == 0) <= ((x & 58 != 0) <= (x & A != 0)))
        # flag = flag and ((x & 105 != 0) or ((x & 58 == 0) or (x & A != 0)))
    if flag is True:
        print(A)
        break
'''

# Ответ: 18

# 1. Какого фига мы меняем (x & 105 == 0) на (x & 105 != 0) и (x & 58 ≠ 0) на (x & 58 == 0) и "→"на "or"
#    Если мы не меняем, то ответ 65
# 2. Зачем писать flag = flag and ... если и так же должно работать: flag = ...; if flag is True: print(A)
#    Если так не писать, то ответ первое значение A




# Тип 15 № 35473
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# Для какого наименьшего натурального числа А формула ДЕЛ(A, 45) ∧ (ДЕЛ(750, x) → (¬ДЕЛ(A, x) → ¬ДЕЛ(120, x)))
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?

'''
def Del(n, m):
    return n % m == 0

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if (Del(A, 45) and Del(750, x) <= ((not Del(A, x)) <= (not Del(120, x)))) == False:
            flag = False
            break
    if flag == True:
        print(A)
        quit()
'''

# Вариант 2
'''
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((A % 45 == 0) and (750 % x == 0) <= ((A % x != 0) <= (120 % x != 0))) == False:
            flag = False
            break
    if flag == True:
        print(A)
        quit()
'''

# Вариант 3
'''
def F(x):
    return (A % 45 == 0) and (750 % x == 0) <= ((A % x != 0) <= (120 % x != 0))

for A in range(1, 1000):
    if all(F(x) for x in range(1, 1000)):
        print(A)
        break
'''

# На РешуЕГЭ решение опять кaрдинально отличается:
'''
for A in range(1, 101):
    k = 0
    for x in range(1, 1000):
        if (A % 45 == 0) and ((750 % x == 0) <= ((A % x != 0) <= (120 % x != 0))):
            k += 1
    if k == 999:
        print(A)
        break
'''
# Ответ: 90



# Тип 24 № 36879
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
# В строках, содержащих менее 25 букв G,
# нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.

# Пример. Исходный файл:
# GIGA
# GABLAB
# NOTEBOOK
# AGAAA

# В этом примере во всех строках меньше 25 букв G.
# Самое большое расстояние между одинаковыми буквами — в третьей строке между буквами O,
# расположенными в строке на 2-й и 7-й позициях.
# В ответе для данного примера нужно вывести число 5.

# Вариант 1
"""
f = open('24.txt')
a = [x for x in f.readlines()]
'''
a = open('24.txt').readlines()
#a = ['GIGA', 'GABLAB', 'NOTEBOOK', 'AGAAA']
max_s = 0
for i in range(len(a)):
    if a[i].count('G') < 25:
        for j in range(len(a[i])-1):
            for q in range(j+1, len(a[i])):
                if a[i][j] == a[i][q]:
                    if q - j > max_s:
                        max_s = q - j
#                print(a[i][j], a[i][q], max_s, abs(j - q))
#        print('-------')
print(max_s)
"""


'''
alphabet = sorted([i for i in 'QWERTYUIOPASDFGHJKLZXCVBNM'])
print(alphabet)

import string
print(string.ascii_uppercase)
'''


# Вариант 2
'''
a = open('24.txt').readlines()
M = []
for s in a:
    if s.count('G') < 25:
        M.append(s)

alpahbet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
maxi = 0
for s in M:
    for a in alphabet:
        maxi = max(maxi, s.rindex(a) - s.index(a))
print(maxi)
'''

# Вариант 3
'''
maxi = 0
a = open('24.txt').readlines()
for s in a:
    if s.count('G') < 25:
        for a in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            maxi = max(maxi, s.rindex(a) - s.index(a))
print(maxi)
'''
# Ответ: 1001


# Тип 24 № 33769
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле после двух одинаковых символов.
# Например, в тексте CCCBBABAABCC есть комбинации CCC, CCB, BBA и AAB.
# Чаще всего — 2 раза — после двух одинаковых символов стоит B, в ответе для этого случая надо написать B.

'''
f = open('Файлы/24.txt')
a = [x for x in f.readline()]
#a = [x for x in 'CCCBBABAABCC']
letters = []
for i in range(len(a) - 2):
    if a[i] == a[i+1]:
        letters.append(a[i+2])
#print(letters)

maxim = 0
l = ''
for i in range(len(letters)):
    if letters.count(letters[i]) > maxim:
        maxim = letters.count(letters[i])
        l = letters[i]
print(l)
'''

# Вариант 2
'''
a = open('24.txt').readline()

letters = []
for i in range(len(a) - 2):
    if a[i] == a[i+1]:
        letters.append(a[i+2])

maxim = 0
alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
for a in alphabet:
    if letters.count(a) > maxim:
        maxim = letters.count(a)
        print(a, maxim)
'''
# Ответ: K


# Тип 24 № 27694
# Текстовый файл состоит не более чем из 106 символов A, B и C.
# Определите максимальную длину цепочки вида ABABAB...
# (составленной из фрагментов AB, последний фрагмент может быть неполным).
'''
s = open('24.txt').readline()
print(s)
print(len('ABABABABABABABABABABABAB'))
'''

'''
f = open('Файлы/zadanie24_1.txt')
a = f.readline()
#a = 'ABABACABABAB'

l = []
for i in range(0,len(a)-1, 2):
    l.append(a[i] + a[i+1])
chain, counter, maxim = 'AB', 0, -1
#print(l)

for i in range(len(l)):
    #print(l[i], counter, maxim)
    if l[i] == 'AB':
        counter += 1
        maxim = max(counter, maxim)
    else:
        counter = 0
print(maxim)
'''

'''
f = open('24.txt')

l = f.readline()
l = 'ABABAB'
l = l.replace('AB', '*')
maxim, counter = -1, 0
print(l)
for i in range(len(l)-1):
    if l[i] == '*' and (l[i+1] == 'A' or l[i+1] == 'B'):
        counter += 3
        maxim = max(counter, maxim)
    elif l[i] == '*':
        counter += 2
        maxim = max(counter, maxim)
    else:
        maxim = max(counter, maxim)
        counter = 0

print(maxim)
'''

'''
s = open('24.txt').readline()
# s = 'ABABABABABABABABABABABAB'
count = 1
maxi = 0
for i in range(0, len(s)-1):
    # if (s[i] == 'A' and s[i+1] == 'B') or (s[i] == 'B' and s[i+1] == 'A'):
    if s[i:i+2] == 'AB' or s[i:i+2] == 'BA':
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''
# ничё из этого не работает
# Ответ: 12, должно быть 24

# endregion Домашка: ************************************************************


# region Урок: ************************************************************



# endregion Урок: ************************************************************


# todo: Василий = [2, 5, 6, 8, 12, 14+, 15, 17, 19, 20, 22, 24]
# на прошлом уроке: Разбирали домашку и прорешивали разными способами 15, 24 номера
# на следующем уроке:  Проговорить 9 Пайтон, 15 повторить, 25, Эксель
