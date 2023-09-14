
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Циклы while и for
# Циклы - какое-то повторяющееся действие

# Циклы for - это цикл "повтори n раз"
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

for x in range(10, 0, -1):  # range(START=10, STOP=0+1, STEP=-1)
    print(x, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()
'''


# Пробежать список (строку) используя функцию range() и len()
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# i  01234
s = 'abcde'

for i in range(len(M)):   # len() - это длина коллекции (то есть кол-во ее элементов)
    print(i, end=' ')  # 0 1 2 3 4
print()

for i in range(len(M)):
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(s)):
    print(s[i], end=' ')  # a b c d e
print()

# Если перед нами стоит задача, поменять все элементы списка (или часть из них),
# то это придется делать через цикл for in range()
for i in range(len(M)):
    if i % 2 == 0:  # если позиция четная, то удваиваем 
        M[i] = M[i] * 2
    elif i % 2 != 0:  # если нечетная, то утраиваем
        M[i] = M[i] * 3
print(M)  # ['aa', 'bbb', 'cc', 'ddd', 'ee']
print(*M)  # aa bbb cc ddd ee  -  * это оператор раскрытия
'''

# Перебираем элементы коллекции, напрямую
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# i  01234
s = 'abcde'
    
for x in M:
    print(x, end=' ')  # a b c d e 
print()

for x in s:
    print(x, end=' ')  # a b c d e 
print()
'''

# Цикл while - это цикл с условием "пока выполняется поставленное условие - делай"
'''
for x in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(x, end=' ')  # 2 4 6 8 10
print()

x = 2
while x <= 10: 
    print(x, end=' ')  # # 2 4 6 8 10
    x += 2
'''

# Бесконечный цикл
'''
k = 1
while True:
    print(k)
    k += 1
'''


# Перевод из 10-ной в n-ную систему счисления
'''
x = int(input('Введите 10-ное число: '))
n = int(input('Введите n-ную систему счисления: '))
M = []
while x > 0:
    M.append(x % n)
    x //= n  # x = x // n
M.reverse()  # M = M[::-1]
print(*M)
'''

'''
print(int('1000', 2))  # 8

x = int(input('Введите 10-ное число: '))
n = int(input('Введите n-ную систему счисления: '))
s = ''
while x > 0:
    s += str(x % n)
    x //= n  # x = x // n
s = s[::-1]
print(s)

print(int(s, 2))  # 8
'''


# Мини калькулятор для перевода в разные системы счисления

ALPHABET = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

while True:
    case = input('\ncase 1: Перевод из 10-ной в n-ную систему. \n'
                 'case 2: Перевод из n-ной в 10-ную систему. \n'
                 'case 0: exit\n')

    if case == '1':
        x = int(input('Введите 10-ное число: '))
        n = int(input('Введите n-ную систему счисления: '))
        s = ''
        while x > 0:
            s += ALPHABET[x % n]
            x //= n
        s = s[::-1]
        print(f'Результат перевода: {s}')

    elif case == '2':
        s = input('Введите n-ное число: ')
        n = int(input('Введите n-ную систему счисления: '))
        print(f'Результат перевода: {int(s, n)}')

    elif case == '0':
        break


# endregion Урок: ******************************************************************


# todo: Марк = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:
