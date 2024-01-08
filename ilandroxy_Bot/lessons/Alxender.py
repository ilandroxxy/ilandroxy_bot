# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# № 12248 ЕГКР 16.12.23 (Уровень: Базовый)
# Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
# F(n)=1 при n≤3;
# F(n)=(n+3)×F(n−2), если n>3.
# Чему равно значение выражения F(2028)/F(2024)?
'''
import sys
sys.setrecursionlimit(10000)

def F(n):
    if n <= 3:
        return 1
    if n > 3:
        return (n+3) * F(n-2)


print(F(2028) / F(2024))

# F(2028) = (2031) * F(2026)
# F(2026) = (2029) * F(2024) / F(2024)

print(2031 * 2029)
'''
# Ответ: 4120899

# [Previous line repeated 996 more times]
# RecursionError: maximum recursion depth exceeded


# Тип 23 №37158
# 1. Прибавить 1
# 2. Прибавить 2
# 3. Умножить на 3
#
# Сколько существует таких программ, которые исходное число 2 преобразуют в число 19
# и при этом траектория вычислений программы проходит через 9 и не проходит через 12?
'''
def F(start, stop):
    if start == stop:
        return 1
    elif start > stop or start == 12:
        return 0
    else:
        return F(start+1, stop) + F(start+2, stop) + F(start*3, stop)


print(F(2, 9) * F(9, 19))


def F(start, stop):
    if start >= stop or start == 12:
        return start == stop
    return F(start+1, stop) + F(start+2, stop) + F(start*3, stop)


print(F(2, 9) * F(9, 19))
'''
# Ответ: 650


# Тип 24 №27688
# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z.
# Определите длину самой длинной последовательности, состоящей из символов Z.
# Хотя бы один символ Z находится в последовательности.
'''
# Вариант 1
s = open('24.txt').readline()
cnt = 1
maxi_cnt = 0
for i in range(len(s)-1):
    # if s[i] == 'Z' and s[i+1] == 'Z':
    if s[i:i+2] == 'ZZ':
        cnt += 1
        maxi_cnt = max(maxi_cnt, cnt)
    else:
        cnt = 1
print(maxi_cnt)

# Вариант 2
s = open('24.txt').readline()
s = s.replace('X', ' ').replace('Y', ' ')
print(max([len(x) for x in s.split()]))

# Вариант 3
print(max([len(x) for x in open('24.txt').readline().replace('X', ' ').replace('Y', ' ').split()]))

# Вариант 4
s = open('24.txt').readline()
print(s)
print(len('ZZZZZZZ'))
'''
# Ответ: 7


# Тип 24 №27695
# Текстовый файл состоит не более чем из 106 символов L, D и R.
# Определите максимальное количество идущих подряд символов, среди которых каждые два соседних различны.
'''
s = open('24.txt').readline()
cnt = 1
maxi = 0
for i in range(0, len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1
        maxi = max(maxi, cnt)
    else:
        cnt = 1
print(maxi)
'''
# Ответ: 45


# Тип 24 № 52195
# Текстовый файл содержит только буквы A, C, D, F, O.
# Определите длину самой длинной цепочки символов, которая начинается и заканчивается буквой D,
# а между двумя последовательными буквами D содержит не более двух букв O
# и произвольное количество других букв.
'''
s = open('24.txt').readline()
s = s.replace('D', '* *')
print([x for x in s.split() if x.count('O') <= 2])
print(max([len(x) for x in s.split() if x.count('O') <= 2]))
'''

# todo Исправить решение на Решу егэ
'''
s = open('24.txt').readline().split('D')
mx = 0
c = 1
r = ''
for i in range(len(s)):
    print(s[i])
    if s[i].count('O') <= 2:
        c += len(s[i]) + 1
        r += s[i]
        print(r)
        mx = max(mx, c)
    else:
        c = 1
        r = ''
print(mx)
'''
# Ответ: 255


# Тип 24 №37131
# Текстовый файл содержит только заглавные буквы латинского алфавита (ABC…Z).
# Определите наибольшую длину цепочки символов, среди которых нет символов K и L, стоящих рядом.
'''
s = open('24.txt').readline()
s = s.replace('KL', '* *').replace('LK', '* *')
print(max([len(x) for x in s.split()]))
'''
# Ответ: 2796


# Тип 24 №27699
# Текстовый файл состоит не более чем из 106 символов L, D и R.
# Определите максимальную длину цепочки вида LDRLDRLDR...
# (составленной из фрагментов LDR, последний фрагмент может быть неполным).
'''
s = open('24.txt').readline()
print(s)
print(len('LDRLDRLDRLDRLDR'))
'''
# Ответ: 15


# Тип 24 №48445
# Текстовый файл содержит только буквы A, C, D, F, O.
# Определите максимальное количество идущих подряд групп символов вида
# согласная + согласная + гласная.
'''
s = open('24.txt').readline()
s = s.replace('O', 'A')
s = s.replace('C', 'D').replace('F', 'D')
s = s.replace('DDA', '*')
for x in 'AD':
    s = s.replace(x, ' ')
print(max([len(x) for x in s.split()]))
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
for x in set(s):
    R.append([M.count(x), x])
    # print(x, M.count(x))
print(max(R)[1])


f = open('24.txt').readline()
j = ''
for i in range(len(f) - 1):
    if f[i] == 'A':
        j += f[i + 1]
print(max(set(j), key=j.count))
'''
# Ответ: G

# endregion Урок: ******************************************************************

# todo Продолжаем 24 номер

# Александр = [9.1, 15.1, 16.1, 17.1, 23.1, 24.1, 25.1]
# КЕГЭ  = []
# на следующем уроке:
