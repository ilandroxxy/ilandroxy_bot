# region Домашка: ******************************************************************
'''
from string import *
alphabet = digits + ascii_uppercase

def my_convert(number, system):
    alphabet = sorted('0123456789qwertyuiopasdfghjklzxcvbnm')
    s = ''
    while number > 0:
        s += alphabet[number % system]
        number //= system
    return s[::-1]


D = []
for n in range(1, 10000):
    s = my_convert(n, 4)
    if len(s) % 2 == 0:
        s = s[:(len(s)//2)] + '0' + s[(len(s)//2):]
    r = int(s, 4)
    if r <= 180:
        D.append(n)
print(max(D))
'''

'''
cnt = 0
s1 = '1357'
s2 = '2468'
for a in s1:
    for b in s2:
        for c in s1:
            for d in s2:
                for f in s1:
                    for g in s2:
                        for h in s1:
                            for k in s2:
                                for l in s1:
                                    slovo = a + b + c + d + f + g + h + k + l
                                    # if slovo[i] % 2 == 0 and slovo[i + 1] % 2 != 0:
                                    if all(slovo.count(x) <= 3 for x in slovo):
                                        cnt += 1
                                        
print(cnt * 2)
'''

# Среди натуральных чисел, не превышающих 108, найдите все числа, соответствующие маске *15*7424,
# которые делятся без остатка только на одно из чисел 111, 113, 127.
#
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце – соответствующие им результаты деления этих чисел на одно
# из чисел 111, 113, 127, на которое число делится без остатка.
'''
from fnmatch import *
for x in range(0, 10**8):
    if fnmatch(str(x), '*15*7424'):
        M = [p for p in [111, 113, 127] if x % p == 0]
        if len(M) == 1:
            print(x, x // M[0])
'''


'''
R = []
for n in range(4, 10000):
    S = '0' + n * '5'
    while '333' in S or '555' in S:
        if '555' in S:
            S = S.replace('555', '3', 1)
        else:
            S = S.replace('333', '5', 1)
    summa = sum([int(x) for x in S if x.isdigit()])
    R.append(summa)
print(max(R))
'''

'''
maxi = 0
for n in range(4, 10000):
    S = '0' + n * '5'
    while '333' in S or '555' in S:
        if '555' in S:
            S = S.replace('555', '3', 1)
        else:
            S = S.replace('333', '5', 1)
    summa = sum([int(x) for x in S if x.isdigit()])
    if maxi < summa:
        maxi = summa
        print(maxi)
'''

# КЕГЭ № 863 (Уровень: Базовый)
# Текстовый файл состоит не более чем из 10**6 заглавных символов латинского алфавита и цифр.
# Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
'''
s = open('24.txt').readline()
count = 1
maxi = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''


# КЕГЭ № 5496 (Уровень: Средний)
# Текстовый файл содержит только буквы A, C, D, F, O.
# Определите длину самой длинной цепочки символов, которая начинается и заканчивается буквой D,
# а между двумя последовательными буквами D содержит не более двух букв O и произвольное количество других букв.



# endregion Домашка: *****************************************************************


# region Урок: ******************************************************************


# endregion Разобрать: *************************************************************


# Екатерина = [2.1, 5.1, 6.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 17.1, 23.1, 24.1, 25.1]
# КЕГЭ  = []
# на следующем уроке: Начинаем разбирать письменные задачи
