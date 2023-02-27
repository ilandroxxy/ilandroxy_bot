# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Условные операторы (ветвление) - if, elif, else
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0 and y > 0:  # if - если (выполняется условие)
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:  # elif - иначесли (промежуточное условие между if и elif)
    print(3)
elif x > 0 and y < 0:
    print(4)
else:           # else - иначе (если не выполняются вышеописанные условия)
    print('Лежит на осях')
'''

# Каскадные условные операторы
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0:
    if y > 0:  # x > 0 and y > 0
        print(1)
    else:    # x > 0 and y <= 0
        print(4)
else:
    if y > 0:  # x <= 0 and y > 0
        print(2)   
    else:     # x <= 0 and y <= 0
        print(3)
'''

'''
a, b, c = int(input('a: ')), int(input('b: ')),  int(input('c: '))
print(a, b, c)
if a > 0 and b > 0 and c > 0:
    print('все числа обязательно больше 0')
elif a > 0 or b > 0 or c > 0:
    print('хотя бы одно из чисел больше 0')
elif not(a > 0 or b > 0 or c > 0):
    print('хотя бы одно из чисел б345')
else:
    print('что-то не так')
'''

# while, for - циклы в Python

# print(4, 5, 6, sep=', ')


# цикл for - повтори n раз, пробеги коллекцию, пробеги строку, пробеги от а до б
'''
for i in range(10):   # range(START=0, STOP=10, STEP=1)
    print(i, end=' ')  # повтори 10 раз
print()

for i in range(2, 10):   # range(START=2, STOP=10, STEP=1)
    print(i, end=' ')  # повтори 10 раз
print()

for i in range(2, 10, 2):   # range(START=2, STOP=10, STEP=2)
    print(i, end=' ')  # повтори 10 раз
print()

for i in range(10, 0, -1):   # range(START=10, STOP=0, STEP=-1)
    print(i, end=' ')  # повтори 10 раз
print()

# i  0  1  2  3  4  5
M = [6, 3, 4, 7, 8, 2]
print(len(M))  # выведет длину списка, то есть кол-во цифр в нем
#-i -6 -5 -4 -3 -2 -1
print(M[0])  # доступ по индексу к минимальному элементу
print(M[-1])  # доступ по индексу к максимальному элементу

for i in range(0, len(M)):
    print(f'Элемент списка {M} под индексом {i} равен {M[i]}')

string = 'alphabet'
for i in string:
    print(i*4, end=' ')
'''

# while - это цикл с условием, тело цикла выполняется, только если условие истинно
'''
x = 12345
summ = 0
while x > 0:
    summ += x % 10
    x //= 10
print(summ)
'''


'''
for i in range(2, 10+1, 2):   # range(START=2, STOP=10, STEP=2)
    print(i, end=' ')  # повтори 10 раз
print()

i = 2
while i <= 10:
    print(i, end=' ')
    i += 2
'''

for x in range(2, 16):  # [0, 16)
    if x == 14:
        break
    if x % 2 == 0:
        continue
    print(x, end=' ')


print('\n\n')

import random
password = 'qwerty'

count = 0
while True:
    pas = input('Введите пароль: ')
    if pas == password:
        print('Welcome')
        break
    count += 1
    if count == 3:
        a = random.randint(1, 100)
        s = random.choice(['-', '+'])
        b = random.randint(1, 100)
        x = int(input(f'решите пример: {a} {s} {b} = '))
        if s == '+' and x == a + b:
            print('Вы не робот, спасибо за проверку')
            count = 0
        elif s == '-' and x == a - b:
            print('Вы не робот, спасибо за проверку')
            count = 0
        else:
            print('BANNED')
            break

    else:
        print('Пароль неверный, попробуйте снова')

# endregion Урок: ******************************************************************



# todo: Егор = []
# на прошлом уроке: Проговаривали теорию условных операторов и циклов
# на следующем уроке:
