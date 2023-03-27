
# region Домашка: ******************************************************************

# Тип 25 № 33770
'''
def f(n):
    sps = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                sps.add(i)
            if (n // i) % 2 == 0:
                sps.add(n // i)
            if len(sps) > 3:
                return sps
    return sps

for j in range(106_000_000, 107_000_001):
    d = f(j)
    if len(d) == 3:
        print(j)
'''
# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Типы задач 17 номера:

M = [1, 2, 3, 4, 5]
# 1. Назовём парой два идущих подряд элемента последовательности.
# 12 23 34 45
'''
for i in range(0, len(M)-1):
    print(f'{M[i]}{M[i+1]}', end=' ')
print('\n')
'''
# 2. Назовём тройкой три идущих подряд элемента последовательности.
# 123 234 345
'''
for i in range(0, len(M)-2):
    print(f'{M[i]}{M[i+1]}{M[i+2]}', end=' ')
print('\n')
'''
# 3. В данной задаче под парой подразумевается два различных элемента последовательности.
# 12 13 14 15
# 23 24 25
# 34 35
# 45
'''   
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        print(f'{M[i]}{M[j]}', end=' ')
    print()
 
for i in range(0, len(M)):
    for j in range(0, len(M)):
        if i < j:
            print(f'{M[i]}{M[j]}', end=' ')
    print()
'''


# Теория для работы с txt файлами
'''
print(open('17.txt', 'r').read())

print(open('17.txt').readline())

print(open('17.txt').readlines())
'''

# with open('17.txt', 'r') as f:
#     M = [int(i) for i in f]


# Тип 17 № 38951
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000. Назовём парой
# два идущих подряд элемента последовательности. Определите количество пар, в которых хотя бы один из двух элементов
# делится на 3, а их сумма делится на 5. В ответе запишите два числа: сначала количество найденных пар,
# а затем – максимальную сумму элементов таких пар.
'''
M = [int(i) for i in open('17.txt')]
count = 0
maxi = -9999
for i in range(0, len(M)-1):
    if M[i] % 3 == 0 or M[i+1] % 3 == 0:
        if (M[i] + M[i+1]) % 5 == 0:
            count += 1
            maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)
'''
# Ответ: 635 19730


# Тип 17 № 40992
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000. Назовём парой
# два идущих подряд элемента последовательности. Определите количество пар, в которых хотя бы один из двух элементов
# делится на 5 и хотя бы один из двух элементов меньше среднего арифметического всех элементов последовательности,
# значение которых нечетно. В ответе запишите два числа: сначала количество найденных пар, а затем — максимальную
# сумму элементов таких пар.

# A = [int(i) for i in open('17.txt') if int(i) % 2 != 0]
# sred = sum(A) / len(A)
'''
M = [int(i) for i in open('17.txt')]
A = [i for i in M if i % 2 != 0]
sred = sum(A) / len(A)

# summ = 0
# kol = 0
# for x in M:
#     if x % 2 != 0:
#         summ += x
#         kol += 1
# sred = summ / kol

count = 0
maxi = -9999
for i in range(0, len(M)-1):
    if M[i] % 5 == 0 or M[i+1] % 5 == 0:
        if M[i] < sred or M[i+1] < sred:
            count += 1
            maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)
'''
# Ответ: 1531 14932



# Тип 17 № 37347
# В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не
# превышает 10000. Определите и запишите в ответе сначала количество пар элементов последовательности, для которых
# произведение элементов не кратно 14, затем максимальную из сумм элементов таких пар. В данной задаче под парой
# подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.
'''
M = [int(i) for i in open('17.txt')]
count = 0
maxi = -9999
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        if (M[i] * M[j]) % 14 != 0:
            count += 1
            maxi = max(maxi, M[i] + M[j])
print(count, maxi)
'''
# Ответ: 40436496 19999

# s = '1213424'
# print(s.split.__doc__)

'''
Return a list of the substrings in the string, using sep as the separator string.

  sep
    The separator used to split the string.

    When set to None (the default value), will split on any whitespace
    character (including \\n \\r \\t \\f and spaces) and will discard
    empty strings from the result.
  maxsplit
    Maximum number of splits (starting from the left).
    -1 (the default value) means no limit.

Note, str.split() is mainly useful for data that has been intentionally
delimited.  With natural text that includes punctuation, consider using
the regular expression module.Return a list of the substrings in the string, using sep as the separator string.

  sep
    The separator used to split the string.

    When set to None (the default value), will split on any whitespace
    character (including \\n \\r \\t \\f and spaces) and will discard
    empty strings from the result.
  maxsplit
    Maximum number of splits (starting from the left).
    -1 (the default value) means no limit.

Note, str.split() is mainly useful for data that has been intentionally
delimited.  With natural text that includes punctuation, consider using
the regular expression module.
'''


A = [1, 2, 3]
B = [4, 5, 6]
C = A + B
print(C)
# [1, 2, 3, 4, 5, 6]



# Тип 9 № 35467
# Электронная таблица содержит результаты ежечасного измерения температуры воздуха на протяжении трёх
# месяцев. Определите, сколько раз за время измерений результат очередного измерения оказывался выше результата
# предыдущего на 2 и более градусов.

M = []
for s in open('9.txt'):
    M += [float(i) for i in s.replace(',', '.').split()]

count = 0
for i in range(0, len(M)-1):
    if M[i+1] - M[i] >= 2:
        count += 1
print(count)


'''
M = [3, 4, 7, 19, 23, 26, 4, 5, 9]
count = 0
for i in range(0, len(M)-1):
    if M[i+1] - M[i] >= 2:
        count += 1
print(count)
'''






# endregion Урок: ******************************************************************


# todo: Сергей = [2, 5, 8, 12, 14, 15, 16, 17, 23, 25]
# на прошлом уроке: Разбирали 17 номера и затронули (чуть-чуть) 9 номер
# на следующем уроке:
