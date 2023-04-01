
# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************



# region Урок: ******************************************************************

# Тип 9 № 39238
# Откройте файл электронной таблицы, содержащей в каждой строке три натуральных числа.
# Определите, сколько среди заданных троек чисел таких, которые могут быть сторонами прямоугольного треугольника.
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(i) for i in s.split()])
    if M[2] ** 2 == M[0] ** 2 + M[1] ** 2:
        count += 1
print(count)
'''
# Ответ: 2



# Тип 9 № 29657
# Электронная таблица содержит результаты ежечасного измерения температуры воздуха на протяжении трёх
# месяцев. Определите, сколько раз за время наблюдений суточные колебания температуры (разность между максимальной и
# минимальной температурой в течение суток) превышали 17 градусов.
'''
count = 0
for s in open('9.txt'):
    M = [float(i) for i in s.replace(',', '.').split()]
    if max(M) - min(M) > 17:
        count += 1
print(count)
'''
# Ответ: 12



# Тип 9 № 27521
# Откройте файл электронной таблицы, содержащей вещественные числа — результаты
# ежечасного измерения температуры воздуха на протяжении трёх месяцев.

# Сколько раз встречалась температура, которая равна минимальному значению?
'''
# Вариант 1
M = []
for s in open('9.txt'):
    M += [float(i) for i in s.replace(',', '.').split()]

count = 0
for x in M:
    if x == min(M):
        count += 1
print(count)

# Вариант 2
A = [float(i) for i in open('9.txt').read().replace(',', '.').split()]
print(len([x for x in A if x == min(A)]))
'''
# Ответ: 1


# Тип 9 № 47213
# Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# — в строке только одно число повторяется ровно два раза, остальные числа различны;
# — среднее арифметическое неповторяющихся чисел строки не больше суммы повторяющихся чисел.
# В ответе запишите только число.
'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    if len(set(M)) == len(M) - 1:  # — в строке только одно число повторяется ровно два раза, остальные числа различны;
        copied = sum(M) - sum(set(M))  # list[43, 28, 36, 31, 129, 28] - set[43, 28, 36, 31, 129] = 28
        if ((sum(M) - copied * 2) / 4 ) <= copied*2:
            count += 1
print(count)
'''
# Ответ: 2241


# Тип 24 № 27687
# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z.
# Определите длину самой длинной последовательности, состоящей из символов Y.
# Хотя бы один символ Y находится в последовательности.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
# Вариант 1
s = open('24.txt').readline()
count = 1
Max_count = 0
for i in range(0, len(s)-1):
    if s[i] == 'Y' and s[i+1] == 'Y':
        count += 1
        Max_count = max(Max_count, count)
    else:
        count = 1
print(Max_count)

# Вариант 2
s = open('24.txt').readline()
s = s.replace('X', ' ').replace('Z', ' ')
M = [len(i) for i in s.split()]
print(max(M))

# Вариант 3
print(max([len(i) for i in open('24.txt').readline().replace('X', ' ').replace('Z', ' ').split()]))

# Вариант 4
s = open('24.txt').readline()
print(s)
print(len('YYYYYYYYYY'))
'''
# Ответ: 10


# Тип 24 № 27690
# Текстовый файл состоит не более чем из 10**6 символов A, B и C.
# Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
s = open('24.txt').readline()
count = 1
Max_count = 0
for i in range(0, len(s)-1):
    if s[i] != s[i+1]:
        count += 1
        Max_count = max(Max_count, count)
    else:
        count = 1
print(Max_count)
'''
# Ответ: 42

# Тип 24 № 38602 i
# Текстовый файл состоит из символов P, Q, R и S.
# Определите максимальное количество идущих подряд символов в прилагаемом файле,
# среди которых нет идущих подряд символов P. Для выполнения этого задания следует написать программу.

# OOOOOPPOOOOPP
'''
s = open('24.txt').readline()
s = s.replace('PP', ' ')
M = [len(i) for i in s.split()]
print(1 + max(M) + 1)
'''
# Ответ: 188


# Тип 24 № 36037
# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z. Определите максимальное
# количество идущих подряд символов, среди которых нет подстроки XZZY. Для выполнения этого задания следует написать
# программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
# XZZYOOOOXZZY
'''
s = open('24.txt').readline()
s = s.replace('XZZY', ' ')
M = [len(i) for i in s.split()]
print(3 + max(M) + 3)
'''
# Ответ: 1713


# Тип 24 № 45258
# Текстовый файл состоит из символов A, B и C.
#
# Определите максимальное количество идущих подряд пар символов AB или CB в прилагаемом файле.
#
# Искомая подпоследовательность должна состоять только из пар AB,
# или только из пар CB, или только из пар AB и CB в произвольном порядке следования этих пар.
#
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline()
s = s.replace('AB', '*').replace('CB', '*')
s = s.replace('A', ' ').replace('B', ' ').replace('C', ' ')
M = [len(i) for i in s.split()]
print(max(M))
'''
# Ответ: 65
# endregion Урок: ******************************************************************


# todo: Никита2 = [5, 3, 9, 17, 19-21, 22, 24.1]
# на прошлом уроке: Разобрали 9 номера и первую часть 24 номеров с строками
# на следующем уроке: