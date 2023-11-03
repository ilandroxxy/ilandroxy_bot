# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Теория списков (list)
# - Хранят в себе неограниченное кол-во элементов разных типов данных
# - Каждый элемент в списки имеет свой порядковый номер - индекс
# - Индексы могут считаться слева-направо начиная с 0 или справа-налево начиная с -1
# - Элементы списка можно изменять через их индексы (в отличие от строк и кортежей)
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(f'Первый элемент списка: {M[0]} \n'
      f'Последний элемент списка: {M[-1]}')

print(M[3])
print(M[-2])

print(M)  # ['a', 'b', 'c', 'd', 'e']
M[1] = 'B'  # таким образом мы изменили значение элемента под первым индексом
print(M)  # ['a', 'B', 'c', 'd', 'e']
'''

# Пробежать элементы списка через цикл:
'''
for x in M:
    print(x, end=' ')  # a B c d e
print()

for i in range(len(M)):  # len() - возвращает длину списка
    print(M[i], end=' ')  # a B c d e
print()

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'B', 'cc', 'ddd', 'eeee']
'''

# Срезы списков:
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(M[1:4])  # ['b', 'c', 'd']
print(M[:4])  # ['a', 'b', 'c', 'd'] - все, что слева
print(M[2:])  # ['c', 'd', 'e'] - все, что справа
print(M[:])  # ['a', 'b', 'c', 'd', 'e'] - все, что слева и справа
print(M[::2])  # ['a', 'c', 'e']
print(M[::-1])  # ['e', 'd', 'c', 'b', 'a'] - это аналог метода .reverse()
'''

# Функции списков
'''
M = [3, 4, 5, 3, 4, 5]
print(len(M))  # возвращает длину списка (то есть кол-во элементов в нем)
print(sum(M))
print(max(M))
print(min(M))

print(set(M))  # {3, 4, 5} - при конвертации в множество - удаляются все копии элементов
print(len(set(M)))  # 3 - сколько различных элементов лежит внутри списка?

print(sorted(M))  # [3, 3, 4, 4, 5, 5] - сортировка по возрастанию
print(sorted(M, reverse=True))  # [5, 5, 4, 4, 3, 3] - сортировка в обратном порядке
# sorted() работает со всеми коллекциями и строками
print(sorted('12345'))  # ['1', '2', '3', '4', '5']
'''

# Ментоды списков (Методы - это частный случай функций)
'''
M = [3, 4, 5]

M.append(5)  # добавить новый элемент в конец списка
M.append(6)
M.append(6)
print(M)  # [3, 4, 5, 5, 6, 6]
M = M + [7, 8, 9]
print(M)  # [3, 4, 5, 5, 6, 6, 7, 8, 9]  - добавили элементы справа
M = [1, 2] + M
print(M)  # [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9] - добавили элементы слева

print(M.count(5))  # 2 - возвращает кол-во вхождений элемента в список
print(M.index(5))  # 4 - возвращает индекс первого найденного элемента

M.sort()
print(M)  # [1, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9]

M.reverse()
print(M)  # [9, 8, 7, 6, 6, 5, 5, 4, 3, 2, 1]
'''

# Генераторы списков
'''
M = [x for x in range(10)]
print(M)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

M = [x**2 for x in range(10)]
print(M)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

M = [x for x in range(10) if x % 2 == 0]
print(M)  # [0, 2, 4, 6, 8]


# Открытие .txt файла с 17-го номера
M = [int(x) for x in open('17.txt')]

# Получите разность сумм четных и нечетных чисел
chet = [x for x in M if x % 2 == 0]
nechet = [x for x in M if x % 2 != 0]
print(sum(chet) - sum(nechet))  # -85013
'''

# Введите список целых чисел с клавиатуры
'''
n = int(input('n: '))
M = []
for i in range(n):
    x = int(input('x: '))
    M.append(x)
print(M)

M = [int(x) for x in input('Введите цифры: ').split() if x.isdigit()]
# Введите цифры: 1234  ytfgyhuj 23456 h435jh43j  2345
print(M)  # [1234, 23456, 2345]
'''


# Тип 14 №29201
# Значение выражения 49**6*7**19 - 7**9 - 21 записали в системе счисления с основанием 7.
# Сколько цифр 6 содержится в этой записи?
'''
x = 49**6*7**19 - 7**9 - 21
M = []
while x > 0:
    M.append(x % 7)
    x //= 7
M.reverse()
print(M.count(6))
'''
# Ответ: 28


# Тип 14 №28552
# Значение выражения 216**6 + 216**4 + 36**6 - 6**14 - 24 записали в системе счисления с основанием 6.
# Сколько различных цифр содержит эта запись?
'''
x = 216**6 + 216**4 + 36**6 - 6**14 - 24
M = []
while x > 0:
    M.append(x % 6)
    x //= 6
M.reverse()
print(len(set(M)))   
'''
# Ответ: 4

# Тип 14 №48387
# Операнды арифметического выражения записаны в системах счисления с основаниями 11 и 19:
#
# x341y_11 + 56x1y_19
#
# В записи чисел переменными x и y обозначены допустимые в данных системах счисления неизвестные цифры.
# Определите значения x и y, при которых значение данного арифметического выражения будет наименьшим и кратно 305.
# Для найденных значений x и y вычислите частное от деления значения арифметического выражения на 305
# и укажите его в ответе в десятичной системе счисления.
# Основание системы счисления в ответе указывать не нужно.
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
for x in alphabet[:11]:
    for y in alphabet[:11]:
        A = int(f'{x}341{y}', 11)
        B = int(f'56{x}1{y}', 19)
        if (A + B) % 305 == 0:
            print((A + B) // 305)
'''
# Ответ: 2778




# endregion Урок: ******************************************************************


# todo: Артур = [2.1. 6.1]
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:
