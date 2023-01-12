# region Домашка: ******************************************************************************



# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************

M = [1, 2, 3, 4, 5]
# 1. Назовём парой два идущих подряд элемента последовательности.
# 12 23 34 45
for i in range(0, len(M)-1):
    print(f'{M[i]}{M[i+1]}', end=' ')
print('\n')

# 2. Назовём тройкой три идущих подряд элемента последовательности.
# 123 234 345
for i in range(0, len(M)-2):
    print(f'{M[i]}{M[i+1]}{M[i+2]}', end=' ')
print('\n')

# 3. В данной задаче под парой подразумевается два различных элемента последовательности
# 12 13 14 15
# 23 24 25
# 34 35
# 45
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        print(f'{M[i]}{M[j]}', end=' ')
    print()


# Метод по простому
f = open('17.txt')
M = [int(i) for i in f]
f.close()

# Работа с файлами на чистоту кода
with open('17.txt', 'r') as f:
    M = [int(i) for i in f]

# Методы который мы используем
M = [int(i) for i in open('17.txt')]



# Тип 17 № 39246
'''
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000.
# Назовём парой два идущих подряд элемента последовательности.
# Определите количество пар, в которых хотя бы один из двух элементов делится на 5, а их сумма делится на 7.
# В ответе запишите два числа: сначала количество найденных пар, а затем — максимальную сумму элементов таких пар.

M = [int(i) for i in open('17.txt')]

count = 0
maxi = 0
for i in range(0, len(M)-1):
    if M[i] % 5 == 0 or M[i+1] % 5 == 0:  # в которых хотя бы один из двух элементов делится на 5
        if (M[i] + M[i+1]) % 7 == 0:  # а их сумма делится на 7
            count += 1
            maxi = max(maxi, M[i] + M[i+1])
            # if maxi < M[i] + M[i+1]:
            #     maxi = M[i] + M[i+1]
print(count, maxi)
'''
# Ответ: 308 18893



# Тип 17 № 39763
'''
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000.
# Назовём тройкой три идущих подряд элемента последовательности.
# Определите количество троек чисел таких, которые могут являться сторонами остроугольного треугольника.
# В ответе запишите два числа: сначала количество найденных троек, а затем — максимальную сумму элементов таких троек.
# Если таких троек не найдётся — следует вывести 00.

M = [int(i) for i in open('17.txt')]

count = 0
maxi = 0
for i in range(0, len(M)-2):
    A = sorted([M[i], M[i+1], M[i+2]])
    if A[2] ** 2 < A[0] ** 2 + A[1] ** 2:
        count += 1
        maxi = max(maxi, M[i] + M[i+1] + M[i+2])
print(count, maxi)
'''
# Ответ: 1175 29451




# Тип 17 № 47014

# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10000.
# Назовём парой два идущих подряд элемента последовательности.
# Определите количество пар, в которых один из двух элементов делится на 5,
# а другой меньше среднего арифметического всех нечётных элементов последовательности.
# В ответе запишите два числа: сначала количество найденных пар, а затем — максимальную сумму элементов таких пар.

# Вариант 1
'''
M = [int(i) for i in open('17.txt')]

summ = 0
kol = 0
for i in range(0, len(M)):
    if M[i] % 2 != 0:
        summ += M[i]
        kol += 1
sred = summ / kol

count = 0
maxi = 0
for i in range(0, len(M)-1):
    if (M[i] % 5 == 0 and M[i+1] < sred) or (M[i+1] % 5 == 0 and M[i] < sred):
        count += 1
        maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)
'''

# Вариант 2
'''
A = [int(i) for i in open('17.txt') if int(i) % 2 != 0]
sred = sum(A) / len(A)

M = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
for i in range(0, len(M)-1):
    if (M[i] % 5 == 0 and M[i+1] < sred) or (M[i+1] % 5 == 0 and M[i] < sred):
        count += 1
        maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)
'''
# 1061 14847


# Тип 17 № 37362
'''
# В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых сумма элементов кратна 80 и хотя бы один элемент из пары делится на 50, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности.
# Порядок элементов в паре не важен.

M = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        if (M[i] + M[j]) % 80 == 0:  # у которых сумма элементов кратна 80
            if M[i] % 50 == 0 or M[j] % 50 == 0:  # и хотя бы один элемент из пары делится на 50
                count += 1
                maxi = max(maxi, M[i] + M[j])
print(count, maxi)
'''
# Ответ: 21648 19760




# Тип 17 № 45251
'''
# В файле содержится последовательность натуральных чисел.
# Элементы последовательности могут принимать целые значения от 1 до 100 000 включительно.
# Определите количество пар последовательности, в которых хотя бы одно число делится на минимальный элемент последовательности, кратный 21.
# Гарантируется, что такой элемент в последовательности есть.
# В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.

A = [int(i) for i in open('17.txt') if int(i) % 21 == 0]

M = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
for i in range(0, len(M)-1):
    if M[i] % min(A) == 0 or M[i+1] % min(A) == 0:
        count += 1
        maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)
'''
# Ответ: 126 171120

print(range.__doc__)

M = []
print(M.append.__doc__)



# endregion Урок: ******************************************************************************


# todo: Александр_2 = [2, 5, 6, 8, 12, 14+, 15+, 16, 17, 23, 25.2]
# на прошлом уроке: Разобрали 17 номер все типы задач.
# на следующем уроке: Разбираем 24 номер







