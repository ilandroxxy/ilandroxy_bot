
# region Домашка

# endregion Домашка


# region Урок

# Тип 24 № 27688
# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z.
# Определите длину самой длинной последовательности, состоящей из символов Z.
# Хотя бы один символ Z находится в последовательности.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.


# Вариант 1
'''
f = open('24.txt')
s = f.readline()
№ print(s)

# XZZZY
count = 1
MaxCount = 0
for i in range(0, len(s)):
    if s[i] == 'Z' and s[i+1] == 'Z':
        count += 1
        MaxCount = max(count, MaxCount)
    else:
        count = 1
print(MaxCount)
'''

# Вариант 2
# print(max([len(i) for i in open('24.txt').readline().replace('X', ' ').replace('Y', ' ').split()]))

# ip = '194.32.23.245'
# M = ip.split('.')
# print(M)
#
# A = [int(i) for i in ip.split('.')]
# print(A)



# Тип 24 № 27699
# Текстовый файл состоит не более чем из 10**6 символов L, D и R. Определите максимальную длину цепочки вида LDRLDRLDR...
# (составленной из фрагментов LDR, последний фрагмент может быть неполным).
#
# Для выполнения этого задания следует написать программу. Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

# print(max([len(i) for i in open('24.txt').readline().replace('LDR', '***').replace('L', ' ').replace('D', ' ').replace('R', ' ').split()]))



# Тип 24 № 36879
'''
# Текстовый файл содержит строки различной длины.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# В строках, содержащих менее 25 букв G, нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.

f = open('24.txt')
M = f.readlines()

A = []
for s in M:
    if s.count('G') < 25:
        A.append(s)

import string
Alphabet = string.ascii_uppercase
print(Alphabet)

maxi = 0
for s in A:
    for i in Alphabet:
        maxi = max(maxi, s.rindex(i) - s.index(i))
print(maxi)
'''
# Ответ: 1001




# Тип 24 № 33769
'''
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле после двух одинаковых символов.
import string
Alphabet = string.ascii_uppercase
print(Alphabet)

f = open('24.txt')
s = f.readline()

A = []
for i in range(0, len(s)-2):
    if s[i] == s[i+1]:
        A.append(s[i+2])

dic = {}
for i in Alphabet:
    if maxi < A.count(i):
        maxi = A.count(i)
        dic[maxi] = i
print(dic)
'''
# Ответ: K



# Тип 24 № 47228
'''
# Текстовый файл состоит из символов A, C, D, F и O.
#
# Определите максимальное количество идущих подряд пар символов вида
#
# согласная + гласная.

# BABABAB
#
# Для выполнения этого задания следует написать программу.

f = open('24.txt')
s = f.readline()

sogl = 'CDF'
glas = 'AO'

count = 0
maxi = 0
st = ''
for i in range(0, len(s)-1):
    if (s[i] in sogl and s[i+1] in glas) or (s[i+1] in sogl and s[i] in glas):
        count += 1
        st += s[i]
        if maxi < count:
            maxi = count
            print(st)
    else:
        st = ''
        count = 0
print(maxi)
'''


# Тип 24 № 36037
# Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки XZZY.
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

# print(max([len(i) for i in open('24.txt').readline().replace('XZZY', ' ').split()]) + 6)

# Ответ: 1713





# Тип 24 № 45258
'''
# Текстовый файл состоит из символов A, B и C.
# Определите максимальное количество идущих подряд пар символов AB или CB в прилагаемом файле.
# Искомая подпоследовательность должна состоять только из пар AB, или только из пар CB, или только из пар AB и CB в произвольном порядке следования этих пар.
# Для выполнения этого задания следует написать программу.


f = open('24.txt')
s = f.readline()

count = 1
maxi = 0
st = ''
st_max = ''
for i in range(0, len(s)-1):
    if (s[i] + s[i+1]) == 'AB' or (s[i] + s[i+1]) == 'BA' or (s[i] + s[i+1]) == 'CB' or (s[i] + s[i+1]) == 'BC':
        count += 1
        st += s[i]
        if maxi < count:
            maxi = count
            st_max = st
    else:
        st = ''
        count = 1
print(st_max)
print(maxi/2)

print(len('CBABABABABCBCBABABCBABCBCBCBCBABABCBCBABCBABABCBCBCBCBABABCBABABCBABABCBCBCBABABABCBCBCBABABCBCBABCBCBCBABCBCBCBABCBABABCBCBCBCBA'))
'''
# Ответ: 65





# endregion Урок


# todo:  Гриша = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], на следующем уроке: