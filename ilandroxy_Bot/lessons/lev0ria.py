# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Как открыть .txt файлик
'''
for s in open('17.txt'):
    print(s)


M = [int(x) for x in open('17.txt')]
print(M)
'''


# Разберем три основных типа задач на примере.
# Представим, что наш файл содержал такие значения:
'''
# i  0  1  2  3  4
M = [1, 2, 3, 4, 5]

# 1. В данной задаче под парой подразумевается
# два идущих подряд элемента последовательности:
# 12 23 34 45

for i in range(0, len(M)-1):
    x, y = M[i], M[i + 1]
    print(f"{x}{y}", end=' ')
print()

"""
Если написать: for i in range(0, len(M)):
То получим ошибку: IndexError: list index out of range
"""

# 2. В данной задаче под тройкой подразумевается
# три идущих подряд элемента последовательности:
# 123 234 345

for i in range(0, len(M) - 2):
    x, y, z = M[i], M[i + 1], M[i + 2] 
    print(f"{x}{y}{z}", end=' ')
print()

M = [1, 2, 3, 4, 5]
# 3. В данной задаче под парой подразумевается
#   два различных элемента последовательности:
# 12 13 14 15
# 23 24 25
# 34 35
# 45

for i in range(0, len(M)):
    for j in range(i + 1, len(M)):
        x, y = M[i], M[j]
        print(f"{x}{y}", end=' ')
    print()
'''


# № 2400 (Уровень: Базовый)
# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от -10000 до 10000 включительно.
# Определите и запишите в ответе сначала количество пар элементов последовательности,
# в которых сумма элементов не менее 100 и хотя бы одно число в паре отрицательное,
# затем максимальное из произведений элементов таких пар.
#
# В данной задаче под парой подразумевается два подряд идущих элемента последовательности.
'''
M = [int(x) for x in open('17.txt')]
cnt = 0  # количество пар элементов последовательности
maxi = -999999999  # максимальное из произведений элементов таких пар
for i in range(0, len(M)-1):
    x, y = M[i], M[i + 1]
    if (x + y) >= 100 and (x < 0 or y < 0):
        cnt += 1
        maxi = max(maxi, x * y)
print(cnt, maxi)
'''
# 1137 -2655


# № 2993 (Уровень: Базовый)
# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от 0 до 10 000 включительно.
# Определите количество пар чисел, в котоин из двух элементов больше,
# чем наибольшее из всех чисел в файле, делящихся на 111, и хотя бы один элемент из
# двух оканчивается на 7. В ответе запишите два числа: сначала количество найденных пар,
# а затем – минимальную сумму элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.

# print(123 % 10)
# print(-123 % 10)
'''
M = [int(x) for x in open('17.txt')]
A = max([x for x in M if x % 111 == 0])

cnt = 0
mini = 999999999
for i in range(0, len(M)-1):
    x, y = M[i], M[i + 1]
    if x > A or y > A:
        if abs(x) % 10 == 7 or abs(y) % 10 == 7:
            cnt += 1
            mini = min(mini, x + y)
print(cnt, mini)
'''
# Ответ: 147 10849

# endregion Урок: ******************************************************************

# Лев = []
# КЕГЭ  = []
# на следующем уроке: