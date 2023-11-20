# region Домашка: ******************************************************************

# КЕГЭ № 5496 (Уровень: Средний)
# Текстовый файл содержит только буквы A, C, D, F, O.
# Определите длину самой длинной цепочки символов, которая начинается и заканчивается буквой D,
# а между двумя последовательными буквами D содержит не более двух букв O и произвольное количество других букв.

# todo: Как это можно оптимизировать задачу
'''
s = open('24.txt').readline()
s = s.replace('A', '*').replace('C', '*').replace('F', '*')
s = s.replace('D', 'D D')
for x in s.split():
    if x.count('O') > 2:
        s = s.replace(x, '0', 1)
print(s)
'''

'''
s = open('24.txt').readline()
s = s.replace('A', '*').replace('C', '*').replace('F', '*')
s = s.replace('D', ' D ').split()
print(s)
maxi = 0
for i in range(len(s)):
    if s[i].count('O') <= 2:
        s[i] = '*' * len(s[i])
    if s[i].count('O') > 2:
        s[i] = ' '
print(s)
s = ''.join(s).split()
for i in s:
    maxi = max(maxi, len(i))
print(maxi)
'''

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [125256; 125330],
# числа, имеющие ровно шесть различных чётных натуральных делителей.
# Для каждого найденного числа запишите эти шесть делителей в шесть соседних столбцов на экране с новой строки.
# Делители в строке должны следовать в порядке возрастания.
'''
def Divisors(x):
    divisors = []
    for j in range(1, x+1):
        if x % j == 0 and j % 2 == 0:
            divisors.append(j)
    return divisors


for num in range(125256, 125330+1):
    d = Divisors(num)
    if len(d) == 6:
        print(*d)
'''
# Вариант 2
'''
def Divisors(x):
    divisors = []
    for j in range(1, x+1):
        if x % j == 0:
            divisors.append(j)
    return divisors


for num in range(125256, 125330+1):
    d = Divisors(num)
    if len([x for x in d if x % 2 == 0]) == 6:
        print(*[x for x in d if x % 2 == 0])
'''

# Вариат 3
'''
def Divisors(x):
    divisors = set()
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            if j % 2 == 0:
                divisors.add(j)
            if (x//j) % 2 == 0:
                divisors.add(x//j)
    return sorted(divisors)


for num in range(125256, 125330+1):
    d = Divisors(num)
    if len(d) == 6:
        print(*d)
'''


def Divisors(x):
    divisors = set()
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            divisors.add(j)
            divisors.add(x//j)
    return sorted(divisors)


# endregion Урок: ******************************************************************


# Марк = [2.1, 6.1, 5.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 17.1, 23.1, 24.1, 25.1]
# КЕГЭ  = []
# на следующем уроке:
