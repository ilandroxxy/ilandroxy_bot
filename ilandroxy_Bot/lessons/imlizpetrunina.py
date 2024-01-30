# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# Тип 9 №27521
'''
# Откройте файл электронной таблицы, содержащей вещественные числа — результаты ежечасного измерения температуры воздуха на протяжении трёх месяцев.
#
# Сколько раз встречалась температура, которая равна минимальному значению?
A = []
for s in open('9.txt'):
    A += [float(x) for x in s.replace(',', '.').split()]

print(A.count(min(A)))
'''
# Ответ: 1


# Тип 9 №35983
# Электронная таблица содержит результаты ежечасного измерения температуры воздуха
# на протяжении трёх месяцев. Определите, сколько раз за время измерений максимальная
# суточная температура оказывалась выше среднесуточной на 7 и более градусов.
'''
count = 0
for s in open('9.txt'):
    M = [float(x) for x in s.replace(',', '.').split()]
    if max(M) - (sum(M) / len(M)) >= 7:
        count += 1
print(count)
'''
# Ответ: 66



# Тип 9 №52180
# В каждой строке электронной таблицы записаны пять натуральных чисел.
#
# Определите, сколько в таблице строк, для которых выполнены следующие условия:
# — все числа в строке различны;
# — чётных чисел больше, чем нечётных;
# — сумма чётных чисел меньше суммы нечётных.
#
# В ответе запишите число — количество строк, для которых выполнены эти условия.
'''
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
'''
# Ответ: 241


# Тип 9 №58321
# Откройте файл электронной таблицы, содержащей в каждой строке четыре натуральных числа.
#
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# — наименьшее из четырёх чисел более чем в шесть раз меньше суммы трёх других;
# — произведение наибольшего и наименьшего числа больше произведения оставшихся чисел.
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if M[0] * 6 < (M[1] + M[2] + M[3]):
        if M[0] * M[3] > M[1] * M[2]:
            count += 1
print(count)
'''
# Ответ: 118


# Тип 9 №56537
# В каждой строке электронной таблицы записаны шесть натуральных чисел.
#
# Определите, сколько в таблице строк, для которых выполнены следующие условия:
# — в строке есть как повторяющиеся, так и неповторяющиеся числа;
# — среднее арифметическое всех неповторяющихся чисел строки меньше,
# чем среднее арифметическое всех повторяющихся чисел этой строки.
#
# При вычислении средних значений каждое число учитывается столько раз,
# сколько оно встречается в строке.
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if len(M) != len(set(M)):
        copied = [x for x in M if M.count(x) > 1]
        necopied = [x for x in M if M.count(x) == 1]
        try:
            if (sum(necopied) / len(necopied)) < (sum(copied) / len(copied)):
                count += 1
        except ZeroDivisionError:
            continue
print(count)


count = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if len(M) != len(set(M)):
        copied = [x for x in M if M.count(x) > 1]
        necopied = [x for x in M if M.count(x) == 1]
        if len(copied) > 0 and len(necopied) > 0:
            if (sum(necopied) / len(necopied)) < (sum(copied) / len(copied)):
                count += 1
print(count)
'''
# Ответ: 1770


# Тип 9 №58517
# В каждой строке электронной таблицы записаны шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых одновременно выполнены все следующие условия:
#
# — минимальное число встречается в строке ровно один раз;
# — хотя бы одно число в строке повторяется более одного раза;
# — максимальное число в строке превышает среднее арифметическое
# остальных пяти чисел этой строки более чем в три раза.
#
# В ответе запишите число — количество строк, для которых выполнены эти условия.
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if M.count(M[0]) == 1:  # — минимальное число встречается в строке ровно один раз;
        if len(M) != len(set(M)):  # — хотя бы одно число в строке повторяется более одного раза;
            if M[-1] > (sum(M[:5]) / 5) * 3:
                count += 1
print(count)
'''
# Ответ: 49


# endregion Урок: ******************************************************************


# Лиза = [2.1, 6.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 23.1]
# КЕГЭ  = []
# на следующем уроке:
