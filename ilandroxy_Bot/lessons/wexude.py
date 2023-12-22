# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Цикл - это некоторое повторяющееся действие

# Циклы for и while

# Цикл for отвечает на запрос: "повтори n раз", "пробеги от А до В"
'''
s = 'Hello'
for i in range(5):  # "повтори 5 раз"
    print(s)
    # Hello
    # Hello
    # Hello
    # Hello
    # Hello


for i in range(2, 10):  # "пробеги от 2 до 10-1"
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
'''

# range - диапазон
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()  # '\n' - переход на новую строку

for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()
'''

# Форики идеально подходят для итерируемых объектов (последовательности: lsit(), set(), str(), tuple()

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']   # len(M) - длина списка M (кол-во элементов в нем)

'''
# Такой подход удобен, если нам нужно пробежать все элементы последовательности с каким-то условием
for x in M:   # Мы напрямую пробегаем каждый элемент списка М
    print(x, end=' ')  # a b c d e
print()

for x in M:   # Мы напрямую пробегаем каждый элемент списка М
    if x in 'ae':  # Тут добавили условие
        print(x, end=' ')  # a e
print()
'''

# Такой подход удобен при работе именно с списками, так как через индексы мы можем изменять элементы списка
'''
for i in range(len(M)):   # Мы напрямую пробегаем каждый элемент списка М
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):   # Мы напрямую пробегаем каждый элемент списка М
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']

'''

# Цикл while отвечает на запрос: "Пока условие верно - выполняй действие", "Бесконечный цикл"

'''
i = 0
while i < 10:  # "Пока условие верно - выполняй действие"
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
    i += 1
print('КОНЕЦ')
'''

'''
for i in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

i = 2
while i < 10+1:
    print(i, end=' ')  # 2 4 6 8 10
    i += 2  # i = i + 2
'''

# Перевод из 10-ной в n-ную систему счисления
'''
x = 8
n = 2
M = []
while x > 0:
    M.append(x % n)  # .append() - добавить новый элемент в конец списка
    x //= n  # x = x // n
M.reverse()  # ю.reverse() - развернуть элементы списка list()
print(M)  # [1, 0, 0, 0]
'''

'''
k = 0
while True:
    k += 1
    print(k)
'''
# N = множество натуральных чисел бесконечно
# Z = множество целых чисел бесконечно
# А каки чисел больше? Какое множество больше?

# Z > N: натуральные числа лежат в целых

# N: {1, 2, 3, 4, ..., +inf)
# Z: {-inf,..., -2, -1, 0, 1, 2, ..., +inf}

'''
import time

snake = '****'
while True:
    time.sleep(1)
    snake = ' ' + snake
    print(snake)
'''

'''
import time

snake = '****'
for i in range(10):
    snake = ' ' + snake
    print(snake, end='', flush=True)
    time.sleep(.3)
print()
'''


'''
import random
import time

pas = 'qwerty'
password = input('Введите пароль: ')
count = 0
while True:
    if pas == password:
        break
    password = input('Пароль неверный, попробуйте снова: ')
    count += 1
    if count == 3:
        print('Подозрительная попытка входа, решите пример!')
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        x = int(input(f'{a} + {b} = '))
        if x == a + b:
            count = 0
            print('Проверка на робота пройдена успешно!')
        else:
            print('Повторите попытку через 5 минут.')
            time.sleep(5*60)

print('Welcome!')
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
        n = int(input('Введите n-ную систему счисления: '))
        s = input(f'Введите число в {n}-ной системе: ')
        k = int(input('Введите k-ую систему счисления: '))

        r = int(s, n)

        s = ''
        while r > 0:
            s += alphabet[r % k]
            r //= k
        s = s[::-1]
        print(f'Результат перевода: {s}')

    elif case == '0':
        print('Конец программы.')
        break
'''

# endregion Урок: ******************************************************************

# Лика = []
# КЕГЭ  = []
# на следующем уроке:
