

# Циклы
# Ключевые слова: while, for, range, break, continue

# for - повтори n раз, пробеги элементы списка/строки, пробежать диапазон (отрезок)



"""
for i in range(10+1):  # функция range() - строит диапазон [0, 10)
    print(i, end=' ')  # end - убирает этот переходи и заменяет символом в " "
print()  # в функции print() есть переход на новую строку /n

for i in range(2, 10+1):  # range() с двумя аргументами - [START, STOP)
    print(i, end=' ')
print()

for i in range(0, 10+1, 2):  # range() с тремя аргументами - START, STOP, STEP
    print(i, end=' ')
print()

for i in range(10, -1, -1):  # пример когда полезно изменить стандартный шаг +1 на шаг -1
    print(i, end=' ')
print()

M = []
for i in range(0, 100+1, 2):  # пример как можно получить список четных элементов из диапазона (отрезка)
    M.append(i)
print(M)
"""

"""
s = '4567834'
# i  0123456 у элементов строки/списка есть порядковые номера начиная с 0 - индексы
print(len(s))  # len() - длина строка (кол-во элементов в нем)
print(s[0], s[3], s[-1])  # элемент с индексом 0 - первый, элемент с индексом -1 - последний

# Форик пробегающий элементы строки по индексам
for i in range(0, len(s)):  # [0, 7) или [0, 6]
    print(s[i], end=' ')
print()

# Форик пробегающий строку напрямую через значение элементов
for x in s:
    print(x, end=' ')
print()


A = [4, 5, 6, 7, 8, 3, 4]
print(A)
for i in range(0, len(A)):
    A[i] = A[i] ** 2
print(A)
"""


# while - цикл с условием, то есть если выполняется условие, то заходим в тело цикла
# если условие не выполняется (False), цикл прерывается

"""
for i in range(0, 10+1, 2):  # START, STOP, STEP
    print(i, end=' ')
print()

i = 0  # START
while i <= 10:  # STOP
    print(i, end=' ')
    i += 2  # STEP
print()
"""

"""
x = int(input('x: '))  # 12345
summ = 0

while x > 0:
    summ += x % 10
    x //= 10
    print(f'x = {x}, summ = {summ}')
print('Итоговая сумма цифр: ', summ)
"""

# region Тип 14 № 38948
"""
# Значение выражения 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49 записали в системе счисления с основанием 16.
# Сколько разных цифр встречается в этой записи?
x = 4**36 + 3*4**20 + 4**15 + 2*4**7 + 49
print(x)
M = []
while x > 0:
    M.append(x % 16)  # сохраняем остаток от деления
    x //= 16  # делим целочисленно, чтобы двигать процесс
    # x = x // 16
M.reverse()
print(M)
M = set(M)
print(M, len(M))
"""
# Ответ: 5
# endregion Тип 14 № 38948

# break - прервать выполнение цикла
# continue - прервать итерацию цикла

"""
for i in range(0, 20):
    if i % 2 != 0:
        continue
    if i == 14:
        break
    print(i, end=' ')
"""

'''
x = int(input('x: '))
if -1 < x < 17:
    print('YES')
else:
    print('NO')
'''

# todo: flag

# Бесконечный цикл
'''
k = 0
while True:
    print(k)
    k += 1
'''

import random

password = 'qwerty'
count = 0
while True:
    pas = input('Введите пароль: ')
    if pas == password:
        print('welcome!')
        break
    print('Пароль неверный.')
    count += 1
    if count == 3:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        print(f'Пройдите проверку на робота\nРешите пример:\n{a} + {b} =')
        x = int(input())
        if x == a + b:
            print('Окей')
            count = 0
            continue
        else:
            print('Banned')
            break




