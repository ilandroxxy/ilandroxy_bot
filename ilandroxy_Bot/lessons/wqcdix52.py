# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Циклы while и for

# Цикл - это какое-то повторяющееся действие

# for цикл по типу: "повтори n раз", "пробеги от А до Б"

# Работа с циклом for через функцию range()
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

for x in range(2, 10+1, 2):  # range(START=2, STOP=10+1-1, STEP=2)
    print(x, end=' ')  # 2 4 6 8
print()


for x in range(10, 0, -1):  # range(START=10, STOP=0+1, STEP=-1)
    print(x, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()
'''

# А зачем этот range() нужен? Он нужен для того, чтобы брать элементы списка (и других) или менять элементы списка
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(M[0], M[-1])  # a e - взяли первый и последний элементы

s = 'abcde'
print(s[0], s[-1])  # a e - взяли первый и последний элементы


for i in range(len(M)):  # len(M) - это длина списка. то есть кол-во его элементов
    # print(i, end=' ')   # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(s)):  # len(M) - это длина списка. то есть кол-во его элементов
    # print(i, end=' ')   # 0 1 2 3 4
    print(s[i], end=' ')  # a b c d e
print()


# В списках можно менять значения элементов через индексы
for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Можно брать элементы списков напрямую из коллекции (последовательности)
'''
M = ['a', 'b', 'c', 'd', 'e']
s = 'abcde'

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in s:
    print(x, end=' ')  # a b c d e
print()

L = [234, 34, 564, 23, 45, 23, 12, 343, 23, 543]

for x in L:  # возьмите только четные элементы
    if x % 2 == 0:
        print(x, end=' ')   # 234 34 564 12
print()

for x in L:  # возьмите все трехзначные числа
    if len(str(x)) == 3:
        print(x, end=' ')   # 234 564 343 543 
print()
'''


# while цикл по типу: "делай ПОКА условие выполняется", "бесконечный цикл"
'''
for x in range(2, 10+1, 2):  # range(START=2, STOP=10+1-1, STEP=2)
    print(x, end=' ')  # 2 4 6 8
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
    i += 2  # i = i + 1 и по аналогии: -= /= //= **= *= %=
print()
'''

'''
# Перевод из 10-ной в 2-ную (n-ную систему счисления)
x = 8
M = []
while x > 0:
    M.append(x % 2)
    x //= 2
M.reverse()
print(M)

print(int('1000', 2))   # 8

# Аналогичная задача, но хотим получить в результате строку

x = 8
s = ''
while x > 0:
    s += str(x % 2)
    x //= 2
s = s[::-1]  # срез в обратном порядке
print(s)
'''

# Универсальная программа для перевода из 10-ной в n-ную
'''
import string
alphabet1 = string.digits + string.ascii_uppercase
print(alphabet1)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

alphabet2 = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

x = int(input('Введите 10-ное число: '))
n = int(input('Введите n-ную систему счисления: '))
s = ''
while x > 0:
    s += alphabet1[x % n]
    x //= n
s = s[::-1]
print(f'Результат перевода: {s}')
'''

# Бесконечный цикл
'''
k = 1
while True:
    print(k)
    k += 1
'''

'''
alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
while True:
    case = input('\n\n'
                 'case 1: Перевод из 10-ной в n-ную систему счисления \n'
                 'case 2: Перевод из n-ной в 10-ную систему счисления \n'
                 'case 3: Перевод из n-ной в k-ную систему счисления \n'
                 'case 0: exit \n')

    if case == '1':
        x = int(input('Введите 10-ное число: '))
        n = int(input('Введите n-ную систему счисления: '))
        s = ''
        while x > 0:
            s += alphabet[x % n]
            x //= n
        s = s[::-1]
        print(f'Результат перевода: {s}')

    elif case == '2':
        n = int(input('Введите n-ную систему счисления: '))
        s = input(f'Введите число {n}-ной системе счисления: ')
        x = int(s, n)
        print(f'Результат перевода числа {s} из {n}-ной системы счисления: {x}')

    elif case == '3':
        pass

    elif case == '0':
        break
'''

import random
import time

Err = ['Не верно', 'Повторите попытку', 'Ошибочно',
       'Попробуйте еще раз', 'Неправильно',
       'Повторите пожалуйста', 'Неверный ответ',
       'Попытайтесь снова', 'Неудачно', 'Пробуйте снова']


# Маленький пример скрипта на проверку пароля от пользователя
'''
pas = 'qwerty'
password = input('Введите пароль для входа: ')
count = 1
while True:
    if pas == password:
        print('Welcome!')
        break
    password = input(f'{random.choice(Err)}: ')
    count += 1
    if count == 3:
        print('Слишком много попыток, пройдите проверку на робота решив пример: ')
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        x = int(input(f'{a} + {b} = '))
        if x == a + b:
            count = 0
            print('Проверка успешно пройдена! ')
        else:
            print('Подозрительная активность, попробуйте через 5 минут: ')
            time.sleep(5*60)

print('Тут программа')
'''

# endregion Урок: ******************************************************************


# todo: Артур = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:
