# region Домашка:

# 1 номер
'''
email = input()
if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')
'''

'''
M = [1, 2, 3 ,4, 3, 2,1, 2 ,3 ,4,4,2,21,21,2, 2,3]
A = []
for x in M:
    if x not in A:
        A.append(x)
print(A)
'''


#2 номер
"""
x = int(input())
if x == 2:
    print("28")
else:
    print(30 + (x + x // 8) % 2)
"""


#3 номер
"""
x = int(input())
if -30 < x <= -2 or 7 < x <= 25:
    print ('Принадлежит')
else:
    print('Не принадлежит')
"""

# endregion Домашка:



# region Урок:

# Теория по циклам
# Ключевые слова: while, for, range, len, break, continue, flag

# for - цикл для пробежки по спискам или цикл "повтори n раз"
'''
for i in range(5):  # [0, 5)    range(START = 0, STOP, STEP = 1)
    print(i, end=' ')
print()

for i in range(1, 10):  # [1, 10)  range(START, STOP, STEP = 1)
    print(i, end=' ')
print()

for i in range(0, 10, 2):  # [1, 10)  range(START, STOP, STEP)
    print(i, end=' ')
print()

for i in range(10, 0, -1):  # поменяли шаг на -1, чтобы пройти по убыванию
    print(i, end=' ')
print()

M = [4, 5, 6, 7, 8, 9]
# i  0  1  2  3  4  5

print(len(M))  # len() это функция возвращающая длину списка (то есть кол-во элементов в нем)
for i in range(0, len(M)):  # [0, 6)  # вывели элементы нашего списка через индексы
    print(M[i], end=' ')
print()

for x in M:  # вывели элементы нашего списка напрямую - то есть Х принимал значение элементов списка
    print(x, end=' ')
print()

for i in range(0, len(M)):  # [0, 6)  # вывели элементы нашего списка через индексы
    M[i] = M[i] ** 2
print(M)
'''



# while - цикл с условием (если условие истинно, то выполняем действие, если же ложно - выходим из цикла)
'''
for i in range(0, 10+1, 2):
    print(i, end=' ')
print()

i = 0
while i <= 10:  # плохой бесконечный цикл
    print(i, end=' ')
    i += 2


# Сумма цифр числа
x = int(input())
summ = 0
while x > 0:
    summ += x % 10
    x //= 10
    print(x)
print(summ)

# Факториал числа
x = int(input())
f = 1
for i in range(1, x+1):
    f *= i
print(f)
'''

# break - команда которая прерывает цикл
# continue - прерывает итерацию цикла
'''
for i in range(1, 20):
    if i == 16:
        break
    if i % 2 != 0:
        continue
    print(i)
'''


# Тип 15 № 9320
'''
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# Для какого наименьшего натурального числа А формула
#
# ДЕЛ(x, А) → (ДЕЛ(x, 21) + ДЕЛ(x, 35))
#
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?

for A in range(1, 1000):
    flag = True
    for x in range(1,1000):
        if ((x % A == 0) <= ((x % 21 == 0) or (x % 35 == 0))) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break
'''
# Ответ: 21


# Бесконечный цикл
'''
k = 0
while True:
    k += 1
    print(k)
'''

import random

password = 'qwerty'
count = 0
while True:
    pas = input('Введите пароль: ')
    if pas == password:
        print('Welcome')
        break
    print('Пароль неверный, попробуйте снова')
    count += 1
    if count == 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(f'Пройдите проверку на капчу!\nРешите пример: {a} + {b} = ')
        x = int(input())
        if x == a + b:
            print('Пройдено успешно!')
            count = 0
            continue
        else:
            print('BAN')
            break

# endregion Урок:


# todo: Ислам = [], на следующем уроке: разбираем 2 номер ЕГЭ
