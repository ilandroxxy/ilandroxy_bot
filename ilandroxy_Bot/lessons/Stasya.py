# Разбираемся с 6, 22, 2 номерами
# Домашка: решить задачку Все вместе


# Последовательность чисел
'''
m = int(input())
n = int(input())
if m < n:
    for i in range(m, n+1):
        print(i)
else:
    for i in range(m, n-1, -1):
        print(i)
'''


# Все вместе
'''
a = int(input())
summ = 0
count = 0
mult = 1
flag = True
while a != 0:
    if flag == True:
        last = a % 10
        flag = False
    count += 1
    summ = summ + (a % 10)
    mult = mult * (a % 10)
    first = a % 10
    a = a // 10

print(f'summ = {summ}, mult = {mult}, count = {count}, sred = {summ / count}, first = {first}, {first}+{last} = {last + first}')
'''

# Простые числа
'''
a = int(input())
b = int(input())
if a == 1:
    a += 1
for i in range(a, b+1):
    for c in range(2, i):
        if i % c == 0:
            break
    else:
        print(i)
'''

'''
a = int(input())
b = int(input())
if a == 1:
    a += 1

for i in range(a, b + 1):
    flag = True
    for c in range(2, i):
        if i % c == 0:
            flag = False
            break
    if flag == True:
        print(i)
'''


# Тип 6 № 33508
# Определите, при каком наименьшем введённом значении переменной s программа выведет число 60.
# Для Вашего удобства программа представлена на четырёх языках программирования.

'''
for i in range(6, 1000000):
    s = i
    s = (s + 1) // 7
    n = 36
    while s < 2050:
        s = s * 2
        n = n + 3
    if n == 60:
        print(f's = {i}, n = {n}')  # n == 60
        break
'''

"""
M = []
for i in range(6, 1000000):
    s = i
    s = (s + 1) // 7
    n = 36
    while s < 2050:
        s = s * 2
        n = n + 3
    if n == 60:
        M.append(i)
print(min(M))
"""
# Ответ: 62




# Тип 6 № 40981
'''
# Определите, при каком наибольшем введённом значении переменной s данная программа выведет число 121.
# Для Вашего удобства программа представлена на четырёх языках программирования.

# Вариант 1
for i in range(0, 100000):
    s = i
    s = s // 10
    n = 1
    while s < 221:
        if n % 2 == 0:
            s = s + 13
        n = n + 5
    if n == 121:
        print('Вариант 1', i, n)
# Ответ: 779

# Вариант 2
for i in range(100000, 1, -1):
    s = i
    s = s // 10
    n = 1
    while s < 221:
        if n % 2 == 0:
            s = s + 13
        n = n + 5
    if n == 121:
        print('Вариант 2', i)
        break

# Вариант 3
M = []
for i in range(0, 100000):
    s = i
    s = s // 10
    n = 1
    while s < 221:
        if n % 2 == 0:
            s = s + 13
        n = n + 5
    if n == 121:
        M.append(i)
print('Вариант 3', max(M))
'''


# Тип 22 № 11249
'''
# Получив на вход число x, этот алгоритм печатает число M. Известно, что x > 200.
# Укажите наименьшее такое (т.е. большее 200) число x, при вводе которого алгоритм печатает 60.

for i in range(201, 10000):
    x = i
    L = x - 30
    M = x + 30
    while L != M:
        if L > M:
            L = L - M
        else:
            M = M - L
    if M == 60:
        print(i, M)
        break
'''
# Ответ: 210




# Тип 22 № 3273
'''
# Получив на вход число x, эта программа печатает два числа, L и M.
# Укажите наибольшее из таких чисел x, при вводе которых алгоритм печатает сначала 3, а потом 10.

# Вариант 1
for i in range(0, 10000):
    x = i
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if M < x and x % 2 == 1:
            M = (x % 10)*2
        x = x // 10
    if L == 3 and M == 10:
        print('Вариант 1', i, L, M)

# Вариант 2
for i in range(10000, 1, -1):
    x = i
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if M < x and x % 2 == 1:
            M = (x % 10)*2
        x = x // 10
    if L == 3 and M == 10:
        print('Вариант 2', i, L, M)
        break
'''
# Ответ: 985


# Тип 2 № 26974
# Логическая функция F задаётся выражением (x ∨ y) ∧ ¬(y ≡ z) ∧ ¬w.
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки.
# Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.

# Кол-во строк в таблице: 2 * 2 * 2 * 2 (x*y*z*w) = 16 строк

# Функции в математической логике
# Инверсия (отрицание)     ¬w   <---->   (not(w))
# Конъюнкция (логическое умножение)    x ∧ y  <---->   x and y
# Дизъюнкция (логическое сложение)    x ∨ y   <--->   x or y
# Импликация    x → y   <---->   x <= y
# Тождество   x ≡ y   <---->  x == y


print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x or y) and (not(y == z)) and (not(w))  # (x ∨ y) ∧ ¬(y ≡ z) ∧ ¬w.
                if F == True:
                    print(x, y, z, w, F)
