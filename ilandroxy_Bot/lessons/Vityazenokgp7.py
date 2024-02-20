# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Циклы в Пайтон

# Цикл for: Отвечает запросам: "повтори n раз", "пробеги от А до В", бонусом работа с последовательностями (коллекциями)


# Работа с циклом for через функцию range()

# Повтори 5 раз:
'''
for _ in range(5):
    print('hello, world')
'''

'''
for i in range(10):   # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):   # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):   # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(2, 10+1, 2):   # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0, -1):   # range(START=10, STOP=1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()
'''

# Тип 5 №47002
# Алгоритм получает на вход натуральное число N > 1 и строит по нему новое число R следующим образом:
# 1. Строится двоичная запись числа N.
# 2. Вычисляется количество единиц, стоящих на чётных местах
# в двоичной записи числа N без ведущих нулей, и количество нулей, стоящих на нечётных местах.
# Места отсчитываются слева направо (от старших разрядов к младшим, начиная с единицы).
# 3. Результатом работы алгоритма становится модуль разности полученных двух чисел.
# При каком наименьшем N в результате работы алгоритма получится R = 4?
'''
for n in range(2, 1000):
    s = bin(n)[2:]
    cnt1 = s[1::2].count('1')
    cnt0 = s[0::2].count('0')
    r = abs(cnt0 - cnt1)
    if r == 4:
        print(n)  # наименьшее n подходящее по условию
        break

for n in range(1000, 2, -1):
    s = bin(n)[2:]
    cnt1 = s[1::2].count('1')
    cnt0 = s[0::2].count('0')
    r = abs(cnt0 - cnt1)
    if r == 4:
        print(n)  # наибольшее n подходящее по условию
        break
'''

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']  # list()
'''
# Через индексы мы можем получать элементы списка
for i in range(len(M)):  # len() - возвращает длину списка (кол-во элементов в нем)
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

# Через индексы мы можем получать пары последовательных элементов списка (17 номер егэ)
for i in range(len(M)-1):
    x, y = M[i], M[i+1]
    print(f'{x}{y}', end=' ')  # ab bc cd de
print()

# Через индексы мы можем изменять элементы списка
for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

'''
# То есть через цикл for мы можем пробежать напрямую все элементы колелкции/последовательности
for x in M:
    print(x, end=' ')  # a b c d e
print()

# Такой способ удобен для проверки элементов последовательности

A = [23, 234, 123, 12, 124, 2354, 231]
for x in A:
    if x % 2 == 0:
        print(x, end=' ')  # 234 12 124 2354
print()


A = [23, 234, 123, 12, 124, 2354, 123]
for i in range(len(A)):
    if A[i] % 2 == 0:
        print(A[i], end=' ')  # 234 12 124 2354
print()
'''

# Генераторы списков:
'''
chet = [x for x in A if x % 2 == 0]
nechet = [x for x in A if x % 2 != 0]
copied = [x for x in A if A.count(x) > 1]
not_copied = [x for x in A if A.count(x) == 1]
print(A)
print(chet, nechet)
print(copied, not_copied)
'''


# Цикл while: Отвечает запросам: "пока условие верно - делаем действие", "бесконечные циклы"
'''
for i in range(2, 10+1, 2):   # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()
'''

# Перевод в n-ую систему счисления из 10-ой
'''
num = 8
n = 2  # система счисления
s = ''
while num > 0:
    s += str(num % n)
    num //= n
s = s[::-1]  # срез в обратном порядке
print(s)  # 1000

num = 8
n = 2  # система счисления
s = ''
while num > 0:
    s = str(num % n) + s
    num //= n
print(s)  # 1000
'''

# Универсальная программа перевода в n-ую систему счисления из 10-ой:
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
num = 123213214231412
n = 16  # система счисления
s = ''
while num > 0:
    s = alphabet[num % n] + s
    num //= n
print(s)  # 700FCFDDAB74

# В Питоне есть встроенная функция перевода из n-ой в 10-ную
print(int('700FCFDDAB74', 16))  # 123213214231412
# ValueError: int() base must be >= 2 and <= 36, or 0
'''


alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
while True:
    case = input('\n\ncase 1:  Перевод из 10-ой в n-ую систему.\n'
                 'case 2:  Перевод из n-ой в 10-ую систему.\n'
                 'case 3:  Перевод из n-ой в k-ую систему.\n'
                 'case 0: exit\n')

    if case == '1':
        num = int(input('Введите 10-ое число: '))
        old_num = num
        n = int(input('Введите n-ую систему счисления: '))
        s = ''
        while num > 0:
            s = alphabet[num % n] + s
            num //= n
        print(f'Результат перевода числа {old_num} в {n}-ую систему: {s}')

    elif case == '2':
        n = int(input('Введите n-ую систему счисления: '))
        num = input(f'Введите {n}-ое число: ')

        r = int(num, n)
        print(f'Результат перевода числа {num} из {n}-ой системы в 10-ую: {r}')

    elif case == '3':
        pass

    elif case == '0':
        break

# endregion Урок: **********************************************************


# Михаил = []
# КЕГЭ  = []
# на следующем уроке:
