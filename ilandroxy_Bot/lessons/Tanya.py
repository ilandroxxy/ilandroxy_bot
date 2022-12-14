# region Домашка: ******************************************************************************

# Задача: Следуй правилам
# n = int(input())
# for i in range(1, n+1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)

'''
for i in range(1, n+1):
    if not(5 <= i <= 9) and not(17 <= i <= 37) and not(78 <= i <= 87):
        print(i)
'''

# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************

# СПИСКИ
'''
# list() - это типа данных коллекций, то есть в отличие от переменной список может хранить много значений
# 1) Элементы списка упорядоченные, то есть каждый из них имеет порядковый номер - индекс
# 2) Через индекс можно не только доставать значение элемента списка, но и менять его!

M = []  # пустой список

print(len(M))  # функция len() - возвращает длину списка (то есть кол-во элементов в нем)

x = 12345
s = str(x)  # в целом можем получить длину int-ового числа
l = len(s)

A = [4, 5, 6, 7]
# i  0  1  2  3
# i -4 -3 -2 -1

print(A[0])   # первый элемент списка
print(A[1], A[2])
print(A[-1])  # последний элемент списка


for x in A:  # через такой цикл достаем элементы списка напрямую
    print(x, end=' ')
print()

# цикл позволяющий обращаться к элементам через индекс
for i in range(0, len(A)):  # [0, 4)
    print(A[i], end=' ')
print()


for i in range(0, len(A)):
    A[i] = A[i] ** 2
print(A)
print(*A)
'''


# Функции списков
"""
A = [3, 5, 6, 7, 8, 3, 5, 5]
print(len(A))
print(sum(A))
print(max(A))
print(min(A))

M = []
for x in A:
    if x not in M:
        M.append(x)
print(M, len(M))

B = set(A)  # перевели список в тип данных множество set() таким образом избавились от копий
print(B, len(B))
"""


# Методы списков - метод это функция направленная на один тип данных (объект)
"""
A = [3, 5, 6, 7, 8]
print(A)
A.append(3)  # добавляет новый элемент в конец списка
A.append(3)
print(A)

print(A.count(3))  # возвращает кол-во вхождений элемента в список


A.sort()
print(A)  # отсортировали по возрастанию

A.reverse()  # Перевернули список
print(A)

print(A.index(3))  # вывел индекс первого вхождения (слева) элемента в список


x = A.pop(4)  # забрал значение элемента по индексу и положил в переменную х
print(A, x)

B = A  # это не копия
print(A, B)

M = A.copy()  # настоящие независимая копия списка
A.clear()
print(A, B, M)
"""



# Списочные выражения - способ задать список в одну строку

# Задача: из диапазона достать все четные числа
'''
M = []
for x in range(40, 100+1):
    if x % 2 == 0:
        M.append(x)
print(M)

A = [i for i in range(40, 100+1) if i % 2 == 0]
print(A)

A = [i**2 for i in range(40, 100+1) if i % 2 == 0]
print(A)

S = [i for i in input()]
print(S)

S = [i for i in input().split()]
print(S)

S = [int(i) for i in input('Введите числа через пробел: ').split()]  # если нужно ввести список целых чисел с клавиатуры
print(S)
'''

# Тип 14 № 29662
"""
# Значение выражения 81**17 + 3**24 − 45? записали в системе счисления с основанием 9.
# Сколько цифр «8» содержится в этой записи?
x = 81**17 + 3**24 - 45
M = []
while x > 0:
    print(x)
    M.append(x % 9)
    x //= 9
M.reverse()
print(M)
print(M.count(8))
"""
# Ответ: 10


# Тип 14 № 33484
"""
# Значение выражения 343**6 - 7**10 + 47? записали в системе счисления с основанием 7.
#
# Сколько цифр «6» содержится в этой записи?
x = 343**6 - 7**10 + 47
M = []
while x > 0:
    M.append(x % 7)
    x //= 7
M.reverse()
print(M.count(6))
"""
# Ответ: 9

# endregion Урок: ******************************************************************************


# todo: Татьяна = [2, 14], на следующем уроке: Разбираем 5 номер