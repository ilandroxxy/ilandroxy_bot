# region Домашка: ************************************************************


# endregion Домашка: ************************************************************


# region Урок: ************************************************************

# region: Задача 9 из пробника Статград 2023
# Вариант 1
# В каждой строке электронной таблицы записаны пять натуральных чисел.
# Определите, сколько в таблице строк, для которых выполнены следующие
# условия:
# – все числа в строке различны;
# – нечётных чисел больше, чем чётных;
# – сумма нечётных чисел меньше суммы чётных.
# В ответе запишите число – количество строк, для которых выполнены эти
# условия.
'''
count = 0
for s in open('9.txt'):
    # M = s.split()
    M = [int(i) for i in s.split()]
    if len(set(M)) == len(M):  # – все числа в строке различны;
        nechet = [i for i in M if i % 2 != 0]
        chet = [i for i in M if i % 2 == 0]
        if len(nechet) > len(chet):  # – нечётных чисел больше, чем чётных;
            if sum(nechet) < sum(chet):  # – сумма нечётных чисел меньше суммы чётных.
                count += 1
                print(M, set(M))
print(count)
'''
# Ответ: 303

# endregion: Задача 9 из пробника Статград 2023

# region: Задача 9 из пробника Статград 2023
# Вариант 2
# В каждой строке электронной таблицы записаны пять натуральных чисел.
# Определите, сколько в таблице строк, для которых выполнены следующие
# условия:
# – все числа в строке различны;
# – чётных чисел больше, чем нечётных;
# – сумма чётных чисел меньше суммы нечётных.
# В ответе запишите число – количество строк, для которых выполнены эти
# условия.
'''
count = 0
for s in open('9.txt'):
    # M = s.split()
    M = [int(i) for i in s.split()]
    if len(set(M)) == len(M):  # – все числа в строке различны;
        nechet = [i for i in M if i % 2 != 0]
        chet = [i for i in M if i % 2 == 0]
        if len(nechet) < len(chet):  # – нечётных чисел больше, чем чётных;
            if sum(nechet) > sum(chet):  # – сумма нечётных чисел меньше суммы чётных.
                count += 1
print(count)
'''
# Ответ: 241
# endregion: Задача 9 из пробника Статград 2023

# Вариант 2
# В базе данных хранится информация об объектах определённой структуры.
# Каждый объект описывается как последовательность из 310 простых
# элементов, при этом всего используется 980 различных простых элементов.
# Каждое описание объекта записывается как последовательность кодов
# простых элементов, при этом код каждого элемента содержит одинаковое для
# всех элементов минимально возможное число битов, а для описания в целом
# отводится минимально возможное целое число байтов.
# Сколько Кбайтов потребуется для хранения 16 384 описаний, построенных
# по такой схеме? В ответе запишите только число – количество Кбайтов.
'''
symbols = 310
alphabet = 980
# alphabet = 2 ** i
# alphabet = 2 ** 10
i = 10
bit = symbols * i
byte = int(bit / 8) + 1
print(byte)

print((16384 * byte) / (2 ** 10))
'''
# Ответ: 6208


# Вариант 1
# В базе данных хранится информация об объектах определённой структуры.
# Каждый объект описывается как последовательность из 290 простых
# элементов, при этом всего используется 1012 различных простых элементов.
# Каждое описание объекта записывается как последовательность кодов
# простых элементов, при этом код каждого элемента содержит одинаковое для
# всех элементов минимально возможное число битов, а для описания в целом
# отводится минимально возможное целое число байтов.
# Сколько Кбайтов потребуется для хранения 32 768 описаний, построенных
# по такой схеме? В ответе запишите только число – количество Кбайтов.
'''
symbols = 290
alphabet = 1012
# alphabet = 2 ** i
# alphabet = 2 ** 10
i = 10
bit = symbols * i
byte = int(bit / 8) + 1
print(byte)

print((32768 * byte) / (2 ** 10))
'''
# Ответ: 11616


# region: Задача 14 из пробника Статград 2023
'''
# В выражении 123x_37 + 4x59_37 x обозначает некоторую цифру из алфавита
# системы счисления с основанием 37. Определите наименьшее значение x,
# при котором значение данного выражения кратно 36.  Для найденного x
# вычислите частное от деления данного выражения на 36 и запишите его
# в ответе в десятичной системе счисления.


for x in range(0, 37):
    A = [int(i) for i in f'1 2 3 {x}'.split()]
    B = [int(i) for i in f'4 {x} 5 9'.split()]

    a = 0
    A.reverse()
    for i in range(0, len(A)):
        a += A[i] * 37 ** i

    b = 0
    B.reverse()
    for i in range(0, len(B)):
        b += B[i] * 37 ** i

    if (a + b) % 36 == 0:
        print((a + b) // 36)
'''
# Ответ: 7348
# endregion: Задача 14 из пробника Статград 2023


# region: Задача 15 из пробника Статград 2023
'''
# Вариант 1
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без
# остатка на натуральное число m».
# Укажите наименьшее целое значение A, для которого формула
# (ДЕЛ(144, x)→ ¬ДЕЛ(x, y)) ∨ (x + y > 100) ∨ (A – x > y)
# тождественно истинна при любых натуральных значениях переменных x и y.

def F(x, y):
    return ((144 % x == 0) <= (x % y != 0)) or (x + y > 100) or (A - x > y)


for A in range(0, 1000):
    if all(F(x, y) for x in range(1, 100) for y in range(1, 100)):
        print(A)
        break
'''
# Ответ: 97
# endregion: Задача 15 из пробника Статград 2023

# Вариант 1
'''
from functools import lru_cache

@lru_cache()
def F(n):
    if n == 0:
        return 0
    else:
        return F(n // 10) + (n % 10)

print(F(12345))

counter = 0
for n in range(237567892, 1134567009+1):
    if F(n) > F(n+1):
        counter += 1
print(counter)
'''

# Вариант 2
'''
counter = 0
for n in range(237567899, 1134567009+1, 10):
    counter += 1
print(counter)
'''

# Вариант 3
'''
print(113456700 - 23756789+1)
'''
# 89699912


# region: Задача 17 из пробника Статград 2023

# Вариант 1
'''
# Файл содержит последовательность целых чисел, по модулю не превышающих
# 10 000.  Назовём парой два идущих подряд элемента последовательности.
# Определите количество таких пар, в которых запись меньшего элемента
# заканчивается цифрой 5, а сумма квадратов элементов пары меньше, чем квадрат
# наименьшего из элементов последовательности, запись которых заканчивается
# цифрой 5. В ответе запишите два числа: сначала количество найденных пар,
# затем максимальную сумму квадратов элементов этих пар.

A = [int(i) for i in open("17.txt") if int(i) % 10 == 5]
mini = min(A)

M = [int(i) for i in open("17.txt")]

counter = 0
maxim = -1
for i in range(len(M) - 1):
    if min(M[i], M[i+1]) % 10 == 5:
        if M[i] ** 2 + M[i+1] ** 2 < mini ** 2:
            counter += 1
            maxim = max(maxim, M[i] ** 2 + M[i+1] ** 2)

print(counter, maxim)
'''
# Ответ: 403 99805561
# endregion: Задача 17 из пробника Статград 2023

for s in open('9.txt'):
    print(s)


# endregion Урок: ************************************************************


# todo: Василий = [2, 5, 6, 8, 12, 14+, 15, 17, 19, 20, 22, 24]
# на прошлом уроке: Проанализировали задачи с пробника и прорешать Статград ВАРИАНТ 1 - проблемные задачи.
# на следующем уроке: Обсуждаем вариант и вопросы.
