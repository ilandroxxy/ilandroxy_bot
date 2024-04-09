# region Домашка: ******************************************************************


# endregion Домашка: *****************************************************************


# region Урок: ******************************************************************

'''
file = open('9.txt')
for s in file:
    print(s)
file.close()  # закрытие файла - это правило хорошего тона

with open('9.txt') as file:
    for s in file:
        print(s)
'''


# Тип 9 №45243
# Определите количество строк таблицы, в которых квадрат
# суммы максимального и минимального чисел в строке больше суммы квадратов трёх оставшихся.
'''
cnt = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if ((M[0] + M[-1]) ** 2) > (M[1] ** 2 + M[2] ** 2 + M[3] ** 2):
        cnt += 1
print(cnt)
'''
# Ответ: 2640


# Тип 9 №58476
# В каждой строке электронной таблицы записаны шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых одновременно выполнены все следующие условия:
#
# — максимальное число встречается в строке ровно один раз;
# — хотя бы одно число в строке повторяется более одного раза;
# — максимальное число в строке превышает среднее арифметическое всех остальных чисел этой строки более чем в три раза.
#
# В ответе запишите число — количество строк, для которых выполнены эти условия.
'''
cnt = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if M.count(max(M)) == 1:
        if len(M) != len(set(M)):
            if max(M) > (sum(M[:-1]) / 5) * 3:
                cnt += 1
print(cnt)
'''
# Ответ: 95


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
cnt = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if len(M) == len(set(M)):
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if len(chet) > len(nechet):
            if sum(chet) < sum(nechet):
                cnt += 1
print(cnt)
'''
# Ответ: 241


# Тип 9 №59714
# В файле находится таблица, которая содержит в каждой из строк по 7 натуральных чисел.
# Ваша задача состоит в том, чтобы посчитать количество таких строк, в
# которых два числа повторяются по 2 раза, а три других различны,
# и среднее арифметическое неповторяющихся чисел больше среднего арифметического повторяющихся.
'''
cnt = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    copied = [x for x in M if M.count(x) == 2]
    not_copied = [x for x in M if M.count(x) == 1]
    if len(copied) == 4 and len(not_copied) == 3:
        if sum(not_copied) / 3 > sum(copied) / 4:
            cnt += 1
print(cnt)
'''
# Ответ: 96


'''
# Пары подряд идущих элементов:
M = [1, 2, 3, 4, 5]
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    print(f'{x}{y}', end=' ')  # 12 23 34 45 
'''


# Тип 9 №58322
# Откройте файл электронной таблицы, содержащей в каждой строке четыре натуральных числа.
#
# Определите количество строк таблицы, содержащих числа, для которых выполнено хотя бы одно из условий:
# — квадрат наибольшего из четырёх чисел больше произведения трёх других;
# — будучи упорядоченными, четыре числа образуют арифметическую прогрессию.
#
# В ответе запишите только число.
'''
cnt = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if M[3] ** 2 > (M[0] * M[1] * M[2]) or all(M[1] - M[0] == M[i+1] - M[i] for i in range(len(M)-1)):
        cnt += 1
print(cnt)
'''
# Ответ: 61



# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Дмитрий = [2, 5, 8, 12, 14, 15, 16, 23]
# КЕГЭ  = []
# на следующем уроке:
