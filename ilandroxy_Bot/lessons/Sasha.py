# region Домашка: ************************************************************



# endregion Домашка: ************************************************************


# region Урок: ************************************************************

'''
x = 5  # 5!
r = 1
while x > 0:
    r *= x
    x -= 1
print('Факториал числа: ', r)



x = 10  # 5!
r = 1
while x > 0:
    r *= x
    x -= 1
print('Факториал числа: ', r)



x = 6  # 5!
r = 1
while x > 0:
    r *= x
    x -= 1
print('Факториал числа: ', r)
'''


# Написали свою функцию факториала
'''
def MyFactorial(x):  # x, r - Локальные переменные
    r = 1
    while x > 0:
        r *= x
        x -= 1
    return r

x = MyFactorial(5)
print(x)
print(MyFactorial(10))
print(MyFactorial(6))
'''


'''
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

maxi = max(a, b, c)
mini = min(a, b, c)

sred = (a + b + c) - (maxi + mini)

print(maxi, sred, mini)
'''

# Написали свою функцию поиска среднего из трех чисел
'''
def sred(x, y, z):
    maxi = max(x, y, z)
    mini = min(x, y, z)

    sr = (x + y + z) - (maxi + mini)
    return sr

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

maxi = max(a, b, c)
sr = sred(a, b, c)
mini = min(a, b, c)

print(f'Среднее число из тройки равно: {sr}')
'''


# Тип 15 № 17336
"""
# Для какого наименьшего целого неотрицательного числа A выражение
# (3x + 4y ≠ 60) ∨ ((A ≥ x) ∧ (A ≥ y))
#
# тождественно истинно при любых целых неотрицательных x и y?

def F(A, x, y):
    return ((3*x + 4*y) != 60) or ((A >= x) and (A >= y))

for A in range(0, 1000):
    flag = True
    for x in range(0, 100):
        for y in range(0, 100):
            if F(A, x, y) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break 
"""

# Ответ: 20.


# endregion Урок: ************************************************************



# todo: на следующем уроке: Оформляем портфолио для первого нашего бота.
