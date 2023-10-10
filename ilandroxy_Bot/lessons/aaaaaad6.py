
# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Циклы while и for: Цикл - повторяющееся действие

# Цикл for: "Повтори n раз", "Пробеги от a до b"
'''
# Работа цикла for с использованием функции range()
for x in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(x, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for x in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(x, end=' ')  # 2 3 4 5 6 7 8 9
print()

for x in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(x, end=' ')  # 2 4 6 8
print()

for x in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(x, end=' ')  # 2 4 6 8 10
print()

for x in range(10, 0, -1):
    print(x, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

s = 'abcde'

print(M[0], M[-1])   # взятие крайнего левого и крайнего правого элементов
print(s[0], s[-1])  # a e

for i in range(0, len(M)):  # len(M) - это функция возвращающая длину последовательности (кол-во элементов)
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
    # Получаем элементы списка через индексы
print()

for i in range(len(s)):
    print(s[i], end=' ')  # a b c d e
print()

# В чем разница использования индексов через функцию range для списков и строк?
# Ответ: в списках через индексы можно менять элементы, а в строках/кортежах нельзя

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']


# Можно обращаться (брать) к элементам последовательности напрямую

M = ['a', 'b', 'c', 'd', 'e']
s = 'abcde'

for x in M:
    print(x, end=' ')  # a b c d e
print()

import random
L = [random.randint(1, 100) for _ in range(10)]  # [90, 17, 72, 79, 68, 52, 51, 17, 17, 24]
print(L)

# Задача: взять все четные элементы списка
for x in L:
    if x % 2 == 0:
        print(x, end=' ')
print()
'''


# Цикл while: "Повторяй действие ПОКА условие выполняется", "Бесконечный цикл"
'''
for x in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(x, end=' ')  # 2 4 6 8 10 
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10 
    i += 2
print()
'''


# Перевод из 10-ной в 2-ную систему счисления
'''
x = 8
M = []
while x > 0:
    M.append(x % 2)  # метод списков, который добавляет новый элемент в конец списка
    x //= 2
M.reverse()  # это метод списков, разворачивающий все элементы в обратном порядке
print(M)
'''

# Перевод из 10-ной в n-ную систему счисления
'''
x = int(input())
n = int(input())
M = []
while x > 0:
    M.append(x % n)  # метод списков, который добавляет новый элемент в конец списка
    x //= n
M.reverse()  # это метод списков, разворачивающий все элементы в обратном порядке
print(M)
'''

# Перевод из 10-ной в n-ную через строки
'''
import string as st
alphabet1 = st.digits + st.ascii_uppercase
print(alphabet1)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

alphabet2 = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

x = int(input())
n = int(input())
s = ''
while x > 0:
    s += alphabet1[x % n]
    x //= n
s = s[::-1]  # срез элементов строки в обратном порядке
print(s)
'''


# break и continue
'''
for x in range(100):
    if x == 50:
        break
    if x % 2 != 0:
        continue
    print(x)
'''

# Бесконечные циклы
'''
k = 1
while True:
    k += 1
    print(k)
'''


# программа для проверки пароля
'''
import random
import time
pas = 'qwerty'
count = 0
password = input('Введите пароль для проверки: ')
while True:
    if pas == password:
        print('Welcome!')
        break
    password = input('Пароль неверный, попробуйте снова: ')
    count += 1
    if count == 2:
        print('Подозрительная попытка входа, пройдите проверку на робота, решив пример: ')
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        x = int(input(f'{a} + {b} = '))
        if x == a + b:
            count = 0
            print('Проверка пройдена успешно!')
        else:
            print('Проверка на робота не пройдена, повторите через 5 минут: ')
            time.sleep(5*60)
'''


'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
while True:
    case = input('\n\ncase 1: Перевод из 10-ной в n-ную: \n'
                 'case 2: \n'
                 'case 3: \n'
                 'case 0: exit \n')

    if case == '1':
        x = int(input('Введите 10-ное число для перевода: '))
        n = int(input('Введите систему счисления в которую будем переводить: '))
        s = ''
        while x > 0:
            s += alphabet[x % n]
            x //= n
        s = s[::-1]  # срез элементов строки в обратном порядке
        print(f'Результат перевода: {s}')

    elif case == '2':
        pass

    elif case == '3':
        pass

    elif case == '0':
        break
'''
# endregion Урок: ******************************************************************


# todo: Лера = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:
