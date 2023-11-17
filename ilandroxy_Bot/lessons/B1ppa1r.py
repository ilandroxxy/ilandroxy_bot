# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 8 №59744
# Евгений составляет 6-буквенные слова из букв М, У, Ж, Ч, И, Н, А.
# Каждая из букв может встречаться в слове ровно один раз, причём первой буквой не может быть Ч,
# буква Ж должна встречаться не менее 1 раза и номер слова должен быть нечётный.
# Сколько различных слов может составить Евгений?
'''
s = 'МУЖЧИНА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if len(slovo) == len(set(slovo)):  # Каждая из букв может встречаться в слове ровно один раз
                            if a != 'Ч' and slovo.count('Ж') >= 1:
                                count += 1
print(count / 2)
'''
# Ответ: 1860


# Тип 8 №27295
# Света составляет 5-буквенные коды из букв С, В, Е, Т, А.
# Каждую букву нужно использовать ровно один раз, при этом нельзя ставить рядом две гласные.
# Сколько различных кодов может составить Света?
'''
from itertools import permutations
count = 0
for s in permutations('СВЕТА', 5):
    slovo = ''.join(s)
    if all(pair not in slovo for pair in ['ЕА', 'АЕ']):
        count += 1
print(count)


from itertools import permutations
count = 0
for s in permutations('СВЕТА', 5):
    slovo = ''.join(s)
    if all(pair not in slovo for pair in 'ЕА АЕ'.split()):
        count += 1
print(count)


from itertools import permutations
count = 0
for s in permutations('СВЕТА', 5):
    slovo = ''.join(s)
    if 'ЕА' not in slovo and 'АЕ' not in slovo:
        count += 1
print(count)


from itertools import permutations
count = 0
for s in permutations('СВЕТА', 5):
    slovo = ''.join(s)
    flag = True
    for pair in ['ЕА', 'АЕ']:
        if pair in slovo:
            flag = False
    if flag == True:
        count += 1
print(count)


s = 'СВЕТА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if len(slovo) == len(set(slovo)):
                        if all(pair not in slovo for pair in 'ЕА АЕ'.split()):
                            count += 1
print(count)
'''
# Ответ: 72


# Тип 8 №58475
# Виктор составляет коды из букв, входящих в слово ВИКТОР. Каждая буква должна входить в код ровно один раз.
# Все возможные коды Виктор записывает в алфавитном порядке и нумерует. Начало списка выглядит так
# 1. ВИКОРТ
# 2. ВИКОТР
# 3. ВИКРОТ
#
# Какой код будет записан под номером 266?
'''
from itertools import permutations
k = 1
for s in permutations(sorted('ВИКТОР')):
    slovo = ''.join(s)
    if k == 266:
        print(k, slovo)
    k += 1

import itertools
alphabet = "ВИКОРТ"
ar = itertools.permutations(alphabet)
arl = []
for e in ar:
    arl.append(list(e))
print(*arl[265])
'''
# Ответ: КИВОТР


'''
# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]
# 12 23 34 45

for i in range(len(M)-1):
    print(f'{M[i]}{M[i+1]}', end=' ')
print()

for i in range(len(M)-2):
    print(f'{M[i]}{M[i+1]}{M[i+2]}', end=' ')
print()
'''


# Тип 8 №59742
# Определите количество четырехзначных чисел, записанных в десятичной системе счисления,
# в записи которых все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
'''
# Вариант 1
from itertools import permutations
count = 0
for s in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4):
    if s[0] != 0:
        if all((s[i] + s[i+1]) % 2 == 1 for i in range(len(s)-1)):
            count += 1
print(count)

# Вариант 2
from itertools import permutations
count = 0
for s in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4):
    if s[0] != 0:
        if all(s[i] % 2 != s[i+1] % 2 for i in range(len(s)-1)):
            count += 1
print(count)

# Вариант 3
count = 0
s = '0123456789'
s1 = '13579'
s2 = '02468'
for a in s1:
    for b in s2:
        for c in s1:
            for d in s2:
                slovo = a + b + c + d
                if len(slovo) == len(set(slovo)):
                    count += 1
for a in s2:
    for b in s1:
        for c in s2:
            for d in s1:
                slovo = a + b + c + d
                if a != '0':
                    if len(slovo) == len(set(slovo)):
                        count += 1
print(count)
'''
# Ответ: 720




# endregion Урок: ******************************************************************

# Никита = [5.1, 8.1, 12.1, 14.1]
# КЕГЭ  = []
# на следующем уроке: Продолжаем разбирать 8-ой номер
