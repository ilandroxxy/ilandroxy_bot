
#Церемония взвешивания
'''
a=int(input('Введите значение '))
if a < 60:
    print('Лёгкий вес')
elif 60 < a < 64:
    print('Первый полусредний вес')
elif 64 < a < 69:
    print('Полусредний вес')
else:
    print('Не подходит условию задачи')
'''


#Среднее число
'''
a=int(input('Введите число 1 '))
b=int(input('Введите число 2 '))
c=int(input('Введите число 3 '))
if b < a < c or c < a < b:
    print(f'Среднее число - {a}')
elif a < b < c or c < b < a:
    print(f'Среднее число - {b}')
else:
    print(f'Среднее число - {c}')
'''
'''
a=int(input('Введите число 1 '))
b=int(input('Введите число 2 '))
c=int(input('Введите число 3 '))

summ = a + b + c
print(summ - max(a, b, c) - min(a, b, c))
'''


#Ход коня
'''
x1=int(input('Введите x1 '))
y1=int(input('Введите y1 '))
x2=int(input('Введите x2 '))
y2=int(input('Введите y2 '))
if x1==x2 and y1==y2:
    print('Конь остался на месте')
elif x1-x2==2 and y1-y2==1:
    print('YES')
elif x2-x1==2 and y2-y1==1:
    print('YES')
elif x1-x2==2 and y2-y1==1:
    print('YES')
elif x2-x1==2 and y1-y2==1:
    print('YES')
elif x1-x2==1 and y1-y2==2:
    print('YES')
elif x1-x2==1 and y2-y1==2:
    print('YES')
elif x2-x1==1 and y2-y1==2:
    print('YES')
elif x2-x1==1 and y1-y2==2:
    print('YES')
else:
    print('NO')
'''


# Циклы - повторяющееся действие
# Ключевые слова: while, for, range, break, continue, flag

# for - это цикл помогающий пробегать диапазон, списки, строки и тд
"""
n = 10

for i in range(n+1):  # если функция range() принимает один аргумент, то стартует с 0 [0, n)
    print(i, end=' ')
print()

for i in range(0, n+1):  # [0, n) range - диапазон или отрезок
    print(i, end=' ')  # end - убирает /n из print() и вместо подставляет новый знак 'любой символ'
print()  # в каждом принте есть /n - переход на новую строку

for i in range(1, n+1, 2):  # если функция range() принимает три аргумент, то START, STOP, STEP - изменяется шаг цикла
    print(i, end=' ')  # стардартный шаг цикла for при range(1, 2 аргумента) - единица
print()

for i in range(n, -1, -1):  # пример когда нужен дополнительный шаг
    print(i, end=' ')
print()

M = []
for i in range(2, 100+1, 2):  # пример как можно получить список четных значений используя range()
    M.append(i)
print(M)


A = [5, 6, 7, 8, 4, 5]  # в списке элементы имеют порядковый номер - индекс
# i  0  1  2  3  4  5

print(len(A))  # функция len() - выводит длину списка (кол-во элементов в нем)

# цикл for удобен для индексной пробежки по списку
for i in range(0, len(A)):  # [0, len(A) )
    print(f'Элемент {A[i]}, имеет индекс: {i}')

# В данном цикле переменная x получает значения элементов списка (поочередно)
for x in A:
    print(x, end=" ")
print()

# через индексы элементов списка мы можем менять значения этих элементов
for i in range(0, len(A)):  # [0, len(A) )
    A[i] = A[i] ** 2
print(A)

A = '34567'
for i in range(0, len(A)):  # [0, len(A) )
    print(f'Элемент {A[i]} имеет индекс {i}', end=", ")
"""






# while - это цикл с условием (если условие истинно, то тело цикла выполняется)

"""
for i in range(0, 10+1, 2):
    print(i, end=' ')
print()

i = 0  # START
while i <= 10:   # STOP - пока условие истинно - выполнять 
    print(i, end=' ')
    i += 2  # STEP
"""

"""
x = int(input('x: '))
print(x)

summ = 0
while x > 0:
    summ += x % 10
    x //= 10
    print(x, summ)
print('Сумма цифр числа: ', summ)
"""

# break - прерывает цикл
# continue - прерывает итерацию цикла

"""
for i in range(0, 20):
    if i % 2 != 0:
        continue
    if i == 14:
        break
    print(i, end=' ')
print()
print('Welcome')
"""

# Пока делимся
"""
x = int(input('x: '))
M = []
while x % 7 == 0:
    print(x)
    M.append(x)  # .append() это метод списков, который добавляет новый элемент в конец списка
    x = int(input('x: '))
print(M)
"""


# Третья цифра
"""
x = int(input('x: '))
s = str(x)
print(s[2])
"""

# Бесконечный цикл
"""
k = 0
while True:
    k += 1
    print(k)
"""


import random

password = 'qwerty'
count = 0
while True:
    pas = input('Введите пароль: ')
    if pas == password:
        print('Welcome')
        break
    print('Неверный пароль, попробуйте еще раз!')
    count += 1
    if count == 3:
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        print(f'Пройдите проверку на робота!\nРешите уравнение:\n{a} + {b} = ')
        x = int(input())
        if x == a + b:
            print('Проверка пройдена.')
            count = 0
            continue
        else:
            print('BANNED')
            break

# todo: номер 2 из ЕГЭ, начинаем тему списки


