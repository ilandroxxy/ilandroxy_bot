
# region Домашка: ******************************************************************************

# Тип 17 № 47014
'''
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10000.
# Назовём парой два идущих подряд элемента последовательности. Определите количество пар,
# в которых один из двух элементов делится на 5, а другой меньше среднего арифметического всех нечётных элементов последовательности.
# В ответе запишите два числа: сначала количество найденных пар, а затем— максимальную сумму элементов таких пар.

m = [int(i) for i in open('17.txt')]

kol = 0
summa = 0
for x in m:
    if x % 2 != 0:
        summa += x
        kol += 1
sred = summa / kol

count = 0
maxi = 0
for i in range(0, len(m) - 1):
    if (m[i] % 5 == 0 and m[i+1] < sred) or (m[i+1] % 5 == 0 and m[i] < sred):
        count += 1
        maxi = max(maxi, m[i] + m[i+1])
print(count, maxi)
# 1061 14847
'''

# Тип 17 № 37359
'''
# В файле содержится последовательность из 10 000 целых положительных чисел. 
# Каждое число не превышает 10 000. Определите и запишите в ответе сначала количество пар элементов последовательности, 
# у которых сумма элементов кратна 117, затем максимальную из сумм элементов таких пар. 
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

m = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
for i in range(0, len(m)):
    for j in range(i+1, len(m)):
        if (m[i] + m[j]) % 117 == 0:
            count += 1
            maxi = max(maxi, m[i] + m[j])
print(count, maxi)
# 427120 19890
'''

# Тип 17 № 37337
'''
# В файле содержится последовательность из 10 000 натуральных чисел. Каждое число не превышает 10 000. 
# Определите и запишите в ответе сначала количество пар элементов последовательности, 
# у которых различные остатки от деления на d  =  160 и хотя бы одно из чисел делится на p  =  7, 
# затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента последовательности. 
# Порядок элементов в паре не важен.

m = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
for i in range(0, len(m)):
    for j in range(i+1, len(m)):
        if ((m[i] % 160) != (m[j] % 160)) and ((m[i] % 7 == 0) or (m[j] % 7 == 0)):
            count += 1
            maxi = max(maxi, m[i] + m[j])
print(count, maxi)
# 12749665 19989
'''

# Тип 17 № 37368
'''
# В файле содержится последовательность из 10 000 целых положительных чисел. 
# Каждое число не превышает 10 000. Определите и запишите в ответе сначала количество пар элементов последовательности, 
# у которых сумма элементов кратна 60 и хотя бы один элемент из пары делится на 40, 
# затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента последовательности. 
# Порядок элементов в паре не важен.

m = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
for i in range(0, len(m)+1):
    for j in range(i+1, len(m)):
        if ((m[i] + m[j]) % 60 == 0) and ((m[i] % 40 == 0) or (m[j] % 40 == 0)):
            count += 1
            maxi = max(maxi, m[i] + m[j])
print(count, maxi)
# 29278 19860
'''

# Тип 9 № 45243
'''
# Откройте файл электронной таблицы, содержащей в каждой строке пять натуральных чисел. 
# Определите количество строк таблицы, в которых квадрат суммы максимального и минимального 
# чисел в строке больше суммы квадратов трёх оставшихся.

count = 0
for s in open('9.txt'):
    m = sorted([int(i) for i in s.split()])
    if (m[0] + m[4])**2 > (m[1]**2 + m[2]**2 + m[3]**2):
        count += 1
print(count)
# 2640
'''

# endregion Домашка: ******************************************************************************




# region Урок: ******************************************************************************


# Тип 9 № 27522 i
# Откройте файл электронной таблицы, содержащей вещественные числа — результаты ежечасного измерения температуры воздуха на протяжении трёх месяцев.

# Сколько раз встречалась температура, выше округленного до десятых среднего арифметического значения всех чисел в таблице?
'''
A = []
for s in open('9.txt'):
    M = [float(i) for i in s.replace(',', '.').split()]
    A += M

sred = round(sum(A) / len(A), 1)
count = 0
for x in A:
    if x > sred:
        count += 1
print(count)
'''

# Вариант 2
'''
A = []
for s in open('9.txt'):
    M = [float(i) for i in s.replace(',', '.').split()]
    A += M

sred = round(sum(A) / len(A), 1)
print(len([x for x in A if x > sred]))
'''

# Вариант 3
'''
A = []
for s in open('9.txt'):
    A += [float(i) for i in s.replace(',', '.').split()]

print(len([x for x in A if x > round(sum(A) / len(A), 1)]))
'''

# Вариант 4
'''
A = [float(i) for i in open('9.txt').read().replace(',', '.').split()]
print(len([x for x in A if x > round(sum(A) / len(A), 1)]))
'''
# Ответ: 1192


# Тип 9 № 36864
# Электронная таблица содержит результаты ежечасного измерения температуры воздуха на протяжении трёх месяцев.
# Определите, сколько раз за время измерений минимальная суточная температура оказывалась ниже среднесуточной на 8 и более градусов.
'''
count = 0
for s in open('9.txt'):
    M = [float(i) for i in s.replace(',', '.').split()]
    if (sum(M) / len(M)) - min(M) >= 8:
        count += 1
print(count)
'''
# Ответ: 51



# Тип 24 № 27692
# Текстовый файл состоит не более чем из 10**6 символов A, B и C. Определите максимальное количество идущих подряд символов B.
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

# Вариант 1
'''
s = open('24.txt').readline()
count = 1
max_count = 0
for i in range(0, len(s)-1):
    if s[i] == 'B' and s[i+1] == 'B':
        count += 1
        # if max_count < count:
        #     max_count = count
        max_count = max(max_count, count)
    else:
        count = 1
print(max_count)
'''

# Вариант 2
'''
s = open('24.txt').readline()
s = s.replace('A', ' ').replace('C', ' ')
M = [len(i) for i in s.split()]
print(max(M))
'''

# Вариант 3
'''
print(max([len(i) for i in open('24.txt').readline().replace('A', ' ').replace('C', ' ').split()]))
'''

# Вариант 4
'''
s = open('24.txt').readline()
print(s)
print(len('BBBBBBBBBBB'))
'''


# Тип 24 № 27689
# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z.
# Определите максимальную длину цепочки вида XYZXYZXYZXY... (составленной из фрагментов XYZ, последний фрагмент может быть неполным).
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
s = open('24.txt').readline()
print(s)
print(len('XYZXYZXYZXYZX'))
'''


'''
s = open('24.txt').readline()
count = 2
max_count = 0
for i in range(0, len(s)-2):
    # if (s[i] == 'X' and s[i+1] == 'Y' and s[i+2] == 'Z') or (s[i] == 'Y' and s[i+1] == 'Z' and s[i+2] == 'X') or (s[i] == 'Z' and s[i+1] == 'X' and s[i+2] == 'Y'):
    if s[i:i+3] == 'XYZ' or s[i:i+3] == 'YZX' or s[i:i+3] == 'ZXY':
        count += 1
        max_count = max(max_count, count)
    else:
        count = 2
print(max_count)
'''
# Ответ: 13



# Тип 24 № 36037
# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
s = open('24.txt').readline()
# s = 'XZZYAAAXZZY'
s = s.replace('XZZY', ' ')
M = [len(i) for i in s.split()]
print(3+max(M)+3)    # длина подстроки XZZY - 1 = 3
'''
# XZZYAAAXZZY
# некорректно AAA
# корректно ZZYAAAXZZ

# Ответ: 1713

# Тип 24 № 37159
# Текстовый файл состоит не более, чем из 10**7 строчных букв английского алфавита.
# Найдите максимальную длину подстроки, в которой символы «a» и «d» не стоят рядом.
#
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.
'''
s = open('24.txt').readline()
s = s.replace('ad', ' ').replace('da', ' ')
M = [len(i) for i in s.split()]
print(1+max(M)+1)  # длина подстроки ad, da - 1 = 1
'''
# Ответ: 2252


# Тип 24 № 33526
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле между двумя одинаковыми символами.
'''
M = []
s = open('24.txt').readline()
for i in range(0, len(s)-2):
    if s[i] == s[i+2]:
        M.append(s[i+1])

maxi = 0
result = 0
alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
for a in alphabet:
    if maxi < M.count(a):
        maxi = M.count(a)
        result = a
print(result)
'''

# Вариант 2
'''
M = []
s = open('24.txt').readline()
for i in range(0, len(s)-2):
    if s[i] == s[i+2]:
        M.append(s[i+1])

my_dict = {}
alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
for a in alphabet:
    my_dict[a] = M.count(a)

for key in my_dict:
    print(key, my_dict[key])

print(max(my_dict.values()))

for key in my_dict:
    if my_dict[key] == 1517:
        print(key)
'''
# endregion Урок: ******************************************************************************


# todo: Дмитрий = [2, 5, 8, 9.1, 12, 14+, 15+, 16, 17, 23, 24.1, 25.2]
# на прошлом уроке: Посмотрели 9 номер через Пайтон и начали разбирать 24 номер на строки.
# на следующем уроке: Добиваем 24 номер, начинаем ЭКСЕЛЬ задачи: 3, 9, 10, 18, 19-21, 22