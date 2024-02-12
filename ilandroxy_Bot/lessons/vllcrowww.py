# region Домашка: ***************************************************************
'''
s = [int(x) for x in open('17.txt')]
c = max(x for x in s if len(str(abs(x))) == 3)
M = []
for i in range(len(s)-1):
    x, y = s[i], s[i+1]
    # if(s[i]*s[i+1]) % c == 0 and (((100 <= s[i] <= 999) + (100 <= s[i+1] <= 999)) == 1):
    if(x * y) % c == 0 and ((len(str(abs(x))) == 3) + (len(str(abs(y))) == 3)) == 1:
        M.append(x * y)

print(len(M), min(M))
'''
# endregion Домашка: ************************************************************


# region Урок: ******************************************************************

'''
import math

M = [1, 2, 3, 4, 5]
print(sum(M))  # 15
print(math.prod(M))  # 120

print(math.sqrt(16))  # 4.0
print(16 ** (1/2))  # аналог

print(math.factorial(5))  # 120

print(math.fabs(-20))  # 20.0
print(abs(-20))  # аналог

print(math.gcd(12, 24))  # 12  -  НОД
print(math.lcm(12, 24))  # 24  -  НОК

print(math.pi)  # 3.141592653589793

print(math.floor(3.141592))  # 3 - округление вниз
print(math.ceil(3.141592))  # 4 - округление вверх

print(math.ceil.__doc__)
# Return the ceiling of x as an Integral.
#
# This is the smallest integer >= x.
'''

'''
from math import gcd
print(gcd(115, gcd(78, 51)))


from math import gcd
print(gcd(78, gcd(115, 51)))


from math import gcd
print(gcd(115, 78, 51))


from math import gcd
print(gcd(24, 12, 8))
'''


# Тип 9 №52180
# В каждой строке электронной таблицы записаны пять натуральных чисел.
# Определите, сколько в таблице строк, для которых выполнены следующие условия:
# — все числа в строке различны;
# — чётных чисел больше, чем нечётных;
# — сумма чётных чисел меньше суммы нечётных.
# В ответе запишите число — количество строк, для которых выполнены эти условия.
'''
# Для которых выполнены все следующие условия:
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    if len(M) == len(set(M)):  # — все числа в строке различны;
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if len(chet) > len(nechet):
            if sum(chet) < sum(nechet):
                count += 1
print(count)

# Ответ: 241


# Для которых выполнено только одно из условий:
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    flag = 0
    if len(M) == len(set(M)):
        flag += 1
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if len(chet) > len(nechet):
        flag += 1
    if sum(chet) < sum(nechet):
        flag += 1
    if flag == 1:
        count += 1
print(count)

# Ответ: 2608


# Для которых выполнено хотя бы одно из условий:
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    flag = 0
    if len(M) == len(set(M)):
        flag += 1
    chet = [x for x in M if x % 2 == 0]
    nechet = [x for x in M if x % 2 != 0]
    if len(chet) > len(nechet):
        flag += 1
    if sum(chet) < sum(nechet):
        flag += 1
    if flag > 0:
        count += 1
print(count)
'''
# Ответ: 6228


# Тип 9 №63025
# Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# Определите количество строк таблицы, для чисел которых
# одновременно выполнены все следующие условия:
# — в строке есть повторяющиеся числа;
# — максимальное число в строке не повторяется;
# — сумма всех повторяющихся чисел в строке больше максимального числа этой строки.
# При подсчёте суммы повторяющихся чисел каждое число учитывается столько раз, сколько оно встречается.
# В ответе запишите число — количество строк, удовлетворяющих заданным условиям.
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if len(M) != len(set(M)):
        # if M[-1] != M[-2]:
        if M.count(M[-1]) == 1:
            copied = [x for x in M if M.count(x) > 1]
            if sum(copied) > M[-1]:
                count += 1
print(count)

# Вариант 2
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    if len(M) != len(set(M)):
        if M.count(max(M)) == 1:
            copied = [x for x in M if M.count(x) > 1]
            if sum(copied) > max(M):
                count += 1
print(count)
'''
# Ответ: 941


# Тип 9 №47213
# Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# — в строке только одно число повторяется ровно два раза, остальные числа различны;
# — среднее арифметическое неповторяющихся чисел строки не больше суммы повторяющихся чисел.
# В ответе запишите только число.
'''
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    copied = [x for x in M if M.count(x) > 1]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 2:
        if (sum(not_copied) / len(not_copied)) <= (sum(copied)):
            count += 1
print(count)
'''
# Ответ: 2241



# endregion Урок: ******************************************************************


# Марго = [2.1, 5.1, 6.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 17.1, 23.1]
# КЕГЭ  = []
# на следующем уроке:
