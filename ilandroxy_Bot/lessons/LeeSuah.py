# region Домашка: ************************************************************


# endregion Домашка: ************************************************************

# region Урок: ************************************************************

# Тип 9 №51978
# В каждой строке электронной таблицы записаны пять целых положительных чисел.
# Определите, сколько в таблице строк, для которых выполнены следующие условия:
# — все числа в строке различны;
# — нечётных чисел больше, чем чётных;
# — сумма нечётных чисел меньше суммы чётных.
# В ответе запишите число — количество строк, для которых выполнены эти условия.
'''
count = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    if len(M) == len(set(M)):  # — все числа в строке различны;
        chet = [x for x in M if x % 2 == 0]
        nechet = [x for x in M if x % 2 != 0]
        if len(nechet) > len(chet):
            if sum(nechet) < sum(chet):
                count += 1
print(count)
'''
# Ответ: 303


# Открытие файла 17 номера:
'''
M = [int(x) for x in open('17.txt')]


# Рассмотрим различные типы задач 17 номера:
M = [1, 2, 3, 4, 5]

# 1. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
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


# Тип 17 №55604
# Файл содержит последовательность целых чисел, модуль которых находится в интервале от 100 до 10000.
# Назовём парой два идущих подряд элемента последовательности.
#
# Определите количество пар, для которых выполняются следующие условия:
# — последняя цифра записи одного из элементов пары совпадает с предпоследней цифрой записи другого элемента;
# — ровно один элемент из пары делится без остатка на 7;
# — сумма квадратов элементов пары не превышает квадрат наименьшего из элементов последовательности,
# две последние цифры в записи которого одинаковы.
#
# В ответе запишите два числа: сначала количество найденных пар, затем максимальную величину
# суммы квадратов элементов этих пар.
'''
M = [int(x) for x in open('17.txt')]
A = min([x for x in M if str(x)[-1] == str(x)[-2]])
count = 0
maxi = 0
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    if str(x)[-1] == str(y)[-2] or str(y)[-1] == str(x)[-2]:
        if (x % 7 == 0) + (y % 7 == 0) == 1:
            if (x ** 2 + y ** 2) <= A ** 2:
                count += 1
                maxi = max(maxi, x**2 + y**2)
print(count, maxi)
'''
# Ответ: 205 99520570

# endregion Урок: ************************************************************


# Олеся = []
# КЕГЭ = []
# на следующем уроке:
