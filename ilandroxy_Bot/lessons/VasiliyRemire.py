
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 25 №27855
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [95632; 95700],
# числа, имеющие ровно шесть различных чётных натуральных делителей
# (при этом количество нечётных делителей может быть любым).
# Для каждого найденного числа запишите эти шесть делителей в шесть соседних столбцов на экране с новой строки.
# Делители в строке должны следовать в порядке возрастания.
'''
def divisors(num):
    div = set()
    for j in range(1, int(num**0.5)+1):
        if num % j == 0:
            if j % 2 == 0:
                div.add(j)
            if (num // j) % 2 == 0:
                div.add(num // j)
    return sorted(div)


for n in range(95632, 95700+1):
    d = divisors(n)
    if len(d) == 6:
        print(*d)
'''
# Ответ:
# 2 10 50 3826 19130 95650
# 2 26 338 566 7358 95654
# 2 4 8 23918 47836 95672

# from time import time
# start = time()

'''
def divisors(num):
    div = []
    for j in range(1, num+1):
        if num % j == 0:
            div.append(j)
    return div


print(divisors(100_000_000))

end = time() - start
print(end)  # 0.29619503021240234
'''

'''
def divisors(num):
    div = set()
    for j in range(1, int(num**0.5)+1):
        if num % j == 0:
            div.add(j)
            div.add(num // j)
    return sorted(div)


print(divisors(100_000_000))


end = time() - start
print(end)  # 0.00033092498779296875


print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(24 / 4)  # 6.0
print(24 / 6)  # 4.0
print(divisors(16))  # [1, 2, 4, 8, 16]
'''



# Тип 25 №61405
# Маска числа — это последовательность цифр, в которой могут встречаться специальные символы «?» и «*».
# Символ «?» означает ровно одну произвольную цифру,
# символ «*» означает произвольную (в том числе пустую) последовательность цифр.
#
# Найдите все натуральные числа, не превышающие 10**10,
# которые соответствуют маске 3?2258*4 и при этом без остатка делятся на 2024.
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


def divisors(num):
    div = set()
    for j in range(1, int(num**0.5)+1):
        if num % j == 0:
            div.add(j)
            div.add(num // j)
    return sorted(div)


# Тип 25 №27856
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [95632;95650],
# числа, имеющие ровно шесть различных нечётных натуральных делителей (при этом количество четных
# делителей может быть любым). Для каждого найденного числа запишите эти шесть делителей
# в шесть соседних столбцов на экране с новой строки.
# Делители в строке должны следовать в порядке возрастания.
'''
def divisors(num):
    div = set()
    for j in range(1, int(num**0.5)+1):
        if num % j == 0:
            div.add(j)
            div.add(num // j)
    return [x for x in sorted(div) if x % 2 != 0]


for x in range(95632, 95650+1):
    d = divisors(x)
    if len(d) == 6:
        print(*d)
'''
# 1 3 9 10627 31881 95643
# 1 7 49 61 427 2989
# 1 5 25 1913 9565 47825


# Тип 25 №28124
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [568023; 569230],
# число, имеющее максимальное количество различных натуральных делителей,
# если таких чисел несколько — найдите минимальное из них.
# Выведите на экран количество делителей такого числа и само число.
'''
def divisors(num):
    div = set()
    for j in range(1, int(num**0.5)+1):
        if num % j == 0:
            div.add(j)
            div.add(num // j)
    return sorted(div)


maxi = 0
r = 0
for x in range(568023, 569230+1):
    d = divisors(x)
    if maxi < len(d):
        maxi = len(d)
        r = x
print(maxi, r)

'''
# 144 568260


# Тип 25 №28120
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому
# отрезку [201455; 201470], числа, имеющие ровно 4 различных натуральных делителя.
# Выведите эти четыре делителя для каждого найденного числа в порядке возрастания.

def F(num):
    div = set()
    for j in range(1, int(num**0.5)+1):
        if num % j == 0:
            div.add(j)
            div.add(num // j)
    return sorted(div)


for x in range(201455, 201470+1):
    d = F(x)
    if len(d) == 4:
        print(*d)

# 1 3 67153 201459
# 1 13 15497 201461
# 1 29 6947 201463
# 1 2 100733 201466

# endregion Урок: ******************************************************************


# Василий = [2.1, 3.1, 5.1, 6.1, 8.1, 12.1, 14.1, 15.1, 16.1, 17.1, 19-21.1, 22.1, 23.1, 24.1, 25.1]
# КЕГЭ  = []
# на следующем уроке: Разбираем 18 номер
