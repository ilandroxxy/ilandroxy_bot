# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 25 №59703
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# 1) символ «?» означает ровно одну произвольную цифру;
# 2) символ «*» означает любую последовательность — цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
#
# Среди натуральных чисел, не превышающих 10**8, найдите все числа,
# соответствующие маске 3?1*57, делящиеся на 2023 без остатка.

# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце — соответствующие им результаты деления этих чисел на 2023.
# Количество строк в таблице для ответа избыточно.
'''
from fnmatch import *
for x in range(2023, 10**8, 2023):  # не превышающих 10**8 and делящиеся на 2023 без остатка
    if fnmatch(str(x), '3?1*57'):
        print(x, x // 2023)
        # 321657 159
        # 34105757 16859
        # 35117257 17359
        # 36128757 17859
        # 37140257 18359
        # 38151757 18859
        # 39163257 19359
'''

# Тип 25 №61405
# Маска числа — это последовательность цифр, в которой могут встречаться специальные символы «?» и «*».
# Символ «?» означает ровно одну произвольную цифру, символ «*» означает произвольную (в том числе пустую)
# последовательность цифр. Найдите все натуральные числа,
# не превышающие 10**10, которые соответствуют маске 3?2258*4 и при этом без остатка делятся на 2024.
# В ответе запишите все найденные числа в порядке возрастания.
'''
from fnmatch import *
for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '3?2258*4'):
        print(x)
'''
# 3422584
# 352258984
# 3022582904
# 3122588744
# 3222584464
# 3322580184
# 3422586024
# 3522581744
# 3622587584
# 3722583304
# 3822589144
# 3922584864


# № 12477 PRO100 ЕГЭ 29.12.23 (Уровень: Средний)
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
#
# символ «?» означает ровно одну произвольную цифру;
# символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
#
# Среди натуральных чисел, не превышающих 10**7, найдите все простые числа, соответствующие маске 3?1111*.
# В ответе запишите все найденные числа в порядке возрастания.
# Количество строк в таблице для ответа избыточно.
'''
def prime(x): # 12
    if x == 1:
        return False
    for j in range(2, x):
        if x % j == 0:
            return False
    return True


print(prime(24))
print(prime(11))
'''


#
# № 11672 (Уровень: Базовый)
# (Л. Шастин) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# — символ «?» означает ровно одну произвольную цифру;
# — символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.

# Среди натуральных чисел, не превышающих 10**10, найдите все числа, соответствующие маске 12*34?5,
# делящиеся на 21025 без остатка и состоящие из одинакового количества чётных и нечётных цифр.

# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце — соответствующие им результаты деления этих чисел на 21025.


#
# № 3901 Джобс 14.05.2022 (Уровень: Базовый)
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# — символ «?» означает ровно одну произвольную цифру;
# — символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
#
# Найдите 5 минимальных чисел, больших 700000, которые кратны 13
# и не подходят ни под одну из трех масок: *0??3*, *4??2 и *1*.
# Найденные числа запишите в порядке возрастания, справа от каждого найденного числа укажите сумму значений разрядов.


sum([int(a) for a in str(x)])

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Лиза = [1, 2, 4, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 23, 24, 25]
# КЕГЭ  = []
# на следующем уроке:
