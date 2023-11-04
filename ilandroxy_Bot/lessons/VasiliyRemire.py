
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# Тип 9 №59780
# Откройте файл электронной таблицы, содержащей в каждой строке семь натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# — среди семи чисел совпадают ровно четыре числа;
# — среднее значение повторяющихся чисел строго меньше чем среднее арифметическое ВСЕХ чисел строки.
#
# В ответе запишите только число

# todo добавить разбор
'''
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    if len(set(M)) == 4 and any(M.count(x) == 4 for x in M):  # — среди семи чисел совпадают ровно четыре числа;
        sred = sum(M) / len(M)  # среднее арифметическое ВСЕХ чисел строки
        copied = (sum(M) - sum(set(M))) / 3
        if copied < sred:
            count += 1
print(count)
'''
# Ответ: 10


# Тип 9 №51978
# В каждой строке электронной таблицы записаны пять натуральных чисел.
# Определите, сколько в таблице строк, для которых выполнены следующие условия:
# — все числа в строке различны;
# — нечётных чисел больше, чем чётных;
# — сумма нечётных чисел меньше суммы чётных.
# В ответе запишите число — количество строк, для которых выполнены эти условия.
'''
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    if len(set(M)) == len(M):  # # — все числа в строке различны;
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if len(nechet) > len(chet):
            if sum(nechet) < sum(chet):
                count += 1
print(count)
'''
# Ответ: 303


# Тип 9 №55805
# Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел.
#
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# — каждое число в строке встречается по одному разу,
# — утроенная сумма максимального и минимального значений не превышает удвоенной суммы оставшихся чисел.
#
# В ответе запишите только число.
# todo добавить разбор
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if len(set(M)) == len(M):
        if (M[0] + M[-1]) * 3 <= (sum(M[1:-1])) * 2:
            count += 1
print(count)
'''
# Ответ: 853


# Тип 9 №55626
# В каждой строке электронной таблицы записаны шесть натуральных чисел.
#
# Назовём ячейку таблицы хорошей, если для неё выполняются следующие условия:
# — число в данной ячейке не встречается в других ячейках этой же строки;
# — число в данной ячейке ровно 50 раз встречается в других строках таблицы.
#
# Определите количество строк таблицы, содержащих хотя бы одну хорошую ячейку.
'''
count = 0
A = []
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    A += M

for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    for x in M:
        if M.count(x) == 1:
            if A.count(x) == 50:
                count += 1
print(count)
'''

# Ответ: 250


# № 9156 Джобс 06.06.2023 (Уровень: Базовый)
# Откройте файл электронной таблицы, содержащей в каждой строке четыре натуральных числа.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# – сумма максимального и минимального значений кратна 3;
# – четыре числа можно разбить на две пары так, чтобы разность значений в парах была одинаковой.
# В ответе запишите только число.
# todo Добавить разбор
'''
count = 0
from itertools import permutations
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    if (max(M) + min(M)) % 3 == 0:
        if any((s[0] - s[1]) == (s[2] - s[3]) for s in permutations(M, 4)):
            count += 1
print(count)
'''



# endregion Урок: ******************************************************************


# todo: Василий = [2.1, 5.1, 6.1, 8.1, 12.1, 14.1, 15.1, 16.1, 17.1, 23.1]
# todo:   КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:
