
# region Домашка: ******************************************************************

# Напишите программу, которая запрашивает у пользователя пятизначное число
# и вычисляет произведение и сумму его цифр.
# Необходимо сначала вывести произведение, затем сумму.

# Вариант 1
'''
number = int(input())  # 78212
n1 = number // 10000
n2 = (number // 1000) % 10
n3 = (number % 1000) // 100
n4 = (number // 10) % 10
n5 = number % 10
print(n1 * n2 * n3 * n4 * n5)
print(n1 + n2 + n3 + n4 + n5)
'''

# Вариант 2
'''
number = int(input())  # 78212
summa = 0
my_prod = 1
while number > 0:
    x = number % 10
    summa += x
    my_prod *= x
    number //= 10   # number = number // 10
print(my_prod)
print(summa)
'''

# Вариант 3
'''
import math
number = int(input())  # 78212
ELEM = []
while number > 0:
    x = number % 10
    ELEM.append(x)
    number //= 10   # number = number // 10
print(math.prod(ELEM))
print(sum(ELEM))
'''

# Вариант 4
'''
number = int(input())  # 18212
mult_digits = 1
for k in str(number):
    mult_digits *= int(k)
sum_digits = 0
for i in str(number):
    sum_digits += int(i)

print(mult_digits)
print(sum_digits)
'''

# Вариант 5
'''
import math
number = int(input())
M = [int(x) for x in str(number)]  # [3, 2, 1, 4, 5, 6, 7, 8, 9, 0]
print(math.prod(M))
print(sum(M))
'''

'''
# Создание списка квадратов четных чисел от 0 до 9
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Вывод результатов
print(even_squares)
'''
# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Условные операторы if, elif, else
'''
# x, y = int(input('x: ')), int(input('y: '))
x = 7
y = 6
if x > 0 and y > 0:  # if - если
    print('1 четверть')
elif x < 0 and y > 0:
    print('2 четверть')
elif x < 0 and y < 0:
    print('3 четверть')
elif x > 0 and y < 0:
    print('4 четверть')
else:  # else - иначе
    print('Лежит на осях')
print('КОНЕЦ')
'''

# Вложенные условные операторы (каскады)
'''
x = 7
y = 6
if x > 0:
    if y > 0:  # x > 0, y > 0
        print('1 четверть')
    else:  # x > 0, y <= 0
        print('4 четверть')
else:
    if y > 0:  # x <= 0, y > 0
        print('2 четверть')
    else:  # x <= 0, y <= 0
        print('3 четверть')
'''


# Логические связки and, or, ^, not
'''
flag = True
print(not flag)  # False

a = 7
b = -5
if a > 0 and b > 0:  # and - гарантирует, что оба условия будут выполняться
    print('and')
if a > 0 or b > 0:  # or - хотя бы одно
    print('or')
if (a > 0) ^ (b > 0):  # () ^ () - только одно
    print('^')
 '''

# endregion Урок: **********************************************************


# Михаил = []
# КЕГЭ  = []
# на следующем уроке:
