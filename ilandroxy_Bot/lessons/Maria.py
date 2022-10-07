# Домашка разбираем
'''
#YES or NO
x = int(input())
if x % 2 != 0:
    print('YES')
if x % 2 == 0 and  x >= 2 and x <=5:
    print('NO')
if x % 2 == 0 and x >= 6 and x <= 20:
    print('YES')
if x % 2 == 0 and x > 20:
    print('NO')
'''

'''
#среднее число
a = int(input())
b = int(input())
c = int(input())
if a > b > c or a < b < c:
    print(b)
elif b > a > c or b < a < c:
    print(a)
else:
    print(c)
'''

'''
x1 = int(input('x1: '))
y1 = int(input('y1: '))

x2 = int(input('x2: '))
y2 = int(input('y2: '))

if (x2 == (x1 + 1) and y2 == (y1 - 2)) or (x2 == (x1 + 2) and y2 == (y1 - 1)) or (x2 == (x1 + 2) and y2 == (y1 + 1)) or (x2 == (x1 + 1) and y2 == (y1 +2)) or (x2 == (x1 - 1) and y2 == (y1 + 2)) or (x2 == (x1 + 2) and  y2 == (y1 + 1)) or (x2 == (x1 - 2) and y2 == (y1 -1)) or (x2 == (x1 - 1) and y2 == (y1 - 2)):
    print('YES')
else:
    print('NO')
'''


# Циклы - это повторение каких-либо действий
# Ключевые слова: for, while, range, len, flag, break, continue
'''

for i in range(10):  # [0, 10)  # range(0 - start, 10 - stop)  # 0 - это стандартное значение start при одном аргументе в range
    print(i, end=' ')
print()

for i in range(1, 10):  # [1, 10) # range(1 - start, 10 stop)
    print(i, end=' ')
print()

for i in range(0, 10, 2):  # [1, 10) # range(1 - start, 10 stop, 2 - step) # при трех аргументах
    print(i, end=' ')
print()
'''

# индекс - это порядковый номер элемента в строке, списке, кортеже ... начинается счет с нуля

# Цикл фор для работы со строками
'''
s = '987654321'
#    012345678
print(s[0])

print(len(s))  # длину строки - то есть кол-во элементов в ней

for i in range(0, len(s)):  # форик пробигает элементы строки через их индексное представление
    print(s[i], end=' ')
print()

for x in s:  # пробигает строку напрямую через значение элементов
    print(x, end=' ')
print()
'''


# Цикл фор для работы со списками
'''
M = [9, 8, 7, 6, 5, 4, 3, 2, 1]
#    0  1  2  3  4  5  6  7  8

#M[4] = '*'
print(M)

for x in M:
    print(x, end=" ")
print()

for i in range(0, len(M)):
    M[i] = M[i] ** 2
print(M)
'''

# break - командра нужна для прерывания цикла
# continue - комнада прерывает итерацию цикла
'''

M = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in M:
    if x == 9:
        break
    if x % 2 != 0:
        continue
    print(x)
'''


# Цикл while - это цикл с условием (пока условие истинно - выполняем тело цикла)
'''

for i in range(0, 10+1, 2):
    print(i, end=' ')
print()


i = 0
while i < 10 or i == 10:
    print(i, end=' ')
    i += 2
print()


# Пример
x = int(input('x: '))  # 12345
summ = 0
M = []
while x > 0:
    summ += x % 10
    M.append(x % 10)
    x = x // 10
M.reverse()
print(summ, M)
'''


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
        print('Welcome')
        break
    print("Пароль неверный, попробуйте заново ввести пароль")
    count += 1
    if count == 3:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        print("Пройдите проверку на робота, решите задачу:\n"
              f"{a} + {b} = ")
        x = int(input())
        if x == a + b:
            print("Проверка пройдена!")
            count = 0
        else:
            print('БАН')
            break


