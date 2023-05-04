# region Домашка: ********************************************************

# endregion Домашка: ********************************************************


# region Урок: ********************************************************

'''
f = open('26.txt')
data = f.readlines()
s = data[0].split()
s = int(s[0])
del (data[0])  # первая строка больше не нужна, удаляем ее
for i in range(0, len(data)):
    data[i] = int(data[i])
data = sorted(data)
summa = 0
for count in range(0, len(data)):
    if summa + data[count] > s: break
    summa += data[count]
print(count)
zapas = s - summa
for i in range(0, len(data)):
    if data[i] - data[count - 1] <= zapas:
        itog = data[i]
print(itog)
'''

# Вариант 2
'''
f = open('26.txt')
S, N = [int(i) for i in f.readline().split()]
numbers = sorted([int(i) for i in f.readlines()])
summ = []
for i in range(N):
    if sum(summ) + numbers[i] > S:
        print(i)
        break
    summ.append(numbers[i])
zapas = (S - sum(summ)) + max(summ)
while zapas not in numbers:
    zapas -= 1
print(zapas)
'''
# Ответ: 601 34



# Тип 26 № 35484
# В текстовом файле записан набор натуральных чисел, не превышающих 10**9.
# Гарантируется, что все числа различны. Необходимо определить, сколько в наборе таких пар чётных чисел,
# что их среднее арифметическое тоже присутствует в файле, и чему равно наибольшее из средних арифметических таких пар.
#
# Первая строка входного файла содержит целое число N — общее количество чисел в наборе.
# Каждая из следующих N строк содержит одно число.
#
# В ответе запишите два целых числа: сначала количество пар, затем наибольшее среднее арифметическое.
'''
f = open('26.txt')
N = int(f.readline())
numbers = [int(i) for i in f]
chet = [i for i in numbers if i % 2 == 0]
print(len(chet))

count = 0
maxi = 0
for i in range(0, len(chet)-1):
    for j in range(i+1, len(chet)):
        if (chet[i] + chet[j]) / 2 in numbers:
            count += 1
            maxi = max(maxi, (chet[i] + chet[j]) / 2)
print(count, maxi)
'''

# Вариант 2
'''
import itertools
f = open('26.txt')
N = int(f.readline())
numbers = [int(i) for i in f]
chet = [i for i in numbers if i % 2 == 0]

count = 0
maxi = 0
for pair in itertools.permutations(chet, 2):
    if sum(pair) / 2 in numbers:
        count += 1
        maxi = max(maxi, sum(pair) / 2)

print(count / 2, maxi)
'''
# Ответ: 15 976339247


# endregion Урок: ********************************************************


# todo:   Никита   = [1, 2, 3, 4, 5, 6, 7, 8, 9.1, 11, 12, 13, 14+, 15+, 16, 17, 18, 19-21, 23, 24+, 25.2, 26.1]
# todo: Никита КЕГЭ = [5, 8, 24]
# на прошлом уроке: Поразбирали простые 26 номера на данные пользователей, грузы и свободные места.
# на следующем уроке:
