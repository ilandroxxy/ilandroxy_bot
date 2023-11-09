
# region Домашка: ******************************************************************

# № 2573 (Уровень: Средний)
# Дана программа для исполнителя Редактор:
#
# ПОКА нашлось(55555)
#    заменить(55555, 88)
#    заменить(888, 55)
# КОНЕЦ ПОКА
# Известно, что начальная строка состоит более чем из 300 цифр 5 и не содержит других цифр.
# При какой наименьшей длине исходной строки результат работы этой программы будет содержать
# наибольшее возможное число цифр 5?
'''
R = []
maxi = 0
for i in range(301, 500):
    s = i * '5'
    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '55', 1)
    if maxi < s.count('5'):
        maxi = s.count('5')
        R.append(i)
        # print(i, maxi)
print(max(R))
'''


# № 5632 (Уровень: Средний) (М. Ишимов)
#
# Операнды арифметического выражения записаны в системе счисления с основанием 21.
#
# 32yxA_21 + 16y18_21
#
# В записи чисел переменными х и у обозначены две неизвестные цифры из алфавита
# 21-ричной системы счисления. Определите наименьшее значение х, при котором значение
# данного арифметического выражения кратно 12_10 при любом нечётном значении у.
# Для найденного значения х вычислите частное от деления
# значения арифметического выражения на 12_10 при у = 7
# и укажите его в ответе в десятичной системе счисления.
# Основание системы счисления в ответе указывать не нужно.
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for x in alphabet[:21]:
    if all((int(f'32{y}{x}A', 21) + int(f'16{y}18', 21)) % 12 == 0 for y in alphabet[1:21:2]):
        print((int(f'32{7}{x}A', 21) + int(f'16{7}18', 21)) // 12)
        break
'''

'''
import math as m
print(m.lcm(4, 20))

from math import *  # лучше так не подключать библиотеки 

def lcm(a, b):
    return None
'''

'''
maxi = 0
print(max([1, 2, 3, 4]))
'''

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Тип 8 №8658
# Все 5-буквенные слова, составленные из букв А, Н, П, записаны в алфавитном порядке.
#
# Вот начало списка:
# 1. ААААА
# 2. ААААН
# 3. ААААП
# 4. АААНА
# 5. АААНН
#
# Запишите слово, которое стоит на 201-м месте от начала списка.
'''
s = sorted('АНП')
# print(s)  # ['А', 'Н', 'П']
k = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if k == 201:
                        print(k, slovo)
                    k += 1

# Вариант 2
from itertools import product
k = 1
for s in product(sorted('АНП'), repeat=5):
    slovo = ''.join(s)
    if k == 201:
        print(k, slovo)
    k += 1
'''
# Ответ: ПННАП


# Тип 8 №19059
# Все 4-буквенные слова, в составе которых могут быть буквы Н, О, Т, К, И,
# записаны в алфавитном порядке и пронумерованы, начиная с 1.
#
# Ниже приведено начало списка.
# 1. ИИИИ
# 2. ИИИК
# 3. ИИИН
# 4. ИИИО
# 5. ИИИТ
# 6. ИИКИ
#
# Под каким номером в списке идёт первое слово, которое начинается с буквы О?
'''
from itertools import product
k = 1
for s in product(sorted('НОТКИ'),  repeat=4):
    slovo = ''.join(s)
    if slovo[0] == 'О':
        print(k, slovo)
        break
    k += 1
'''
# Ответ: 376


# Указал на ошибку в условии 59744

# Тип 8 №59744
# Евгений составляет 6-буквенные слова из букв М, У, Ж, Ч, И, Н, А.
# Каждая из букв может встречаться в слове ровно один раз, причём первой буквой не может быть Ч,
# буква Ж должна встречаться не менее 1 раза и номер слова должен быть нечётный.
#
# Сколько различных слов может составить Евгений?
'''
from itertools import permutations
count = 0
k = 1
for s in permutations('МУЖЧИНА', 6):
    slovo = ''.join(s)
    if slovo[0] != 'Ч' and slovo.count('Ж') >= 1:
        k += 1
        if k % 2 != 0:
            count += 1
print(count)

# Вариант 2
s = 'МУЖЧИНА'
k = 1
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if len(set(slovo)) == len(slovo):
                            if slovo[0] != 'Ч' and slovo.count('Ж') >= 1:
                                k += 1
                                if k % 2 != 0:
                                    count += 1
print(count)
'''
# Ответ: Ответ: 1860


# Тип 8 №48456
# Определите количество шестизначных чисел, записанных в девятеричной системе счисления,
# в записи которых ровно одна цифра 4 и ровно две нечётные цифры.
'''
s = '012345678'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        num = a + b + c + d + e + f
                        if num[0] != '0' or a != '0':
                            if num.count('4') == 1:
                                nechet = [int(x) for x in num if int(x) % 2 != 0]
                                if len(nechet) == 2:
                                    # print(num, nechet)
                                    count += 1
print(count)

# Вариант 2
from itertools import product
count = 0
for s in product('012345678', repeat=6):
    num = ''.join(s)
    if num[0] != '0':
        if num.count('4') == 1:
            nechet = [int(x) for x in num if int(x) % 2 != 0]
            if len(nechet) == 2:
                # print(num, nechet)
                count += 1
print(count)
'''
# Ответ: 53760


# Отправил новый вариант решения на Решу ЕГЭ

# Тип 8 №27009
# Николай составляет 4-буквенные коды из букв Н, И, К, О, Л, А, Й.
# Каждую букву можно использовать любое количество раз, при этом код не может начинаться с буквы Й
# и должен содержать хотя бы одну гласную.
# Сколько различных кодов может составить Николай?
'''
# Вариант 1
from itertools import product
count = 0
for s in product('НИКОЛАЙ', repeat=4):
    slovo = ''.join(s)
    if slovo[0] != 'Й':
        if any(x in slovo for x in 'ИОА'):
            count += 1
print(count)

# Вариант 2
s = 'НИКОЛАЙ'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                slovo = a + b + c + d
                if slovo[0] != 'Й':
                    if any(x in slovo for x in 'ИОА'):
                        print(slovo)
                        count += 1
print(count)
'''
# Ответ: 1866


# Сообщил об ошибке на Решу ЕГЭ
# Тип 8 №58237
# Сколько существует различных четырёхзначных чисел, записанных в семеричной системе счисления,
# в записи которых цифры следуют слева направо в строго убывающем порядке?


# Каждую цифру можно использовать только один раз*
'''
from itertools import product
count = 0
for num in product('0123456', repeat=4):
    if list(num) == sorted(num, reverse=True):
        print(num)
        count += 1
print(count)


from itertools import permutations
count = 0
for num in permutations('0123456', 4):
    if list(num) == sorted(num, reverse=True):
        print(num)
        count += 1
print(count)
'''
'''
from itertools import product
alphabet = '0123456'
ap=[]
for i in product(alphabet, repeat=4):
    if i[0] > i[1] > i[2] > i[3]:  # Каждую цифру можно использовать только один раз*
        ap.append(i)
print(len(ap))
'''
# Ответ: 35 / 210


# Тип 8 №47005
# Светлана составляет коды из букв слова ПАРАБОЛА. Код должен состоять из 8 букв,
# и каждая буква в нём должна встречаться столько же раз, сколько в заданном слове.
# Кроме того, в коде не должны стоять рядом две гласные и две согласные буквы.
# Сколько кодов может составить Светлана?
'''
from itertools import permutations

P = []
for s in permutations('ПРБЛ', 2):
    pair = ''.join(s)
    P.append(pair)

count = set()
for s in permutations('ПАРАБОЛА', 8):
    slovo = ''.join(s)
    if all(pair not in slovo for pair in ['АА', 'АО', 'ОА'] + P):
        count.add(slovo)
print(len(count))
'''
# Ответ: 192

# Тип 8№ 59832
# Игорь составляет пятизначные числа, используя цифры девятеричной системы счисления. Сколько различных чисел
# может составить Игорь, в которых ровно две цифры 3 и нечётные цифры не стоят рядом с цифрой 2?
'''
count = 0
s = '012345678'
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    num = a + b + c + d + e
                    if num[0] != '0':
                        if num.count('3') == 2:
                            if all(pair not in num for pair in '12 21 32 23 52 25 72 27'.split()):
                                count += 1
print(count)
'''
# Ответ: 3352


# № 9777 Основная волна 20.06.23 (Уровень: Базовый)
# Все пятибуквенные слова, составленные из букв К, О, М, П, Ь, Ю, Т, Е, Р,
# записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
# 1. ЕЕЕЕЕ
# 2. ЕЕЕЕК
# 3. ЕЕЕЕМ
# 4. ЕЕЕЕО
# 5. ЕЕЕЕП
# 6. ЕЕЕЕР
# 7. ЕЕЕЕТ
# 8. ЕЕЕЕЬ
#
# Под каким номером в списке стоит последнее слово с нечётным номером, которое не начинается с буквы Ь
# и содержит ровно две буквы К?
'''
s = sorted('КОМПЬЮТЕР')
k = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    slovo = a + b + c + d + e
                    if k % 2 != 0 and slovo[0] != 'Ь' and slovo.count('К') == 2:
                        print(k, slovo)
                    k += 1
'''
# Ответ: 58979

'''
# print(help(range))
print(range.__doc__)
'''
# range(stop) -> range object
# range(start, stop[, step]) -> range object
#
# Return an object that produces a sequence of integers from start (inclusive)
# to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
# start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
# These are exactly the valid indices for a list of 4 elements.
# When step is given, it specifies the increment (or decrement).

'''
def Prime(x: int) -> bool:
    """
    Функция Prime проверяет число и дает ответ, простое оно или составное
    :param x: Принимает целое число x
    :return: Возвращает bool значение: True - если простое, False - если составное
    """
    for j in range(2, x):
        if x % j == 0:
            return False
    return True

result = Prime(7)
print(result)
'''
'''
print(Prime.__doc__)
'''
#   Функция Prime проверяет число и дает ответ, простое оно или составное
#   :param x: Принимает целое число x
#   :return: Возвращает bool значение: True - если простое, False - если составное


# Напишем свою функцию Суммы
''''
M = [1, 2, 3]
print(max(M))
print(sum(M))

print(max(1, 2, 3))
# print(sum(1, 2, 3)) - не работает
# TypeError: sum() takes at most 2 arguments (3 given)

def my_summ(*args):
    summ = 0
    for x in args:
        summ += x
    return summ
    # return sum(args)


print(my_summ(1, 2, 3))
'''


# Функция поиска делителей числа:
'''
def Divisors(x: int) -> list:   # 24
    divisors = []
    for j in range(1, x+1):
        if x % j == 0:
            divisors.append(j)
    return divisors


def Modified_Divisors(x: int) -> list:   # 24
    divisors = set()
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            divisors.add(j)
            divisors.add(x // j)
    return sorted(divisors)


print(Divisors(24))   # [1, 2, 3, 4, 6, 8, 12, 24]
print(Modified_Divisors(16))

for n in range(1000000000, 1000000100):
    print(n, len(Modified_Divisors(1000000000)))

print(Modified_Divisors(1000000000))
print(Divisors(1000000000))
'''

# endregion Урок: ******************************************************************


# GOAL = [2.1, 5.1, 6.1, 8.1, 12.1, 14.1]
# КЕГЭ  = []
# на следующем уроке:
