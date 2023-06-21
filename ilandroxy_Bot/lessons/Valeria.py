
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# 9
'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    if len(set(M)) == 5 and all(M.count(x) <= 2 for x in M):
        copied = (sum(M) - sum(set(M))) * 2
        sred_copied = copied / 4
        sred = (sum(M) - copied) / 3
        if sred_copied > sred:
            count += 1
print(count)
'''
'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    copied = [x for x in M if M.count(x) == 2]
    another = [x for x in M if M.count(x) == 1]
    if len(copied) == 0 or len(another) == 0:
        continue
    flag1 = len(set(copied)) == 2 and len(another) == 3
    flag2 = sum(copied)/len(copied) > sum(another)/len(another)
    if flag1 + flag2 == 2:
        count += 1
print(count)
'''


# № 7697 (Уровень: Базовый)
# (Грачев Н.) Откройте файл электронной таблицы, содержащей в каждой строке
# пять натуральных чисел. Определите количество строк таблицы, содержащих числа,
# для которых выполнены хотя бы одно условие:
# – все числа в строке равны 18;
# – сумма всех чисел строки делится на 18 без остатка.
# В ответе запишите только число.
'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    if all(i == 18 for i in M) or sum(M) % 18 == 0:
        count += 1
print(count)
'''
# Показать ответ: 923


# № 7674 (Уровень: Сложный)
# (В. Рыбальченко) В файле содержится 5 чисел.
# Определите количество строк, в которых есть 3 числа, которые не повторяются,
# а среднее значение неповторяющихся чисел, меньше среднего значения повторяющихся чисел.
# В ответ укажите найденное количество строк.
'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    copied = [x for x in M if M.count(x) == 2]
    another = [x for x in M if M.count(x) == 1]

    if len(copied) == 0 or len(another) == 0:
        continue
    if sum(another) / len(another) < sum(copied) / len(copied):
        count += 1
print(count)
'''
# Показать ответ: 344


# 17
'''
M = [int(i) for i in open('17.txt')]
MAXIMUM = max([i for i in M if abs(i) % 100 == 17])

count = 0
maxi = -99999
for i in range(0, len(M)-2):
    if sum([len(str(abs(x))) == 3 for x in [M[i], M[i+1], M[i+2]]]) == 1:
        print(M[i], M[i+1], M[i+2])
        if M[i] + M[i+1] + M[i+2] < MAXIMUM:
            count += 1
            maxi = max(maxi, M[i] + M[i+1] + M[i+2])
print(count, maxi)
'''

# № 8504 Апробация 17.05 (Уровень: Базовый)
# В файле содержится последовательность натуральных чисел. Элементы последовательности могут принимать целые
# значения от 1 до 100 000 включительно. Определите количество пар последовательности, в которых хотя бы один
# из элементов является трёхзначным числом, а сумма элементов пары кратна минимальному трёхзначному элементу
# последовательности, оканчивающемуся на 5. В ответе запишите количество найденных пар, затем максимальную из сумм
# элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
M = [int(i) for i in open('17.txt')]
MINIMUM = min([i for i in M if abs(i) % 10 == 5 and len(str(abs(i))) == 3])

count = 0
maxi = -99999
for i in range(0, len(M)-1):
    if len(str(abs(M[i]))) == 3 or len(str(abs(M[i+1]))) == 3:
    # if sum([len(str(abs(x))) == 3 for x in [M[i], M[i+1]]]) >= 1:
        if (M[i] + M[i+1]) % MINIMUM == 0:
            count += 1
            maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)
'''

'''
# i   0    1    2    3    4    5    6
M = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# -i -7   -6   -5   -4   -3   -2   -1

print(M[::])  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(M[2:])  # ['c', 'd', 'e', 'f', 'g']
print(M[:2])  # ['a', 'b']
print(M[::-1])  # ['g', 'f', 'e', 'd', 'c', 'b', 'a']

# Уберем первые два элемента
print(M[2:])

# Последние три элемента
print(M[-3:])  # ['e', 'f', 'g']

# Поменяем элемент посередине на '8'
print(M[:len(M) // 2] + ['*'] + M[(len(M) // 2) + 1:])
# ['a', 'b', 'c', '*', 'e', 'f', 'g']
'''


# 24
'''
s = open('24.txt').readline()
s = 'HHHHHHHHHHHHHHAAABBBHHHHHHCCACACAHHHHHHHACHHHHHHHHHHHHCBB'  # example
s = s.replace('A', 'C').replace('B', 'C')
while 'CC' in s:
    s = s.replace('CC', 'C C')
print(s)  # HHHHHHHHHHHHHHC CC CC CHHHHHHC CC CC CCHHHHHHHC
M = [len(i) for i in s.split()]
print(max(M))
'''

'''
s = open('24.txt').readline()
# s = 'HHHHHHHHHHHHHHAAABBBHHHHHHCCACACAHHHHHHHACHHHHHHHHHHHHCBB'
count = 1
maxi = 1
a = ['AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']
for i in range(len(s) - 1):
    if (s[i] + s[i + 1]) not in a:
        count += 1
        maxi = max(maxi, count)
    else:
        count = 1
print(maxi)
'''

'''
s = sorted('ПЯТНИЦА')
k = 1
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        slovo = a + b + c + d + e + f
                        if a != 'Ц' and slovo.count('И') == 2:
                            if k % 2 != 0:
                                count += 1
                                print(k, slovo)
                        k += 1
print(count)
'''

'''
from itertools import *
k = 1
count = 0
for s in product(sorted('ПЯТНИЦА'), repeat=6):
    slovo = ''.join(s)
    if slovo[0] != 'Ц' and slovo.count('И') == 2:
        if k % 2 != 0:
            count += 1
    k += 1
print(count)
'''

'''
for n in range(4, 10000):
    s = '5' + '2'*n
    while '52' in s or '1122' in s or '2222' in s:
        if '52' in s:
             s = s.replace('52', '11', 1)
        if '2222' in s:
             s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)
    if sum([int(i) for i in s]) == 64:
        print(n)
        break
'''


# endregion Урок: ******************************************************************



# todo: Валерия = [1, 2, 3, 5+, 6, 7, 8+, 9+, 11, 12+, 13, 14+, 15+, 16, 17, 18, 19-21, 22, 23, 24, 25]
# на прошлом уроке: Закрывали задачи с вопросами из домашней работы: 14, 8, 5, 6, 25 через новое решение fnmatch
# на следующем уроке:  #todo: Письменные, Эксель: 9, 19-21, 18, 22, 26
