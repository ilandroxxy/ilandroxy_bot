# region Домашка: ***************************************************************
'''
a = int(input('Введите возраст'))
if a >= 18:
    print('Вам можно смотреть этот фильм')
else:
    print('Вы слишком молоды для просмотра этого фильма')
'''

# если его номер (кратен 4, но не кратен 100), или если он кратен 400.
'''
a = int(input('Введите год рождения: '))
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print('Дa')
else:
    print('Нет')
'''

# Напишите программу, которая принимает три положительных
# числа и определяет вид треугольника,
# длины сторон которого равны введенным числам.
'''
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a == b == c:
    print('Равносторонний')
elif a == b or b == c or c == a:
    print('Равнобедренный')
else:
    print('Разносторонний')
'''
# endregion Домашка: ************************************************************


# region Урок: ******************************************************************

# Циклы - это какое-то повторяющееся действие n раз

# Цикл for: "повтори n раз", "пробеги от а до б"

# Взаимодействие с циклом for через функцию range()
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

for x in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(x, end=' ')  # 2 4 6 8 10
print()

for x in range(10, 0, -1):  # range(START=10, STOP=0+1, STEP=-1)
    print(x, end=' ')  # 10 9 8 7 6 5 4 3 2 1 
print()
'''

# Через range() мы можем брать элементы списков и менять их
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

print(M[2])  # c
print(M[-3])  # c

for i in range(len(M)):  # Функция len() возвращающая длину списка/строки и тд (кол-во элементов)
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

for i in range(len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

# Через range() мы можем брать элементы строк
'''
s = 'abcde'
for i in range(len(s)):  
    # print(i, end=' ')  # 0 1 2 3 4
    print(s[i], end=' ')  # a b c d e
print()
'''


# # Взаимодействие с циклом for напрямую из коллекции
'''
# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

s = 'abcde'

for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in s:
    print(x, end=' ')  # a b c d e
print()
'''

# Задача: из списка достать все четные числа
'''
import random
M = [random.randint(0, 100) for _ in range(10)]
print(*M)

for x in M:
    if x % 2 == 0:  # если число х четное
        print(x, end=' ')
print()
'''

# Цикл while: "выполняй действие, ПОКА условие верно", "Бесконечный цикл"
'''
for x in range(2, 10+1, 2):  # range(START=2, STOP=10-1, STEP=2)
    print(x, end=' ')  # 2 4 6 8 10
print()


i = 2
while i <= 10:
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
    i += 2
'''

# Бесконечный цикл
'''
k = 1
while True:
    print(k)
    k += 1
'''

# Маленький скриптик на проверку пароля пользователя
'''
import random
import time
pas = 'qwerty'
count = 0
password = input('Введите пароль: ')
while True:
    if pas == password:
        print('Welcome!')
        break
    count += 1
    if count == 3:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        x = int(input(f'{a} + {b} = '))
        if x == a + b:
            print('Проверка на робота пройдена успешно!')
            count = 0
        else:
            print('Подозрительная попытка входа, попробуйте повторить через 10 секунд')
            time.sleep(10)
    password = input('Пароль неверный, попробуйте снова: ')
'''

# endregion Урок: ***************************************************************


# todo: Анастасия = [1.1, 2.1, 3.1, 4.1, 5.1, 7.1, 11.1, 12.1, 13.1, 14.1]
# todo:  КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке: Рассмотреть примеры с переводом в разные системы счисления
