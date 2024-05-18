# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 25 №48473
# Маска числа — это последовательность цифр, в которой могут встречаться
# специальные символы «?» и «*». Символ «?» означает ровно одну произвольную цифру,
# символ «*» означает произвольную (в том числе пустую) последовательность цифр.
#
# Пример. Маске 123*4?5 соответствуют числа 123405 и 12376415.
#
# Найдите все натуральные числа, не превышающие 10**10, которые соответствуют
# маске 1?954*21 и при этом без остатка делятся на 3023.
'''
from fnmatch import *

for x in range(3023, 10**10, 3023):
    if fnmatch(str(x), '1?954*21'):
        print(x, x // 3023)
'''

# КЕГЭ № 9710 (Уровень: Средний)
# Назовём маской числа последовательность цифр,
# в которой также могут встречаться следующие символы:
#
# символ «?» означает ровно одну произвольную цифру;
# символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
# Найдите десятиразрядные числа кратные 2023 с максимальной суммой
# цифр и отвечающие маске «1*1». В ответ
# запишите частное от деления на 2023 пяти наибольших таких чисел в порядке возрастания.

import time
start = time.time()
from fnmatch import *
R = []
for x in range(9999998519, 10**9, -2023):
    if len(str(x)) == 10:
        if fnmatch(str(x), '1*1'):
            R.append([sum(map(int, str(x))), x // 2023])

R = sorted(R)
print(R[-5][1])
print(R[-4][1])
print(R[-3][1])
print(R[-2][1])
print(R[-1][1])

print(time.time() - start)

# endregion Урок: **********************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Михаил = [2, 5, 6, 8, 12, 14, 15, 16, 23]
# КЕГЭ  = []
# на следующем уроке:
