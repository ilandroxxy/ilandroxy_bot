#Задание №1
'''
M = []
for i in range(10000):
    n = int(input('n: '))
    if n % 2 == 0:
        M.append(n)
        print(M)
    else:
        print('Число нечётное!!')
'''

'''
M = []
n = int(input('n: '))
for x in range(1, n+1):
    if x % 2 == 0:
        M.append(x)
print(M)
'''


#Задание №2
'''
L = []
M = []
S = []
for m in range(3):
    n1 = int(input('n1: '))
    M.append(n1)
print(M)
for l in range(3):
    n2 = int(input('n2: '))
    L.append(n2)
print(L)
for i in range(3):
    S.append(M[i] + L[i])
print(S)
'''

'''
M = [int(i) for i in input().split()]
L = [int(i) for i in input().split()]
# print(L)
# print(M)
while len(M) != len(L):
    if len(M) < len(L):
        M.append(0)
    else:
        L.append(0)
# print(L)
# print(M)

S = []
for i in range(len(M)):
    S.append(M[i] + L[i])
print(S)
'''

'''
ip = '192.45.90.7'
M = ip.split('.')  # метод split() разбивает строку на список строк
print(M)
for i in range(0, len(M)):
    M[i] = int(M[i])
print(M)

#Задание №3

x = str(input('Введите предложение: '))
M = x.split()  # split() без аргумента - разделяет по пробелам
print(M)

maxi = 0
for x in M:
    if maxi < len(x):
        maxi = len(x)
print(maxi)
'''

#Задание №4
'''
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
if x1 == x2 and y1 == y2:
    print('Фигура должна сделать ход!')
elif x1+1 == x2 or y1 == y2:
    print('YES')
elif x1+1 == x2 or y1+1 == y2:
    print('YES')
elif x1-1 == x2 or y1 == y2:
    print('YES')
elif x1-1 == x2 or y1+1 == y2:
    print('YES')
elif x1 == x2 or y1+1 == y2:
    print('YES')
elif x1 == x2 or y1-1 == y2:
    print('YES')
elif x1-1 == x2 or y1-1 == y2:
    print('YES')
elif x1+1 == x2 or y1-1 == y2:
    print('YES')
else:
    print('NO')
'''

# Теория: Правила логики в Питоне
# отрицание (инверсия)  ¬y   <---->   (not(y))
# конъюнкция   x ∧ y  <---->   x and y
# дизъюнкция  x ∨ y  <---->   x or y
# тождество  x ≡ z  <---->   x == z
# Импликация z → w  <---->  z <= w    (¬z ∨ w)


# region Тип 2 № 19051
# Миша заполнял таблицу истинности функции (x ∧ ¬y) ∨ (x ≡ z) ∨ ¬w, но успел
# заполнить лишь фрагмент из трёх различных её строк, даже не указав,
# какому столбцу таблицы соответствует каждая из переменных w, x, y, z.
"""
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x and (not(y))) or (x == z) or (not(w))
                if F == False:
                    print(x, y, z, w, F)
"""
# Ответ: xwzy
# endregion Тип 2 № 19051

# region Тип 2 № 15124
# Логическая функция F задаётся выражением (x ≡ y ) ∨ ((y ∨ z) → x).
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z.
print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = (x == y) or ((y or z) <= x)
            if F == False:
                print(x, y, z, F)
# Ответ: xzy
# endregion Тип 2 № 15124

# Списки (массивы) - list()
'''
M = [1, 2, 3]
print(M, type(M))

print(len(M))  # функция len() выводит длину списка (то есть кол-во элементов в нем)

A = []  # пустой список

M = [3, 4, 5, 6, 7]
#    0  1  2  3  4
# Упорядоченные данные - индексируемые (у каждого элемента есть свой порядковый номер - индекс)
# Индексация начинается с нуля (последний элемент списка имеет индекс -1)
# Элементы списка - можно менять

print(M[2])

for i in range(0, len(M)):
    print(M[i], end=" ")
print()

for i in range(len(M)-1, -1, -1):
    print(M[i], end=" ")
print()


M = [3, 4, 5, 6, 7]
for i in range(0, len(M)):
    M[i] = M[i] ** 2
print(M)
'''

# НА след. уроке: срезы список, функции списков, методы списков, системы счисления, 14 номер

x = 8**2020 + 4**2017 + 26 - 1
M = []
while x > 0:
    M.append(x % 2)
    x //= 2
print(M.count(1))


