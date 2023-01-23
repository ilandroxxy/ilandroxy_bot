# region Домашка:  **************************************************

# Манъэтонское расстояние
'''
x1, y1, x2, y2 = [int(input()) for i in range(4)]
print(abs(x1-x2)+abs(y1-y2))

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print(abs(x1-x2)+abs(y1-y2))
'''

# 451 градус
'''
F = int(input('F: '))
print(5/9*(F - 32))
'''

# сортировка чисел
'''
a, b, c = int(input())
if a >= b and a >= c and b >= c:
    print(a, b, c)
elif a <= b and a >= c and b >= c:
    print(b, a, c)
elif a <= b and a <= c and b <= c:

    print(c, b, a)
elif a >= b and a >= c and b <= c:
    print(a, c, b)
elif a >= b and a <= c and b <= c:
    print(c, a, b)
else:
    print(a, c, b)
'''

# Вариант 2
'''
a, b, c = sorted([int(input()) for i in range(3)])
print(a, b, c)

'''

# сумма квадратов
'''
a = int(input('a: '))
b = int(input('b: '))
print(f'Сумма квадратов: {a**2+b**2}\n')

'''


# сумма трех чисел
'''
a = int(input())
b = int(input())
c = int(input())
print ({f'{a}+{b}+{c}= {a+b+c}')
'''
# Вариант 2
'''
print(sum([int(input()) for i in range(3)]))
'''

# endregion Домашка: **************************************************


# region Урок:  **************************************************

# ЦИКЛЫ - это повторение каких-то действий - нн-ое кол-во раз

# for: повторить 4 раза, пробежать элементы списка, пробежать список по индексам
'''
for i in range(10+1):  # [0, 10)  range(START=0, STOP, STEP=1)
    print(i, end=' ')
print()

for i in range(2, 10+1):  # [0, 10)  range(START, STOP, STEP=1)
    print(i, end=' ')
print()

for i in range(2, 10+1, 2):  # [0, 10)  range(START, STOP, STEP)
    print(i, end=' ')
print()


for i in range(10-1, 0-1, -1):  # (10, 0]  range(START, STOP, STEP)
    print(i, end=' ')
print()


M = [1, 2, 3, 4, 5]
s = '12345'

for i in range(0, len(M)):  # способ пробегать контейнер (коллекцию, список, строку, ... ) через индексы (порядковые номера элементов)
    print(M[i], end=' ')
print()

for i in range(0, len(M)):
    print(s[i], end=' ')
print()

print(len.__doc__)

for x in M:  # способ пробегать контейнер (коллекцию, список, строку, ...) напрямую по ее элементам
    print(x, end=' ')
print()

for x in s:
    print(x, end=' ')
print()
'''

# while: "пока истинно условие", цикл с условием. Его тело выполняется пока условие истинно
'''
for i in range(2, 10+1, 2):  # [0, 10)  range(START, STOP, STEP=1)
    print(i, end=' ')
print()

i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
print()


M = [1, 0, 1, 0, 1, 1, 1]
N = [1, 0, 1, 0]

while len(M) != len(N):
    if len(M) < len(N):
        M.reverse()
        M.append(0)
        M.reverse()
    else:
        N.reverse()
        N.append(0)
        N.reverse()

print(M)
print(N)
'''

# Бесконечный цикл
'''
import random as r

password = 'qwerty'
count = 0
while True:
    pas = input('Введите ваш пароль: ')
    if pas == password:
        print('Welcome')
        break
    print('Пароль неверный! Попробуйте снова')
    count += 1
    if count == 3:
        a = r.randint(1, 100)
        b = r.randint(1, 100)
        x = int(input(f'Пройдите проверку решив пример: {a} + {b} = '))
        if x == a + b:
            count = 0
            print('Проверка пройдена.')
        else:
            print('Вы робот.')
            break

print('Программа.')
'''

# Теория для 2 номера ЕГЭ
#  ¬y    <---->  (not y)  инверсия (отрицание)
# x ∧ y  <---->  x and y   конъюнкция (логическое умножение)
# w ∨ x  <---->  w or y    дизъюнкция (логическое сложение)
# z → x  <---->  z <= x   импликация
# x ≡ w  <---->  x == w   тождество (по-сути сравнение)

# Тип 2 № 46960
'''
# Логическая функция F задаётся выражением (¬y → (z ≡ w)) ∧ ((z → x) ≡ w).
# На рисунке приведён частично заполненный фрагмент таблицы истинности функции F, содержащий неповторяющиеся строки.
# Определите, какому столбцу таблицы истинности функции F соответствует каждая из переменных x, y, z, w.

print('x y z w F')
for x in range(2):   # [0, 2)
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not y) <= (z == w)) and ((z <= x) == w)
                if F == True:
                    print(x, y, z, w, F)
'''

# endregion Урок:  **************************************************


# todo: Олеся = []
# на прошлом уроке: Разбирали теорию циклов и решили один 2 номер
# на следующем уроке:  Начать на 10 минут пораньше, повторяем и закрепляем 2 номер и переходит через строки к 14 номеру
