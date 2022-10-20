
# Домашка
# Задание №1 "Обратное число"
"""
x = int(input('x: '))
if x == 0:
    print('Обратного числа не существует')
else:
    print(1 / x)
"""
# Задание №2 "Високосный год"
"""
x = int(input('x: '))
if x % 4 == 0 and (not (x % 100 == 0)):  # if x % 4 == 0 and x % 100 != 0:
    print('YES')
elif x % 400 == 0:
    print('YES')
else:
    print('NO')
"""
# Задание №3 "Корректный email"
"""
x = input('x: ')  # функция input() - сама по себе принимает строку
if ('@' and '.') in x:  # if '@' in x and '.' in x:
    print('YES')
else:
    print('NO')
"""


# Тип 15 № 33187
"""
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
#
# Для какого наибольшего натурального числа А формула
#
# ДЕЛ(90, A) ∧ (¬ДЕЛ(x, А) → (ДЕЛ(x, 15) → ¬ДЕЛ(x, 20)))
#
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?

for A in range(100, -1, -1):
    flag = True
    for x in range(1, 1000):
        if ( (90 % A == 0) and ((not(x % A == 0)) <= ((x % 15 == 0) <= (x % 20 != 0))) ) == False:
            flag = False
            break
    if flag == True:
        print(A)
        break
"""
# Ответ: 30


# Тип 14 № 28552
"""
# Значение выражения 216**6 + 216**4 + 36**6 − 6**14 − 24 записали в системе счисления с основанием 6.
# Сколько различных цифр содержит эта запись?
#
# Пример. Запись 122233_7 содержит три различные цифры: 1, 2 и 3.

x = 216**6 + 216**4 + 36**6 - 6**14 - 24
M = []
while x > 0:
    M.append(x % 6)
    x //= 6
M.reverse()
print(M)

A = []
for x in M:
    if x not in A:
        A.append(x)
print(A, len(A))

B = set(M)
print(B, len(B))
"""


# Циклы
# for, while, range, break, continue, flag

# циклы for и функция range
"""
for i in range(5):  # цикл for бежит по переменной i в диапазоне range(5) от нуля до 5 не включительно [0, 5)
    print(i, end=' ')  # range(0, STOP)
print()

for i in range(2, 10):  # [2, 10)   range(START, STOP)
    print(i, end=' ')
print()

for i in range(2, 10, 2):  # [2, 10) с шагом 2   range(START, STOP, STEP)
    print(i, end=' ')
print()

M = [1, 2, 3, 4]
# i  0  1  2  3

for x in M:
    print(x, end=' ')  # переменная х принимает значение элементов списка на себя
print()

for i in range(0, len(M)):  # мы бежим по индексному диапазону элементов списка
    print(M[i], end=' ')
print()

for i in range(0, len(M)):  # если мы знаем индексы элементов, то мы можем их менять
    M[i] = M[i] ** 2
print(M)
"""


# Цикл while - цикл с условием, выполняет свое тело только при истинном условии
'''
for i in range(2, 10+1, 2):  # [2, 10) с шагом 2   range(START, STOP, STEP)
    print(i, end=' ')
print()

i = 2  # START
while i <= 10:  # делать пока истинно # STOP
    print(i, end=' ')
    i += 2  # STEP
print()

# Переведем x в двоичную систему
x = int(input('x: '))
M = []
while x > 0:
    M.append(x % 2)
    x //= 2
M.reverse()
print(M)
'''

# break - прерывает исполнение цикла (выход из цикла в котором находится)
# continue - прерывает итерацию цикла
"""
for i in range(1, 20):
    if i == 16:
        break
    if i % 2 != 0:
        continue
    print(i, end=' ')
print()
print('Конец программы')
"""


# Бесконечный цикл
'''
count = 0
while True:
    print(count)
    count += 1
'''
import random

pas = 'qwerty'
count = 0
while True:
    password = input('Введите пароль: ')
    if pas == password:
        print('Welcome')
        break
    print('Пароль неверный! ')
    count += 1
    if count == 3:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        print(f'Пройдите проверку на робота:\nРешите пример: {a} + {b} = ')
        x = int(input())
        if x == a + b:
            print('Проверка пройдена')
            count = 0
            continue
        else:
            print('Бан')
            break






