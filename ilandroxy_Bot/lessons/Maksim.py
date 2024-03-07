# region Домашка: ************************************************************


# КЕГЭ № 8481 (Уровень: Базовый) (В. Рыбальченко)
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
#
# — символ «?» означает ровно одну произвольную цифру;
# — символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
#
# Найдите все натуральные числа меньшие 108, которые кратны 237,
# соответствуют маске «81?2*80», но не соответствуют маске «*9*».
# В ответ в первом столбике перечислите все найденные числа в порядке
# возрастания, а во втором столбце – соответствующие им результаты деления этих чисел на 237.
'''
from fnmatch import *
for x in range(237, 10 ** 8, 237):
    if fnmatch(str(x), '81?2*80'):
        if (not fnmatch(str(x),'*9*')):
            print(x, x // 237)
'''


# КЕГЭ № 3691 (Уровень: Базовый) (Калинин А.)
# Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
# — символ «?» означает ровно одну произвольную цифру;
# — символ «*» означает любую последовательность цифр произвольной длины;
# в том числе «*» может задавать и пустую последовательность.
#
# Напишите программу, которая ищет среди целых чисел, превышающих 320400,
# первые пять чисел, которые делятся на все чётные числа, соответствующие маске 1?.
#
# В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
# а во втором столбце — соответствующие им частные от деления на максимальное из чётных чисел, соответствующие маске 1?.

''''
from fnmatch import *
k = 0
for x in range(320400+1, 800000):
    R = []
    for y in range(10, 18+1, 2):
        if fnmatch(str(y), '1?'):
            R.append(y)

    if all(x % y == 0 for y in R):
        print(x, x // 18)
        k += 1
        if k == 5:
            break
'''

'''
k = 0
for x in range(320400+1, 800000):
    if all(x % y == 0 for y in range(10, 18+1, 2)):
        print(x, x // 18)
        k += 1
        if k == 5:
            break
'''
'''
def prime(x):
    div = []
    for j in range(1, int(x ** 0.5) + 1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))

def divisors(x):
    div = []
    for j in range(1, int(x ** 0.5)+1):
        if x % j == 0:
            if len(prime(j)) == 2 and len(prime(x // j)) == 2:
                div += [j, x // j]
    return sorted(set(div))


for x in range(125697, 125721+1):
    d = divisors(x)
    if len(d) == 2:
        print(*d)
'''


# КЕГЭ № 5946 (Уровень: Средний)
#
# Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# – в строке все числа различны;
# – количество чётных чисел превышает количество нечётных чисел.
'''
cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    if len(M) == len(set(M)):
        C = [x for x in M if x % 2 == 0]
        N = [x for x in M if x % 2 != 0]
        if len(C) > len(N):
            cnt += 1
print(cnt)


cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    C, N = [], []
    if len(M) == len(set(M)):
        for y in M:
            if y % 2 == 0:
                C.append(y)
            else:
                N.append(y)
        if len(C) > len(N):
            cnt += 1

print(cnt)
'''

# КЕГЭ № 12918 PRO100 ЕГЭ 26.01.24 (Уровень: Средний)
# # Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# Определите сумму чисел в строке таблицы с наименьшим номером, для которой выполнены все условия:
#
# в строке есть два числа, которые повторяются дважды, остальные два числа различны;
# максимальное число строки не повторяется;
# произведение максимального и минимального чисел строки больше суммы оставшихся четырёх чисел.
# В ответе запишите только число.

'''
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if len([x for x in M if M.count(x) == 2]) == 4:
        if M.count(max(M)) == 1:
            if M[0] * M[-1] > sum(M[1:-1]):
                print(sum(M))
                break
'''
# endregion Домашка: *********************************************************

# region Урок: ************************************************************

# Как открывать текстовый файл для 17 номера
'''
M = [int(x) for x in open('17.txt')]
'''

# Типа номеров 17 номера:
'''
M = [1, 2, 3, 4, 5]

# 1. Назовём парой два идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    print(f'{x}{y}', end=' ')
print()

# 2. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
# 123 234 345
for i in range(len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    print(f'{x}{y}{z}', end=' ')
print()

# 3. В данной задаче под парой подразумевается два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        print(f'{x}{y}', end=' ')
    print()
'''

# Тип 17 №37356
# В файле содержится последовательность из 10000 целых положительных чисел.
# Каждое число не превышает 10 000. Определите и запишите в ответе сначала количество
# пар элементов последовательности, у которых сумма элементов кратна 9, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности.
'''
M = [int(x) for x in open('17.txt')]
R = []
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        if (x + y) % 9 == 0:
            R.append(x + y)
print(len(R), max(R))
'''
# Ответ: 5553635 19998


# Тип 17 №40733
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10000.
# Назовём парой два идущих подряд элемента последовательности.
# Определите количество пар, в которых хотя бы один из двух элементов делится на 3
# и хотя бы один из двух элементов меньше среднего арифметического всех чётных элементов последовательности.
# В ответе запишите два числа: сначала количество найденных пар, а затем — максимальную сумму элементов таких пар.
'''
M = [int(x) for x in open('17.txt')]
chet = [x for x in M if x % 2 == 0]
R = []
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if x % 3 == 0 or y % 3 == 0:
        avg = sum(chet) / len(chet)
        if x < avg or y < avg:
            R.append(x + y)
print(len(R), max(R))
'''
# Ответ: 2288 14875



# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Максим = [2.1, 6.1, 5.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 23.1, 25.1]
# КЕГЭ = []
# на следующем уроке:
