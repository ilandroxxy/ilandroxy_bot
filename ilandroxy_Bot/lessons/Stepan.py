# Домашка
#Задача №1
'''
x = int(input('x: '))
if x % 2 != 0:
    print(f'YES')
elif x % 2 == 0 and x >= 2 and x <= 5:  # 2 <= x <= 5
    print(f'NO')
elif x % 2 == 0 and x >= 6 and x <= 20:
    print(f'YES')
elif x % 2 == 0 and x > 20:
    print(f'NO')
'''

#Задача №2
'''
x1 = int(input('x1: '))
x2 = int(input('x2: '))
x3 = int(input('x3: '))
M = [x1, x2, x3]
M.sort()
print(M[1])
'''

"""
x1 = int(input('x1: '))
x2 = int(input('x2: '))
x3 = int(input('x3: '))
M = [x1, x2, x3]
#    0   1   2
M.sort()
M.reverse()
print(M[1])


print(sum(M) - (min(M) + max(M)))
"""



#Задача №3
'''
x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))
if x1 == x2 and y1 == y2:
    print('Фигура должна сделать ход!')
elif x1+1 == x2 or y1+2 == y2:
    print('YES')
elif x1+1 == x2 or y1-2 == y2:
    print('YES')
elif x1-1 == x2 or y1+2 == y2:
    print('YES')
elif x1-1 == x2 or y1-2 == y2:
    print('YES')
elif x1+2 == x2 or y1+1 == y2:
    print('YES')
elif x1-2 == x2 or y1+1 == y2:
    print('YES')
elif x1+2 == x2 or y1-1 == y2:
    print('YES')
elif x1-2 == x2 or y1-1 == y2:
    print('YES')
else:
    print('NO')
'''


# Циклы

# Ключевые слова: while, for, range, len,  break, continue, flag


# range
'''
# повтори n раз
for i in range(10):  # [0,10)  - от 0 это стандартное значение start при одном аргументе в range(STOP)
    print(i, end=' ')
print()

# пройди от a до b
for i in range(1, 10):  # [1,10) range(START, STOP)
    print(i, end=' ')
print()

# пройди от a до b c шагом 2
for i in range(0, 10, 2):  # [1,10) range(START, STOP, STEP) шаг
    print(i, end=' ')
print()


for i in range(100, 0, -1):  # [1,10) range(START, STOP, STEP) шаг
    print(i, end=' ')
print()
'''

# len() - функция которая возвращает длину списка (строки) - то есть кол-во элементов в нем

# Сценарии использования цикла фор со списками (строками)
'''
M = [4, 5, 6, 7, 8]
#    0  1  2  3  4


# по факту мы пробегаем список через индексы его элементов
for i in range(0, len(M)):  # [0, 5)
    print(M[i], end=" ")
print()

# Просто пробегаем список прям по элементам
for x in M:
    print(x, end=" ")
print()


for i in range(0, len(M)):
    M[i] = M[i] ** 2
print(M)
print(*M)
'''


# Ввод списка с клавиатуры:

'''
n = int(input("Кол-во элеменитов в списке: "))
M = []
for i in range(n):
    M.append(int(input(f"Добавьте {i+1} элемент: ")))
print(M)
'''

'''
s = '1234'
for x in s:
    print(x * 4)

for x in s:
    print(int(x) * 4)

M = [x for x in s]
print(M)

M = [int(x) for x in s]
print(M)

# M = [int(x) for x in input('Введите числовую строку: ')]
# print(M)


M = [int(x) for x in input().split() if int(x) % 2 == 0]
print(M)
'''

# while - цикл с условием, он выполняется, только лишь если его условие истинно
'''
for i in range(0, 10+1, 2):  # [1,10) range(START, STOP, STEP)
    print(i, end=' ')
print()

i = 0
while i < 10 or i == 10:
    print(i, end=' ')
    i += 2
print()

# Сумма цифр числа
x = 12345
summ = 0
while x > 0:
    summ += x % 10
    x //= 10
print(summ)

# Факториал числа
x = int(input('x: '))
temp = x
f = 1
while x > 0:
    f *= x  # f = f * x
    x -= 1  # x = x - 1
print(f'Факториал числа {temp} = {f}')

# Факториал числа через range
x = int(input('x: '))
f = 1
for i in range(1, x+1):
    f *= i
print(f'Факториал числа {x} = {f}')
'''


# Бесконечный цикл
'''
k = 0
while True:
    k += 1
    print(k)
'''


'''  
import random

count = 0
password = 'qwerty'
while True:
    pas = input('Введите пароль для входа: ')
    if pas == password:
        print("Welcome")
        break
    print('Пароль неверный, попробуйте снова.')
    count += 1
    if count == 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print(f'Пройдите проверку на робота, решив пример:\n'
              f'{a} + {b} =')
        x = int(input())
        if x == a+b:
            count = 0
            print('Проверка пройдена')
            continue
        else:
            print('БАН')
            break
'''


# break - прерывает выполнение цикла, выходит их него
# continue - прерывает итерацию цикл
'''
for i in range(1, 20):
    if i == 15:
        break
    if i % 2 != 0:
        continue
    print(i)
'''

summ = 0
maxi = 0
mini = 0
count = 0
flag = True

for i in range(1234, 12394+1):
    if i % 2 == 0 and i % 4 == 0 and i % 7 != 0 and i % 17 != 0:
        if flag == True:
            mini = i
            flag = False
        count += 1
        summ += i
        maxi = i
print(f'summ = {summ}, maxi = {maxi}, mini = {mini}, count = {count}')











