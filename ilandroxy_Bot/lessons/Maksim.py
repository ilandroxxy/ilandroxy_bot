
# region Домашка: ************************************************************

# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.
#
# Sample Input: 123

# Sample Output:
# Сумма цифр = 6
# Произведение цифр = 6
'''
num = int(input())  # 823
a = num // 100
b = (num % 100) // 10
c = num % 10
print(f'Сумма цифр = {a+b+c}')
print(f'Произведение цифр = {a*b*c}')
'''


# Напишите программу, которая принимает год от пользователя
# и проверяет, является ли он високосным.
#
# Если является, программа должна вывести "Да", или "Нет",
# если не является високосным.
#
# Примечание. Год является високосным, если его номер кратен 4, но не кратен 100,
# или если он кратен 400.

# != не равно
# == равно
'''
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('Yes')
else:
    print('No')


year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('Да')
    exit()
print('Нет')
'''

# endregion Домашка: ************************************************************

# region Урок: ************************************************************

# Теория циклов while и for:
# Цикл - это некоторое повторяющееся действие

# for - цикл повтори n раз
'''
for x in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(x, end=' ')  # 0 1 2 3 4 5 6 7 8 9 
print()

for x in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(x, end=' ')  # 2 3 4 5 6 7 8 9 
print()

for x in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(x, end=' ')  # 2 4 6 8 
print()

for x in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(x, end=' ')  # 2 4 6 8 10 
print()

for x in range(10, 0, -1):  # range(START=10, STOP=0-1, STEP=-1)
    print(x, end=' ')  # 10 9 8 7 6 5 4 3 2 1 
print()
'''

# Перебираем все элементы списка (строки) через их индексы
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

# i  01234
s = 'abcde'

for i in range(len(M)):  # получилось перебрать все индексы списк (строки)
    print(i, end=' ')  # 0 1 2 3 4
print()

for i in range(len(M)):
    print(M[i], end=' ')  # a b c d e
print()


# Перебираем все элементы списка (строки) на прямую

for x in M:
    print(x, end=' ')
print()

for x in s:
    print(x, end=' ')
print()
'''


# while - цикл с условием (пока)
'''
for x in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(x, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2
print()
'''

# Бесконечный цикл
'''
k = 1
while True:
    k += 1
    print(k)
'''

# Перевод из 10-ной в n-ную систему счисления
'''
x = int(input('Введите 10-ное число: '))
n = int(input('Введите систему счисления: '))
M = []
while x > 0:
    M.append(x % n)
    x //= n
M.reverse()
print(M)
'''

'''
x = int(input('Введите 10-ное число: '))
n = int(input('Введите систему счисления: '))
s = ''
while x > 0:
    s += str(x % n)
    x //= n
s = s[::-1]
print(s, type(s))

print(f'Обратный перевод: {int(s, n)}')
'''


ALPHABET = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
while True:
    case = input('case 1: Перевод из 10-ной в n-ную систему счисления.\n'
                 'case 2: Перевод из n-ной в 10-ную систему счисления.\n'
                 'case 0: exit\n')
    if case == '1':
        x = int(input('Введите 10-ное число: '))
        n = int(input('Введите систему счисления: '))
        s = ''
        while x > 0:
            s += ALPHABET[x % n]
            x //= n
        s = s[::-1]
        print(f'Результат перевода: {s}\n\n')

    elif case == '2':
        s = input('Введите число в n-ной системе счисления: ')
        n = int(input('Введите n-ную систему счисления: '))
        print(f'Результат перевода: {int(s, n)}\n\n')

    elif case == '0':
        break




# endregion Урок: ************************************************************


# todo: Максим = []
# на прошлом уроке:
# на следующем уроке: Поговорить про условные операторы и подключение библиотек к проекту
