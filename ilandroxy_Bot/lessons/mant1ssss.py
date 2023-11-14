
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# Тип 24 № 37159
# Текстовый файл состоит не более, чем из 10**7 строчных букв английского алфавита.
# Найдите максимальную длину подстроки, в которой символы «a» и «d» не стоят рядом.
'''
s = open('24.txt').readline()
s = s.replace('ad', ' ').replace('da', ' ')
print(max([len(substring) for substring in s.split()]))

# Вариант 2
print(max([len(substring) for substring in open('24.txt').readline().replace('ad', ' ').replace('da', ' ').split()]))
'''
import multiprocessing

# Ответ: 2250


# Тип 24 №27694
# Текстовый файл состоит не более чем из 10**6 символов A, B и C.
# Определите максимальную длину цепочки вида ABABAB...
# (составленной из фрагментов AB, последний фрагмент может быть неполным).
'''
print(open('24.txt').readline())
print(len('ABABABABABABABABABABABAB'))
'''
'''
s = open('24.txt').readline()
s = s.replace('AB', '**').replace('A', ' ').replace('B', ' ').replace('C', ' ')
print(max([len(substring) for substring in s.split()]))
'''


# Тип 24 №55820
# Текстовый файл состоит не более, чем из 1200000 символов английского алфавита.
#
# Определите максимальное количество идущих подряд символов, среди которых символы Q, R, S в различных
# комбинациях (с учётом повторений) не стоят рядом.
'''
from itertools import product
pairs = []
for x in product('QRS', repeat=2):
    pairs.append(''.join(x))

s = open('24.txt').readline()
for pair in pairs:
    s = s.replace(pair, '* *')  

print(max([len(substring) for substring in s.split()]))
'''
# Ответ: 544


# todo: Разобрать задачку
# Тип 24 №60266  №39253 №59729 №59794

# Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
# Определите в прилагаемом файле максимальное количество идущих подряд символов
# (длину непрерывной подпоследовательности), среди которых символ T встречается ровно 100 раз.
#
# Для выполнения этого задания следует написать программу.
'''
s = open('24.txt').readline().split('D')
maxi = 0
for i in range(len(s)-1):
    maxi = max(maxi, len(s[i]) + len(s[i+1]))
print(maxi+1)
'''
# Ответ: 354


# Тип 24 №48445
# Текстовый файл содержит только буквы A, C, D, F, O.
# Определите максимальное количество идущих подряд групп символов вида
# согласная + согласная + гласная.
'''
from itertools import product
T = []
for x in product('ACDFO', repeat=3):
    if x[0] in 'CDF' and x[1] in 'CDF' and x[2] in 'AO':
        T.append(''.join(x))
print(T)

s = open('24.txt').readline()
for x in T:
    s = s.replace(x, '*')
for x in 'ACDFO':
    s = s.replace(x, ' ')

print(max([len(substring) for substring in s.split()]))
'''
# Ответ: 5


# Тип 24 №33196
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите символ, который чаще всего встречается в файле сразу после буквы A.
'''
s = open('24.txt').readline()
M = []
for i in range(len(s)-1):
    if s[i] == 'A':
        M.append(s[i+1])

R = []
for x in set(M):
    R.append([M.count(x), x])
print(max(R))


# Вариант 2 
s = open('24.txt').readline()
M = []
for i in range(len(s)-1):
    if s[i] == 'A':
        M.append(s[i+1])
print(max(set(M), key =M.count))
'''

# todo: Добавить в разборы
# Тип 24 №58329
# Текстовый файл состоит не более чем из 10**6 символов арабских цифр (0,1,...,9).
# Определите максимальное количество идущих подряд цифр,
# среди которых сумма двух идущих подряд чисел больше числа следующего за ними.
# Для выполнения этого задания следует написать программу.
'''
M = [int(x) for x in open('24.txt').readline()]
count = 2
maxi = 0
for i in range(len(M)-2):
    if (M[i] + M[i+1]) > M[i+2]:
        count += 1
        maxi = max(maxi, count)
    else:
        count = 2
print(maxi)
'''
# Ответ: 33

# endregion Урок: ******************************************************************


# Марк = [2.1, 6.1, 5.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 17.1, 23.1, 24.1]
# КЕГЭ  = []
# на следующем уроке:
