# region Домашка: ******************************************************************
'''
a = int(input())
b = int(input())
print(a // b)
print(a % b)
'''


# Напишите программу, которая запрашивает
# у пользователя пятизначное число и вычисляет произведение и сумму его цифр.
# Необходимо сначала вывести произведение, затем сумму.

# Sample Input:
# 18212

# Sample Output:
# 32 = 1 * 8 * 2 * 1 * 2
# 14 = 1 + 8 + 2 + 1 + 2

# print(18212 // 10)  # 1821
# print(18212 % 10)  # 2
# print(18212 // 10000)
'''
x = int(input())
a = x // 10000
b = (x // 1000) % 10
c = (x // 100) % 10
d = (x // 10) % 10
e = x % 10
# print(a, b, c, d, e)
print(a*b*c*d*e)
print(a+b+c+d+e)
'''

# Дано натуральное число. Напишите программу, которая вычисляет:
#
# - количество цифр 2 в нем;
# - сколько раз в нем встречается последняя цифра;
# - количество нечетных цифр;
# - сумму его цифр, больших семи;
# - произведение цифр, больших семи
# (если цифр больших семи нет, то вывести 11, если такая цифра одна, то вывести ее);
# - сколько раз в нем встречаются цифры 0 и 4 (всего суммарно).
'''
x = int(input())  # 1276335123
x = str(x)
print(x.count('2'))
print(x.count(x[-1]))
'''

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

'''
import math
print(math.sqrt(16))  # 4.0

a = 7
b = 2
print(f'Возвести число {a} в степень {b}: {a} ** {b} = {a**b} \n'
      f'Взять квадратный корень от числа 16: 16**(1/2) = {16**(1/2)} \n'
      f'Взять кубический корень от числа 27: 27**(1/3) = {27**(1/3)}')

# Возвести число 7 в степень 2: 7 ** 2 = 49
# Взять квадратный корень от числа 16: 16**(1/2) = 4.0
# Взять кубический корень от числа 27: 27**(1/3) = 3.0
'''


# Условные операторы: if, elif, else (ветвление)
'''
x = int(input())
if x > 0:
    print('Число положительное!')
elif x < 0:
    print('Число отрицательное')
else:
    print('Равно нулю')
'''


'''
# x = int(input('x: '))
# y = int(input('y: '))
x = 7
y = 0

if x > 0 and y > 0:  # if - если
    print('Первая четверть!')
elif x < 0 and y > 0:  # elif - иначе если
    print('Вторая четверть!')
elif x < 0 and y < 0:
    print('Третья четверть!')
elif x > 0 and y < 0:
    print('Четвертая четверть!')
else:  # else - иначе
    print('Лежит на осях!')
print('КОНЕЦ')
'''

# Каскадные условия:
'''
x = int(input('x: '))
y = int(input('y: '))
if x > 0:
    if y > 0:  # x > 0 and y > 0
        print('Первая четверть!')
    else:  # x > 0 and y <= 0
        print('Четвертая четверть! ')
else:
    if y > 0:  # x <= 0 and y > 0
        print('Вторая четверть!')
    else:  # x <= 0 and y <= 0
        print('Третья четверть!')
'''
# Логические связки: and, or, () ^ (), not
'''
flag = True
print(not flag)  # not - инверсия

a = 5
b = -6
if a > 0 and b > 0:  # and - гарантирует, что оба условия верные
    print('YES 1')
if a > 0 or b > 0:  # or - говори о том, что любое из условий верное
    print('YES 2')
if (a > 0) ^ (b > 0):  # ^ - гарантирует, что только одно условие верно 
    print('YES 3')
'''


# Напишите программу, которая определяет, является число четным или нечетным.
# Если число чётное, то необходимо вывести "Чётное", иначе вывести "Нечётное".
# Примечание: Используйте деление %.

x = int(input())

if x % 2 == 0:
    print("Чётное")
else:
    print("Нечётное")


# endregion Урок: ******************************************************************

# Вика = []
# КЕГЭ  = []
# на следующем уроке:
