
# region Домашка: ******************************************************************
'''
x = int(input())
if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
    print('Да')
else:
    print('Нет')
'''
# endregion Домашка: ******************************************************************


# region Урок: ********************************************************************

# Цикл - некоторое повторяющееся действие
# Циклы while и for

# Цикл for: "повтори n раз", "пробеги от a до b"
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')   # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')   # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')   # 2 4 6 8
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')   # 2 4 6 8 10
print()

for i in range(10, 0, -1):   # range(START=10, STOP=0+1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
'''

'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

for i in range(len(M)):
    print(M[i], end=' ')  # a b c d e
    # print(i, end=' ')  # 0 1 2 3 4
print()

for x in M:
    print(x, end=' ')  # a b c d e
print()

s = 'abcde'
for i in range(len(s)):
    print(s[i], end=' ')  # a b c d e
print()

for x in s:
    print(x, end=' ')  # a b c d e
print()

# Через индексы можно изменять элементы списков (только списков)*

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for i in range(len(M)):
    M[i] = M[i] * i
print(M)   # ['', 'b', 'cc', 'ddd', 'eeee']
'''

'''
import random
M = [random.randint(0, 100) for _ in range(10)]
print(M)
for x in M:
    if x % 2 == 0:   # выведем только четные элементы 
        print(x, end=' ')  # 64 88 50 48 58 56 66 
print()
'''

# Цикл while: "выполняй действие, ПОКА условие истинно", "Бесконечный цикл"
'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')   # 2 4 6 8 10
print()

i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
print()
'''

# Перевод из 10-ной в n-ную систему счисления
'''
x = int(input('x: '))
n = int(input('n: '))
M = []
while x > 0:
    M.append(x % n)
    x //= n
M.reverse()
print(M)
'''
'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
x = int(input('x: '))
n = int(input('n: '))
s = ''
while x > 0:
    s += alphabet[x % n]
    x //= n
s = s[::-1]  # развернули строку в обратном порядке
print(s)
print(int(s, n))  # функция int может переводить строку из разных систем счисления в 10-ную
'''

# Бесконечный цикл
'''
k = 1
while True:
    print(k)
    k += 1  # k = k + 1  
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
while True:
    case = input('\ncase 1: Перевод из 10-ной в n-ную систему счисления. \n'
                 'case 2: Перевод из n-ной в 10-ную систему счисления. \n'
                 'case 3: Перевод из n-ной в k-ную систему счисления. \n'
                 'case 0: exit \n\n')

    if case == '1':
        x = int(input('Введите 10-ное число: '))
        temp = x
        n = int(input('Введите n-ную систему счисления: '))
        s = ''
        while x > 0:
            s += alphabet[x % n]
            x //= n
        s = s[::-1]  # развернули строку в обратном порядке
        print(f'Результат перевода числа {temp} в {n}-ную систему счисления: {s}')

    elif case == '2':
        n = int(input('Введите n-ную систему счисления: '))
        s = input(f'Введите число в {n}-ной системе: ')
        x = int(s, n)
        print(f'Результат перевода числа {s} из {n}-ной системы: {x}')

    elif case == '3':
        pass

    elif case == '0':
        break
'''

# endregion Урок: ******************************************************************


# todo: Варя = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:
