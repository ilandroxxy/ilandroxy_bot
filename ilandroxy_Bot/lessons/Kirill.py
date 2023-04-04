# region Домашка:  **************************************************


# endregion Домашка: **************************************************


# region Урок:  **************************************************


# 2. Тип 17 № 47221
# В файле содержится последовательность целых чисел. Элементы последовательности могут принимать
# целые значения от −10000 до 10000 включительно. Определите количество пар последовательности, в которых только
# одно число оканчивается на 3, а сумма квадратов элементов пары не меньше квадрата максимального элемента
# последовательности, оканчивающегося на 3. В ответе запишите два числа: сначала количество найденных пар,
# затем максимальную из сумм квадратов элементов таких пар. В данной задаче под парой подразумевается два идущих
# подряд элемента последовательности.
'''
M = [int(i) for i in open('17.txt')]
MAXI = max([i for i in M if abs(i) % 10 == 3])
count = 0
maxi = -999999
for i in range(0, len(M)-1):
    if (str(M[i])[-1] == '3' and str(M[i+1])[-1] != '3') or (abs(M[i]) % 10 != 3 and abs(M[i+1]) % 10 == 3):
        if M[i] ** 2 + M[i+1] ** 2 >= MAXI ** 2:
            count += 1
            maxi = max(maxi, M[i] ** 2 + M[i+1] ** 2)
print(count, maxi)
'''
# Ответ: 180 190360573

'''
id = '123.32.54.233'
A = id.split('.')
M = [int(i) for i in id.split('.')]
print(M)

s = '*'.join(A)
print(s)
'''

# Тип 9 № 38588
# Откройте файл электронной таблицы, содержащей в каждой строке три натуральных числа.
#
# Выясните, какое количество троек чисел может являться сторонами треугольника,
# то есть удовлетворяет неравенству треугольника. В ответе запишите только число.
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(i) for i in s.split()])
    if M[2] < M[0] + M[1]:
        count += 1
print(count)
'''
# Ответ: 2453


# Тип 9 № 47006 В каждой строке электронной таблицы записаны четыре натуральных числа. Определите, сколько в таблице
# таких четвёрок, в которых любые три числа могут быть сторонами невырожденного треугольника (вырожденным называется
# треугольник, у которого сумма длин двух сторон равна длине третьей стороны).
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(i) for i in s.split()])
    if M[0] + M[1] > M[3]:
        count += 1
print(count)
'''
# Ответ: 1842


# Тип 9 № 47213 i
# Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
#
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
#
# — в строке только одно число повторяется ровно два раза, остальные числа различны;
#
# — среднее арифметическое неповторяющихся чисел строки не больше суммы повторяющихся чисел.
# list([1 2 3 4 5 5])  ->  set({1 2 3 4 5})
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(i) for i in s.split()])
    if len(set(M)) == len(M) - 1:
        copied = sum(M) - sum(set(M))
        if (sum(set(M)) - copied) / 4 <= copied * 2:
            count += 1
print(count)
'''
# Ответ: 2241


# Тип 9 № 36864 Электронная таблица содержит результаты ежечасного измерения температуры воздуха на протяжении трёх
# месяцев. Определите, сколько раз за время измерений минимальная суточная температура оказывалась ниже
# среднесуточной на 8 и более градусов.
'''
count = 0
for s in open('9.txt'):
    M = [float(i) for i in s.replace(',', '.').split()]
    mini = min(M)
    sred = sum(M) / len(M)
    if sred - mini >= 8:
        count += 1
print(count)
'''
# Ответ: 51


A = [1, 2, 3]
B = [4, 5]
C = A + B
print(C)



# Тип 9 № 27528 i
# Откройте файл электронной таблицы, содержащей вещественные числа —
# результаты ежечасного измерения температуры воздуха на протяжении трёх месяцев.
#
# Найдите разность между максимальным значением температуры за три месяца и её средним арифметическим значением.
# В ответе запишите только целую часть получившегося числа.

# Вариант 1
'''
M = []
for s in open('9.txt'):
    M += [float(i) for i in s.replace(',', '.').split()]

print(max(M) - (sum(M) / len(M)))
'''

# Вариант 2
'''
M = [float(i) for i in open('9.txt').read().replace(',', '.').split()]

print(max(M) - (sum(M) / len(M)))
'''
# Ответ: 14

# endregion Урок:  **************************************************

import useful
print(useful.who_is_name())

# todo: Кирилл = [1, 2, 3, 4, 5, 8, 9, 12, 13, 14+, 15, 16, 17, 19-21, 22, 23, 25.1], на следующем уроке:
# на прошлом уроке: Прорешивали 9 номера всех типов через Python
# на следующем уроке:
