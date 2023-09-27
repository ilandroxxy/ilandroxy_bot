
# region Домашка: ******************************************************************

# https://stepik.org/lesson/1051610/step/6?unit=1060696
'''
a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Равносторонний')
elif a == b or b == c or a == c:
    print('Равнобедренный')
else:
    print('Разносторонний')
'''
# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Цикл - какое-то повторяющееся действие, например "повтори n раз"


# Цикл for: "повтори n раз", "пробеги от a до b"

# Цикл for с использованием функции range()
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

# Возьмите все четные числа до 30 включительно
for x in range(0, 30+1, 2):
    print(x, end=' ')  # 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30
print()

# Возьмите все нечетные числа до 30 включительно
for x in range(1, 30+1, 2):
    print(x, end=' ')  # 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29
print()

for x in range(10, 0, -1):  # range(START=10, STOP=0+1, STEP=-1)
    print(x, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()
'''

'''
for _ in range(5):  # можно написать _ , если переменная нам не нужна
    print('Привет')
    
for i in range(5):  # можно использовать название переменной для нумерации
    print(f'{i+1}) Привет')
'''

# Через функцию range мы можем брать элементы списка и менять элементы списка
'''
#  i  0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

for i in range(len(M)):  # Функция len() - выводит длину списка/строки/кортежа.. (кол-во элементов)
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(-1, -len(M)-1, -1):
    # print(i, end=' ')  # -1 -2 -3 -4 -5
    print(M[i], end=' ')  # e d c b a 
print()

for i in range(len(M)):
    M[i] = M[i] * i  # ['', 'b', 'cc', 'ddd', 'eeee']
print(M)
'''

# Через функцию range мы можем брать элементы строк
'''
s = 'abcde'

for i in range(len(s)):
    print(s[i], end=' ')  # a b c d e
print()
'''

# Взаимодействие с элементами списка/строки/.. напрямую через их значение
'''
M = ['a', 'b', 'c', 'd', 'e']
s = 'abcde'

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in s:
    print(x, end=' ')  # a b c d e
print()

from random import randint
M = [randint(0, 100) for _ in range(50)]
# 1. Вывести на экран все четные элементы набора чисел
# 2. Вывести список со всеми четными элементами
R = []
for x in M:
    if x % 2 == 0:
        print(x, end=' ')  # 98 10 60 4 52 82 26 26 16 8 22 28 32 64 70 42 100 68 78 24 
        R.append(x)
print()
print(R)  # [70, 50, 62, 54, 54, 54, 24, 4, 66, 60, 96, 84, 80, 68, 74, 48, 46, 62, 18, 8, 84, 92, 32]
'''


# Цикл while: "повторяй, ПОКА условие выполняется", "Бесконечный цикл"
'''
for x in range(2, 10+1, 2):  # range(START=2, STOP=10+1-1, STEP=2)
    print(x, end=' ')  # 2 4 6 8 10 
print()

i = 2
while i <= 10:
    print(i, end=' ')  # 2 4 6 8 10 
    i += 2  # i = i + 1   # i -= 2, i //= 2, i **= 2
print()
'''


# Задание: Перевести число 8 в 2-ную систему счисления
'''
x = 8
n = 2
M = []
while x > 0:
    M.append(x % n)
    x //= n
M.reverse()
print(M)

print(bin(8)[2:])  # встроенная функция для перевода в 2-ную систему счисления
'''

# Для замены больших чисел на буквы, нам нужен алфавит, рассмотрим два варианта создания:
'''
import string
ALPHABET1 = string.digits + string.ascii_uppercase
print(ALPHABET1)  # 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ

ALPHABET2 = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
print(ALPHABET2)  # ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
print(len(ALPHABET2))  # 36
'''

# Перевод из 10-ной в n-ную систему счисления, но через СТРОКИ
'''
x = int(input('x: '))
n = int(input('n: '))
s = ''
while x > 0:
    s += ALPHABET2[x % n]
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

# Рассмотрим break и continue
'''
for x in range(0, 100+1):
    if x % 2 != 0:
        continue
    if x == 50:
        break
    print(x)
print('КОНЕЦ')
'''

# Напишем простой консольный калькулятор перевода в разные системы счисления
'''
ALPHABET = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
while True:

    case = input('\ncase 1: Перевод из 10-ной в n-ную систему счисления \n'
                 'case 2: Перевод из n-ной в 10-ную систему счисления \n'
                 'case 3: Перевод из k-ной в n-ную систему счисления \n'
                 'case 0: exit \n')

    if case == '1':
        x = int(input('Введем число в 10-ной системе: '))
        x2 = x
        n = int(input('Введем n-ную систему: '))
        s = ''
        while x2 > 0:
            s += ALPHABET[x2 % n]
            x2 //= n
        s = s[::-1]
        print(f'Результат перевода числа {x} в {n}-ную систему счисления: {s}')

    elif case == '2':
        n = int(input('Введите n-ную систему счисления: '))
        s = input(f'Введите число в {n}-ной системе счисления: ')
        x = int(s, n)
        print(f'Результат перевода числа {s} из {n}-ной системы счисления в 10-ную: {x}')

    elif case == '3':
        n = int(input('Введите n-ную систему счисления: '))
        s = input(f'Введите число в {n}-ной системе счисления: ')
        k = int(input('Введите k-ную систему счисления: '))
        x = int(s, n)
        x2 = x
        r = ''
        while x2 > 0:
            r += ALPHABET[x2 % k]
            x2 //= k
        r = r[::-1]
        print(f'Результат перевода числа {s} из {n}-ной системы счисления в {k}-ную: {r}')

    elif case == '0':
        break
'''

# Проверка пароля пользователя
'''
import random
import time

pas = 'qwerty'
password = input('Введите пароль: \n')
count = 0
while True:
    if pas == password:
        print('Welcome')
        break
    count += 1
    if count == 3:
        print('Подозрительные действия, пройдите проверку на робота!')
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        x = int(input(f'{a} + {b} == '))
        if x == a + b:
            count = 0
            print('Проверка на работа пройдена успешно! \n\n')
        else:
            print('Проверка не пройдена, попробуйте через 5 минут!')
            time.sleep(60*5)

    password = input('Неверный пароль, попробуйте снова: \n')
'''

#  ¬x    --->  (not x)  - отрицание (инверсия)
# x ∧ y  --->  x and y  - конъюнкция (логическое умножение)
# x ∨ y  --->  x or y  - дизъюнкция (логическое сложение)
# x → y  --->  x <= y  - импликация
# x ≡ y  --->  x == y  - тождество (сравнение)

# ((¬x ∨ z) ≡ (y ∧ ¬w)) → (z ∧ y)
# (((not x) or z) == (y and (not w))) <= (z and y)

print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (((not x) or z) == (y and (not w))) <= (z and y)
                if not F:
                    print(x, y, z, w, F)


# endregion Урок: ******************************************************************


# todo: GOAL = []
# todo: КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:  # Циклы и разбор 2-го номера
