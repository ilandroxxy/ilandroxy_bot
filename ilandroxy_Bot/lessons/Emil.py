# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# № 5664 Вариант 09.01.23 (Уровень: Базовый)
# (А. Игнатюк) В каждой строке электронной таблицы содержится 3 натуральных числа.
# Необходимо найти количество строк, где хотя бы одно любое произведение двух чисел оканчивается на 4.
'''
import itertools
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    # if (M[0] * M[1]) % 10 == 4 or (M[0] * M[1]) % 10 == 4 or ...
    if any((A[0] * A[1]) % 10 == 4 for A in itertools.permutations(M, 2)):
        count += 1
print(count)
'''
# Ответ: 965


# № 5670 Вариант 09.01.23 (Уровень: Базовый)
# (М. Ишимов) Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
#
# Обозначим через СУММБОЛ(s, d) утверждение «сумма целых чисел s и d больше 0».
#
# Для какого наименьшего натурального числа А формула
#
# (x + A ≥ 160) \/ (ДЕЛ(x, 7) → ¬СУММБОЛ(x, -17))
#
# тождественно истинна (т.е. принимает значение 1) при любом натуральном значении переменной х?
'''
def F(x, A):
    return (x + A >= 160) or ((x % 7 == 0) <= ((x + (-17)) <= 0))

for A in range(1, 10000):
    flag = True
    for x in range(1, 1000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break

def F(x, A):
    return (x + A >= 160) or ((x % 7 == 0) <= ((x + (-17)) <= 0))

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 1000)):
        print(A)
        break

def F(x, A):
    return (x + A >= 160) or ((x % 7 == 0) <= ((x + (-17)) <= 0))

R = []
for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 1000)):
        R.append(A)
print(min(R))


print(min([A for A in range(1, 1000) if all(((x + A >= 160) or ((x % 7 == 0) <= ((x + (-17)) <= 0))) for x in range(1, 1000))]))
'''
# Показать ответ: 139


# № 5672 Вариант 09.01.23 (Уровень: Базовый)
# (М. Ишимов) В файле содержится последовательность натуральных чисел.
# Элементы последовательности могут принимать целые значения от 1 до 10 000 включительно.
# Определите количество пар последовательности, в которых оба числа не меньше всех чисел последовательности,
# которые кратны 73. Гарантируется, что такой элемент в последовательности есть.
# В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
M = [int(i) for i in open('17.txt')]
A = [i for i in M if i % 73 == 0 and i >= 73]
count = 0
maxi = 0
for i in range(0, len(M)-1):
    if all(M[i] >= x for x in A) and all(M[i+1] >= x for x in A):
        count += 1
        maxi = max(maxi, M[i] + M[i+1])
        if maxi < M[i] + M[i+1]: 
            maxi = M[i] + M[i+1]
print(count, maxi)
'''
'''
s = [int(i) for i in open('17.txt')]
m = 0
c = 0
a = [i for i in s if i % 73 == 0 and i >= 73]
for i in range(0, len(s)-1):
    if all(s[i] >= x for x in a) and all(s[i+1] >= x for x in a):
        c += 1
        if s[i] + s[i+1] > m:
            m = s[i] + s[i]
print(c, m)
'''
# Ответ: 161 19678


# № 5677 Вариант 09.01.23 (Уровень: Средний)
# (А. Игнатюк) В текстовом файле дана последовательность латинских букв.
# Необходимо найти в этой последовательности самую длинную подстроку, состоящую из комбинации DAD,
# при этом первый и последний элементы могут быть неполными. Например ADDADDADDADD.
#
# В ответе укажите количество символов, составляющих наибольшую длину подходящей подстроки.
'''
s = open('24.txt').readline()
print(s)
# Ответ: 99

# DAD
print(len('DADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDA'))

# DDAD
print(len('DDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDA'))

# ADDAD
print(len('ADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDADDA'))
'''


'''
import string
ALPHABET = string.ascii_uppercase
s = open('24.txt').readline()
# s = 'FASEAEANPCVESEAEAEADDNPC'
s = s.replace('EA', '**').replace('NPC', '***')
for x in ALPHABET:
    s = s.replace(x, ' ')
M = [len(i) for i in s.split()]
print(max(M))
'''

'''
print(range.__doc__)
print(help(range))

M = []
print(M.append.__doc__)
print(help(M.append))
'''


# № 5678 Вариант 09.01.23 (Уровень: Средний)
# (М. Ишимов) Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
#
# · символ «?» означает ровно одну произвольную цифру;
# · символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.

# Среди натуральных чисел, не превышающих 10**8, найдите все числа, которые делятся
# на сумму нечётных цифр числа и соответствующие маске 124*5*79.
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце – сумму всех цифр этого числа.
'''
print(10**8)
print('1245**79')

import itertools as it
M = []
for l in range(0, 2+1):
    for s in it.product('0123456789', repeat=l):
        s = ''.join(s)
        M.append(s)

R = []
for x in M:
    for y in M:
        A = int(f'124{x}5{y}79')
        if A < 10 ** 8:
            nechet = sum([int(i) for i in str(A) if int(i) % 2 != 0])
            if A % nechet == 0:
                R.append([A, sum([int(i) for i in str(A)])])

for x in sorted(R):
    print(*x)
'''
# Показать ответ:
# 1249579 37
# 12409579 37
# 12452979 39
# 12456179 35


# endregion Урок: ******************************************************************


# todo: Эмиль = []
# на прошлом уроке: #пробник Пообщались, познакомились. Парень хороший, самоучка и много что умеет решать. Нужно проработать: 3,8,15,17,19-21,24,25,26,27 номера.
# на следующем уроке:
