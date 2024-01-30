
# region Домашка: ******************************************************************

# КЕГЭ № 8946 Джобс 02.06.2023 (Уровень: Базовый) (Е. Джобс)
#
# Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# – квадрат наибольшего значения больше произведения остальных чисел;
# – сумма двух наибольших значений как минимум вдвое больше суммы остальных значений в строке..
'''
count = 0
for s in open('9.txt'):
  M = sorted([int(i) for i in s.split()])
  if M[-1] ** 2 > M[0] * M[1] * M[2] * M[3]:
    if 2 * (M[-1] + M[-2]) > M[0] + M[1] + M[2]:
      count += 1
print(count)
'''
# endregion Домашка: ******************************************************************


# region Урок: ********************************************************************

# Тип 24 №27697
# Текстовый файл состоит не более чем из 10**6 символов L, D и R.
# Определите длину самой длинной последовательности, состоящей из символов D.
# Хотя бы один символ D находится в последовательности.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
# Вариант 1
s = open('24.txt').readline()  # DDDDDD
count = 1
count_max = 0
for i in range(len(s)-1):
    if s[i] == 'D' and s[i+1] == 'D':
        count += 1
        count_max = max(count, count_max)
    else:
        count = 1
print(count_max)


# Вариант 2
s = open('24.txt').readline()
s = s.replace('L', ' ').replace('R', ' ')
print(max([len(x) for x in s.split()]))

# Вариант 2.1
print(max([len(x) for x in open('24.txt').readline().replace('L', ' ').replace('R', ' ').split()]))


# Вариант 3 - Решение через ctrl + F
s = open('24.txt').readline()
print(s)
print(len('DDDDDDDDDDD'))
'''
# Ответ: 11


# Тип 24 №36037
# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов,
# среди которых нет подстроки XZZY.
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
s = open('24.txt').readline()
s = s.replace('XZZY', '*** ***')
print(max([len(x) for x in s.split()]))
'''
# Ответ: 1713


# Тип 24 №27421
# Текстовый файл состоит не более чем из 106 символов X, Y и Z.
# Определите максимальное количество идущих подряд символов,
# среди которых каждые два соседних различны.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
s = open('24.txt').readline()
count = 1
count_max = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        count += 1
        count_max = max(count, count_max)
    else:
        count = 1
print(count_max)
'''
# Ответ: 35

# endregion Урок: ******************************************************************

# Варя = [2.1, 5.1, 6.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 17.1, 23.1, 25.1]
# КЕГЭ  = []
# на следующем уроке:
