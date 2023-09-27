
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Цикл - какое-то действие повторяющееся n раз

# Цикл for: "цикл повтори n раз", "пробеги от a до b"
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=10+1-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0, -1):  # range(START=10, STOP=0+1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()
'''

# Обращение к элементам списка и строки через их индексы
'''
#  i  0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

# Получили все элементы списка
for i in range(len(M)):  # len(M) - функция len() выводит длину списка/строки/.. (то есть кол-во элементов)
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

# Изменили элементы списка через их индексы
for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
print(*M)  #  b cc ddd eeee

# индексы расположены аналогично
s = 'abcde'

# Получили все элементы строки
for i in range(len(s)):
    # print(i, end=' ')  # 0 1 2 3 4
    print(s[i], end=' ')  # a b c d e
print()
'''

# Обращение к элементам списка и строки напрямую через их значение
'''
#  i  0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

for x in M:
    print(x, end=' ')  # a b c d e
print()

s = 'abcde'

for x in s:
    print(x, end=' ')  # a b c d e
print()

L = [1, 342, 4, 324, 32, 432, 4, 32, 423, 123, 123, 12, 321, 321, 312, 23, 123, 12, 23, 123, 213, 13]
# 1. Выведите на экран все четные числа
# 2. Выведите список всех четных чисtл
R = []
for x in L:
    if x % 2 == 0:
        print(x, end=' ')  # 1. 342 4 324 32 432 4 32 12 312 12
        R.append(x)
print()
print(R)  # 2. [342, 4, 324, 32, 432, 4, 32, 12, 312, 12]
'''

# Цикл while: "цикл выполняет действие, ПОКА условие выполняется", "Бесконечный цикл"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=10+1-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
    i += 2  # i = i + 1
'''

# Задание: Перевести число 8 в 2-ную систему счисления
# Перевод в 2-ную систему счисления через списки
'''
x = 8
n = 2
M = []
while x > 0:
    M.append(x % n)
    x //= n
M.reverse()
print(M)

print(bin(8)[2:])  # есть встроенная функция перевода в 2-ную
'''

# Для замены больших чисел на буквы, нам нужен алфавит, рассмотрим два варианта:
'''
import string
ALPHABET1 = string.digits + string.ascii_uppercase  # 0123456789 + ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(ALPHABET1)  # '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ALPHABET2 = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(ALPHABET2)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# Перевод в n-ную систему счисления через строки
x = int(input('x: '))
n = int(input('n: '))
s = ''
while x > 0:
    s += ALPHABET1[x % n]
    x //= n
s = s[::-1]
print(s)
'''

# Бесконечный цикл
'''
k = 1
while True:
    k += 1
    print(k)
'''


# break и continue
'''
for x in range(0, 100+1):
    if x % 2 != 0:  # нечетное
        continue  # прерывает итерацию цикла, то есть его шаг
    if x == 50:
        break  # прерывает только тот цикл в котором сейчас находится
    print(x)
'''

ALPHABET = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
# Напишем маленький калькулятор систем счисления:
while True:
    case = input('\ncase 1: Перевод из 10-ной в n-ную систему счисления \n'
                 'case 2: Перевод из n-ной в 10-ную систему счисления \n'
                 'case 3: Перевод из k-ой в n-ную систему счисления \n'
                 'case 0: exit \n')
    if case == '1':
        x = int(input('Введите 10-ное число: '))
        x2 = x
        n = int(input('Ведите n-ную систему счисления: '))
        s = ''
        while x2 > 0:
            s += ALPHABET[x2 % n]
            x2 //= n
        s = s[::-1]
        print(f'Результат перевода числа {x} из 10-ной в {n}-ную систему: {s}')

    elif case == '2':
        n = int(input('Ведите n-ную систему счисления: '))
        s = input(f'Введите число в {n}-ной системе счисления: ')
        x = int(s, n)  # то это встроенная функция для перевода из n-ной системы счисления в 10-ную
        print(f'Результат перевода числа {s} из {n}-ной в 10-ную систему: {x}')

    elif case == '3':
        pass

    elif case == '0':
        break

# endregion Урок: ******************************************************************


# todo: Екатерина = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:
