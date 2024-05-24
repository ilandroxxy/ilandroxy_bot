# region Домашка: ************************************************************


# endregion Домашка: *********************************************************


# region Урок: ************************************************************

'''
M = [1, 2, 3]

print(max(M))
print(sum(M))

print(max(1, 2, 3))
# print(sum(1, 2, 3))
# TypeError: sum() takes at most 2 arguments (3 given)

def my_sum(*args):
    summa = 0
    for elem in args:
        summa += elem
    return summa


print(my_sum(1, 2, 3))
'''

# a = 4 - присваивание значения
# a == 4 - сравнение двух элементов
# a != 4 - два элемента не равны
# Несколько типов решения 15 номера ЕГЭ:
'''
def F(x, A):
    return (x % 18 == 0) <= ((x % A != 0) <= (x % 12 != 0))

for A in range(1, 1000):
    flag = True
    for x in range(1, 10000):
        if F(x, A) == False:
            flag = False
            break
    if flag == True:
        print(A)
 '''

'''
def F(x, A):
    return (x % 18 == 0) <= ((x % A != 0) <= (x % 12 != 0))

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''

'''
def F(x, y, A):
    return (2*y + 4 * x < A) or (x + 2*y > 80)

for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 10000)):
        print(A)
'''

'''
print('Hello, world!')
# Выводит результат на экран


def hello(s):
    return s


x = hello('Hello, world!')
# Возвращает значение
print(x)  # Hello, world!
'''


def F(a1, a2, x):
    P = 22 <= x <= 35
    Q = 15 <= x <= 30
    A = a1 <= x <= a2
    return (P <= A) and ((not Q) or A)

R = []
M = [x / 4 for x in range(1 * 4, 40 * 4)]
for a1 in M:
    for a2 in M:
        if all(F(a1, a2, x) for x in M):
            R.append(a2 - a1)
print(min(R))  # 20




# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************

# Герман = []
# КЕГЭ = []
# на следующем уроке:
