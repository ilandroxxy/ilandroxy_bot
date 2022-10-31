
# region Тип 17 № 37341
'''
#В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности,
# разность которых четна и хотя бы одно из чисел делится на 19, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен
f = open("17.txt", 'r')
M = [int(i) for i in f]
count = 0
maxi = 0
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        if (M[i] - M[j]) % 2 == 0 and (M[i] % 19 == 0 or M[j] % 19 == 0):
            count += 1
            if maxi < M[i] + M[j]:
                maxi = M[i] + M[j]

print(count, maxi)
'''
# Ответ: 2551262 19994
# endregion Тип 17 № 37341

# region Тип 17 № 37369
'''
# В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности, у которых разность элементов кратна 80,
# затем максимальную из разностей элементов таких пар. В данной задаче под парой подразумевается два
# различных элемента последовательности. Порядок элементов в паре не важен.
f = open("17.txt", "r")
M = [int(i) for i in f]
count = 0
maxi = 0
for i in range(len(M)-1):
    for j in range(i + 1, len(M)):
        if (M[i] - M[j]) % 80 == 0 or (M[j] - M[i]) % 80 == 0:
            count += 1
            if maxi < (M[i] - M[j]):  # максимальную из разностей элементов
                maxi = (M[i] - M[j])
print(count, maxi)
'''
# Ответ: 625876 9920
# endregion Тип 17 № 37369

# region Тип 17 № 45251
'''
# В файле содержится последовательность натуральных чисел. 
# Элементы последовательности могут принимать целые значения от 1 до 100 000 включительно. 
# Определите количество пар последовательности, в которых хотя бы одно число делится на минимальный элемент последовательности, кратный 21. 
# Гарантируется, что такой элемент в последовательности есть. 
# В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар. 
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
f = open("17.txt", 'r')
M = [int(i) for i in f]
mini = 99999
for i in range(0, len(M)):
    if M[i] % 21 == 0 and M[i] < mini:
        mini = M[i]
print(mini)
count = 0
maxi = -9999
for i in range(0, len(M) - 1):
    if M[i] % mini == 0 or M[i+1] % mini == 0:
        count += 1
        if maxi < M[i] + M[i+1]:
            maxi = M[i] + M[i+1]
print(count, maxi)
'''
# Ответ 126 171120
# endregion Тип 17 № 45251

# region Тип 17 № 37360
# В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности, у которых сумма элементов кратна 120,
# затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

f = open('17.txt', 'r')
M = [int(i) for i in f]

count = 0
maxi = 0
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        if (M[i] + M[j]) % 120 == 0:
            count += 1
            if maxi < (M[i] + M[j]):
                maxi = (M[i] + M[j])
print(count, maxi)
# Ответ: 414830 19920
# endregion Тип 17 № 37360

# region Тип 17 № 40733
'''
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10000. Назовём парой два идущих подряд элемента последовательности.
# Определите количество пар, в которых хотя бы один из двух элементов делится на 3 и хотя бы один из
# двух элементов меньше среднего арифметического всех чётных элементов последовательности.
# В ответе запишите два числа: сначала количество найденных пар, а затем — максимальную сумму элементов таких пар.

f = open('17.txt', 'r')
M = [int(i) for i in f]

summ = 0
kol = 0
for i in range(0, len(M)):
    if M[i] % 2 == 0:
        summ += M[i]
        kol += 1
sred = summ / kol


count = 0
maxi = 0
for i in range(0, len(M)-1):
    if (M[i] % 3 == 0 or M[i+1] % 3 == 0) and (M[i] < sred or M[i+1] < sred):
        count += 1
        if maxi < M[i] + M[i+1]:
            maxi = M[i] + M[i+1]
print(count, maxi)
'''
# Ответ: 2288 14875
# endregion Тип 17 № 40733

# region Тип 17 № 37337
'''
# В файле содержится последовательность из 10000 натуральных чисел.
# Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности, у которых
# различные остатки от деления на d=160 и хотя бы одно из чисел делится на p=7, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

f = open('17.txt', 'r')
M = [int(i) for i in f]
d = 160
p = 7

count = 0
maxi = 0

for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        if (M[i] % d) != (M[j] % d) and (M[i] % p == 0 or M[j] % p == 0):
            count += 1
            if maxi < (M[i] + M[j]):
                maxi = (M[i] + M[j])
print(count, maxi)
'''
# Ответ: 12749665 19989
# endregion Тип 17 № 37337

# region Тип 17 № 37345
'''
# В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности, для которых произведение элементов делится без остатка на 62,
# затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.


f = open('17.txt', 'r')
M = [int(i) for i in f]

count = 0
maxi = 0

for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        if (M[i] * M[j]) % 62 == 0:
            count += 1
            if maxi < (M[i] + M[j]):
                maxi = (M[i] + M[j])
print(count, maxi)
'''
# Ответ: 2284645 19920.
# endregion Тип 17 № 37345

# region Тип 17 № 37357
'''
# В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности, у которых сумма элементов кратна 8, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

f = open('17.txt', 'r')
M = [int(i) for i in f]

count = 0
maxi = 0

for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        if (M[i] + M[j]) % 8 == 0:
            count += 1
            if maxi < (M[i] + M[j]):
                maxi = (M[i] + M[j])
print(count, maxi)
'''
# Ответ: 6243772 19992
# endregion Тип 17 № 37357

# region Тип 17 № 45251
'''
# В файле содержится последовательность натуральных чисел.
# Элементы последовательности могут принимать целые значения от 1 до 100 000 включительно.
# Определите количество пар последовательности, в которых хотя бы одно число делится на минимальный элемент последовательности, кратный 21.
# Гарантируется, что такой элемент в последовательности есть. В ответе запишите количество найденных пар, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.

f = open('17.txt', 'r')
A = [int(i) for i in f if int(i) % 21 == 0]
mini = min(A)

f = open('17.txt', 'r')
M = [int(i) for i in f]

count = 0
maxsum = 0
for i in range(0, len(M)-1):
    if M[i] % mini == 0 or M[i+1] % mini == 0:
        count += 1
        if maxsum < (M[i] + M[i+1]):
            maxsum = M[i] + M[i + 1]
print(count, maxsum)
'''
# Ответ: 126 171120
# endregion Тип 17 № 45251

# region Тип 17 № 47221
"""
# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от −10000 до 10000 включительно.
# Определите количество пар последовательности, в которых только одно число оканчивается на 3,
# а сумма квадратов элементов пары не меньше квадрата максимального элемента последовательности, оканчивающегося на 3.
# В ответе запишите два числа: сначала количество найденных пар, затем максимальную из сумм квадратов элементов таких пар.
# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.

f = open('17.txt', 'r')
M = [int(i) for i in f]

maxi = 0
for x in M:
    if str(x)[-1] == '3':
        if maxi < x:
            maxi = x
maxi **= (1/2)

count = 0
MAXI = 0
for i in range(0, len(M)-1):
    if (M[i] % 10 == 3 and M[i+1] % 10 != 3) or (M[i] % 10 != 3 and M[i+1] % 10 == 3):
        if (M[i]**2 + M[i+1]**2) < (maxi):
            count += 1
            if MAXI < (M[i]**2 + M[i+1]**2):
                MAXI = (M[i]**2 + M[i+1]**2)
print(count, MAXI)
"""
# endregion Тип 17 № 47221

# region Тип 17 № 46975
'''
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10000.
# Назовём парой два идущих подряд элемента последовательности.
# Определите количество пар, в которых один из двух элементов делится на 3,
# а другой меньше среднего арифметического всех чётных элементов последовательности.
# В ответе запишите два числа: сначала количество найденных пар, а затем — максимальную сумму элементов таких пар.

f = open('17.txt', 'r')
A = [int(i) for i in f if int(i) % 2 == 0]
sred = sum(A) / len(A)

f = open('17.txt', 'r')
M = [int(i) for i in f]


# summ = 0
# kol = 0
# for i in range(0, len(M)):
#     if M[i] % 2 == 0:
#         summ += M[i]
#         kol += 1
# sred = summ / kol
#
# print(sred)

count = 0
maxi = 0
for i in range(0, len(M)-1):
    if (M[i] % 3 == 0 and M[i+1] < sred) or (M[i] < sred and M[i+1] % 3 == 0):
        count += 1
        if maxi < (M[i] + M[i+1]):
            maxi = (M[i] + M[i + 1])
print(count, maxi)
'''
# Ответ: 1711 14666
# endregion Тип 17 № 46975