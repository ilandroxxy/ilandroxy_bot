# region Домашка:  ******************************************************************************


# endregion Домашка: ******************************************************************************


# region Урок:  ******************************************************************************


# Тип 9 № 47006
# В каждой строке электронной таблицы записаны четыре натуральных числа. Определите, сколько в таблице
# таких четвёрок, в которых любые три числа могут быть сторонами невырожденного треугольника (вырожденным называется
# треугольник, у которого сумма длин двух сторон равна длине третьей стороны).
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(i) for i in s.split()])
    if M[3] < M[0] + M[1]:
        count += 1
print(count)
'''
# Ответ: 1842


# Тип 9 № 35983
# Электронная таблица содержит результаты ежечасного измерения температуры воздуха на протяжении трёх
# месяцев. Определите, сколько раз за время измерений максимальная суточная температура оказывалась выше
# среднесуточной на 7 и более градусов.
'''
count = 0
for s in open('9.txt'):
    M = [float(i) for i in s.replace(',', '.').split()]  # ValueError: could not convert string to float: '13,7'
    if max(M) - (sum(M) / len(M)) >= 7:
        count += 1
print(count)
'''
# Ответ: 66


# Тип 9 № 48457
# В каждой строке электронной таблицы записаны шесть натуральных чисел.
#
# Определите, сколько в таблице строк, для которых выполнены следующие условия:
#
# — в строке встречается ровно четыре различных числа; два из них по два раза, два — по одному;
# — сумма повторяющихся чисел (без учёта повторений,
# то есть каждое число входит в сумму один раз) больше суммы неповторяющихся.
#
# В ответе запишите число — количество строк, для которых выполнены эти условия.
'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    if len(set(M)) == 4 and all(M.count(i) <= 2 for i in M):
        sum_copied = sum(M) - sum(set(M))
        if sum_copied > sum(set(M)) - sum_copied:
            count += 1
print(count)
'''
# Ответ: 456


# Тип 9 № 27526 i
# Откройте файл электронной таблицы, содержащей вещественные числа — результаты ежечасного измерения
# температуры воздуха на протяжении трёх месяцев.
#
# Сколько раз встречалась температура, которая была выше половины среднего арифметического значения, округленного до
# десятых, но ниже половины от максимального значения?
'''
M = [float(i) for i in open('9.txt').read().replace(',', '.').split()]
sred = round((sum(M) / len(M)) / 2, 1)
count = 0
for x in M:
    if sred < x < (max(M) / 2):
        count += 1
print(count)
'''
# Ответ: 526


# endregion Урок:  *************************************************************************

import useful
print(useful.who_is_name())

# todo: Ислам = [2, 3, 5, 6, 8, 9, 12, 14+, 15, 16, 17, 19-21, 22, 23, 25]
# на прошлом уроке: Прорешивали 9 номера всех типов через Python
# на следующем уроке:
