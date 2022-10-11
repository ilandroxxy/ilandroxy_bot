# Домашка:

# Самописный калькулятор
'''
a = int(input('a: '))
s = input('s: ')
b = int(input('b: '))

if s == '+':
    print(f'{a} {s} {b} = {a + b}')
elif s == '-':
    print(f'{a} {s} {b} = {a - b}')
elif s == '*':
    print(f'{a} {s} {b} = {a * b}')
elif s == "/"  and b == 0:
    print('На ноль делить нельзя')
elif s == "/":
    print(f'{a} {s} {b} = {a / b}')
else:
    print('Ошибка')
'''

# Принадлежность 3
'''
x = int(input())
# if(x > -30 and x <= -2) or (x > 7 and x <= 25):
if(-30 < x <= -2) or (7 < x <= 25):
    print('yes')
else:
    print('no')
'''


# Красивое число
'''
x = int(input())
if(x % 17 == 0 or x % 7 == 0) and ( x > 1000 or x < 9999):
    print('yes')
else:
    print('no')
'''


'''
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 and y1 == y2:
    print('Фигура обязана походить!')
elif x1 == x2 or y1 == y2:
    print('yes')
else:
    print('no')
'''




# Циклы - какие-либо повторяющиеся действия
# Ключевые слова: while, for, range, in, len, break, continue, flag


# for - повторить n раз, пробежать список/строку, пробежать диапазон range
"""
for i in range(10+1):  # открываем цикл for и по переменной i пробегаем в диапазоне до 10. Диапазон: [0, 10) , step == 1
    print(i, end=' ')
print()

for i in range(10, 20+1):  # Диапазон: [10, 21). range(start, stop), step == 1
    print(i, end=' ')
print()

for i in range(0, 10+1, 2):  # Диапазон: от [0, 11) с шагом 2. range(start, stop, step)
    print(i, end=' ')
print()

for i in range(10, 0, -1):  # Диапазон: от [10, 0) с шагом -1. range(start, stop, step)
    print(i, end=' ')
print()

s = '54345'
S = [5, 4, 3, 4, 5]
#    0  1  2  3  4
print(len(S))  # len() - функция возвращает длину списка/строки/коллекции

for i in range(0, len(S)):  # способ пробежать список/строку через индексы элементов
    print(S[i])

for i in range(0, len(S)):  # способ поменять элементы списка/строки через индексы элементов
    S[i] = S[i] ** 2

print(S)

for x in s:  # пробегаем список/строку напрямую через значение элементов
    print(x)
"""

# while - цикл с условием, выполняется пока условие принимает истинное значение
"""
for i in range(0, 10+1, 2):
    print(i, end=' ')
print()

i = 0
while i <= 10:
    print(i, end=' ')
    i += 2
print()

'''
x = int(input('x: '))
summ = 0
while x > 0:
    summ += x % 10
    x //= 10
print(summ)
'''

x = 8
M = []
while x > 0:
    M.append(x % 2)
    x //= 2
M.reverse()
print(M)

# Тип 14 № 16391
# Значение выражения 49**7 + 7**20 − 28? записали в системе счисления с основанием 7.
#
# Сколько цифр 6 содержится в этой записи?
#
x = 49**7 + 7**20 - 28
M = []
while x > 0:
    M.append(x % 7)
    x //= 7
M.reverse()
print(M, M.count(6))
# Ответ: 12
"""



# break, continue
"""

for i in range(1, 20):
    if i == 15:
        break  # прерывает выполнение цикла
    if i % 2 != 0:
        continue  # прерывает итерацию цикла
    print(i, end=' ')
print()
"""


# 17_1: Демоверсия варианта ЕГЭ по информатике 2021, ФИПИ:
# Рассматривается множество целых чисел, принадлежащих числовому отрезку [1016; 7937],
# которые делятся на 3 и не делятся на 7, 17, 19, 27. Найдите количество таких чисел и максимальное из них.
# В ответе запишите два целых числа: сначала количество, затем максимальное число.
"""

count = 0
maxi = 0
summ = 0
mini = 0
flag = True

for i in range(1016, 7937+1):
    if i % 3 == 0 and i % 7 != 0 and i % 17 != 0 and i % 19 != 0 and i % 27 != 0:
        if flag == True:
            mini = i
            flag = False
        count += 1
        maxi = i
        summ += i

print(f'count= {count}, maxi = {maxi}, summ = {summ},  mini = {mini}')
"""



# бесконечный цикл
'''
count = 0
while True:
    print(count)
    count += 1
'''

password = 'qwerty'
count = 0
while True:
    pas = input('Введите пароль: ')
    if pas == password:
        print('Welcome')
        break
    print('Пароль неверный, попробуйте еще раз!')
    count += 1
    if count == 3:
        print(f'Пройдите проверку на робота, решите пример:\n33 + 67 = ')
        x = int(input())
        if x == 100:
            print('Проверка пройдена')
            count = 0
            continue
        else:
            print('БАн')
            break


