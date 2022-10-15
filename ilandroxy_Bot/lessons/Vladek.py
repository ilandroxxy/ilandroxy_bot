
'''
m = int(input())
n = int(input())
if m > n:
    for i in range(n, m+1):
        print(i)
else:
    for i in range(n, m-1, -1):
        print(i)
'''

'''

a = int(input())
b = int(input())
c = 0
if a < b:
    for i in range (a, b+1):
        if (a, b % i == 0):
            c = c+1
    if (c <= 0):
        print(i)
'''

'''
a = int(input())
b = int(input())
c = 0
if a < b:
    for i in range (a, b+1):
        if i != 1:
            print(i)  
            
'''


'''
a = int(input())
b = int(input())

for i in range(a, b+1):
    KolDel = 0
    for j in range(1, i+1):
        if i % j == 0:
            KolDel += 1
    if KolDel == 2:
        print(i)

for i in range(a, b+1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag == True:
        print(i)
'''

# Все вместе
'''
x = int(input())   # 5498

summ = 0
pro = 1
count = 0
first = 0
flag = True
while x > 0:
    if flag == True:
        last = x % 10
        flag = False
    first = x % 10
    count += 1
    summ += x % 10
    pro *= x % 10
    x //= 10
print(f'summ = {summ}, pro = {pro}, count = {count}, sred = {summ / count}, first = {first}, first +  last = {first + last}')
'''

#  ¬x  <---->   (not(x))


# Тип коллекций - Списки
'''
M = [1, 2, 3]
print(M, type(M))

M = []  # пустой список
print(M, len(M))  # len() - Длина списка - кол-во элементов в нем


# Списки являются индексируемыми - то есть index - это порядковый номер элемента в списке
A = [4, 6, 7, 23]  # счет индексов начинается с нуля
#    0  1  2  3

print(A[0])  # через индексы мы может обращаться к элементам списка


# Списки являются изменяемым типом данных
print(A)
A[0] = '*'
print(A)


B = [4, 5, 6,7 ,8 ,9, 4 ,2, 4] # 9
#    0  1  2 3  4  5  6  7  8

# форик пробегает по индексам списка (индексный форик)
for i in range(0, len(B)):  # [0, 9)
    B[i] = B[i] ** 2
print(B)


for x in B:
    print(x)

V = [1, 2, 3, 4]
print(V[0], V[-1], V[-2])  # элементы списка можно пройти с обратной стороны через отрицательные индексы, начиная с -1
'''


# Функции работы со списками:
'''
M = [1, 2, 3, 4, 5]
print(len(M))
print(sum(M))
print(max(M))
print(min(M))


x1 = int(input())
x2 = int(input())
x3 = int(input())
A = [x1, x2, x3]
print(sum(A) - max(A) - min(A))
'''

# Методы работы со списками
"""
M = [1, 2, 3, 4, 5]
M.append(0)
M.append(1)
M.append(1)  # добавить элемент в конец списка
print(M)

print(M.count(1))  # кол-во элементов в списке по запросу


M.sort()  # отсортировали по возрастанию
print(M)


M.reverse()  # развернули список (получили по убыванию)
print(M)


print(M.index(1))  # возвращает индекс первого элемента по запросу

x = M.pop(3)  # через индекс забирает элемент из списка в переменную x
print(M)
print(x)
"""

# Методы строк split() и join()

# задача: Проверить ip адрес на корректность
"""  split()
ip = '123.56.45.8'  # 0 <= x <= 255
M = [int(i) for i in ip.split('.')]
print(M)

flag = True
for x in M:
    if not(0 <= x <= 255):
        flag = False
if flag == True:
    print('ip адрес корректный')
else:
    print('ip адрес не корректный')
"""

""" join
M = ['h', 'e', 'l', 'l', 'o']
slovo = ''.join(M)
print(slovo)
"""


# Списочные выражения
"""
M = [i for i in 'Text']
print(M)


M = [i for i in '1234']
print(M)

M = [i*3 for i in '1234']
print(M)

M = [int(i) for i in '1234']
print(M)

# M = [i for i in input("Введите слово: ")]
# print(M)


M = [i for i in range(10)]  # создадим список [0, 9] или [0, 10)
print(M)


M = [i for i in range(2, 10, 2)]
print(M)

import string
Symbols = string.punctuation
print(Symbols)
A = [i for i in input("Введите предложение: ") if i not in Symbols]
predloshenie = ''.join(A)
M = [i for i in predloshenie.split()]
print(M)
"""








# Список четных
"""
M = []
n = int(input('n: '))
for i in range(2, n+1, 2):  # и через range по четным элементам 
    M.append(i)
print(M)

M = []
n = int(input('n: '))
for i in range(1, n+1):
    if i % 2 == 0:  # решили через условие, когда число четное - добавляем
        M.append(i)
print(M)
"""


# Символы всех строк
"""
n = int(input('Введите кол-во строк: '))

M = []
for i in range(n):
    s = input(f's{i+1}: ')
    for x in s:
        M.append(x)
print(M)
"""

# Сумма двух списков
"""
L = [int(i) for i in input('Введите числа через пробел: ').split()]
M = [int(i) for i in input('Введите числа через пробел: ').split()]
print(L)
print(M)

while len(L) != len(M):
    if len(L) < len(M):
        L.append(0)
    else:
        M.append(0)
print(L)
print(M)

S = []
for i in range(0, len(L)):
    S.append(L[i] + M[i])
print(S)
"""








