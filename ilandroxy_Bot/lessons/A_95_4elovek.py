
# region Домашка: ***************************************************************


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************

# Циклы for и while
# Цикл - это действие, которое повторяется n раз или пока выполняется поставленное условие

# Цикл for: "повтори n-раз", "пробеги от 2 до 10"
'''
for i in range(10):  # [0, 10)  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # [2, 10)  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')   # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # [2, 10)  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')   # 2 4 6 8
print()

for i in range(10, 0, -1):  # [10, 0)  # range(START=10, STOP=0+1, STEP=-1)
    print(i, end=' ')   # 10 9 8 7 6 5 4 3 2 1
print()
'''

# Берем элементы списков/строк через индексы
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

# i  01234
s = 'abcde'

for i in range(len(M)):  # len(M) - функция возвращает длину списка M (кол-во элементов внутри).
    print(i, end=' ')  # 0 1 2 3 4
print()

for i in range(len(M)):
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(s)):
    print(s[i], end=' ')  # a b c d e
print()
'''

# Меняем элементы списка через индексы
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Берем элементы списков/строк напрямую (без индексов)
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

# Вложенные (каскадные) циклы
'''
s = 'xyz'
for a in s:
    for b in s:
        print(a, b)
'''
# x x
# x y
# x z
# y x
# y y
# y z
# z x
# z y
# z z

# Цикл while - цикл с условием, то есть работать будет "пока выполняется условие", бесконечный цикл
'''
for i in range(2, 10+1, 2):  # [2, 10)  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')   # 2 4 6 8 10 
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10 
    i += 2
'''

# Сделать перевод из 10-ной в 2-ную систему счисления
'''
x = int(input('Число (10-ное) для перевода: '))
n = int(input('Система счисления: '))

M = []
while x > 0:
    M.append(x % n)
    x //= n
M.reverse()
print(M)
'''

'''
x = int(input('Число (10-ное) для перевода: '))
n = int(input('Система счисления: '))

s = ''
while x > 0:
    s += str(x % n)
    x //= n
s = s[::-1]  # срез в обратную сторону
print(s)
print(int(s, n))
'''

'''
k = 1
while True:
    k += 1
    print(k)
    if k == 1000000:
        break
'''

'''
import string
ALPHABET = string.digits + string.ascii_uppercase
print(ALPHABET)

ALPHABET2 = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(ALPHABET2)

while True:
    case = input('\ncase 1: Перевод из 10-ной в n-ную систему счисления. \n'
                 'case 2: Перевод из n-ной в 10-ную систему счисления. \n'
                 'case 0: exit \n')

    if case == '1':
        x = int(input('Число (10-ное) для перевода: '))
        n = int(input('Система счисления: '))

        s = ''
        while x > 0:
            s += ALPHABET[x % n]
            x //= n
        s = s[::-1]
        print(f'Результат перевода: {s}')

    elif case == '2':
        s = input('Число (n-ное) для перевода: ')
        n = int(input('Система счисления (n-ная): '))

        print(f'Результат перевода: {int(s, n)}')
        
    elif case == '3':
        pass  # Перевод из n-ной в k-тую

    elif case == '0':
        break
'''
# endregion Урок: ***************************************************************


# todo: Сева = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:
