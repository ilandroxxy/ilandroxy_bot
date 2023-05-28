
# region Домашка: ******************************************************************************


# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************

# Тип 23 № 18724
# Исполнитель Вычислитель преобразует число на экране.
# У исполнителя есть три команды, которым присвоены номера:
#
# 1. Прибавить 1
# 2. Умножить на 3
# 3. Прибавить 2

# Сколько существует программ, которые преобразуют исходное число 1 в число 15
# и при этом траектория вычислений содержит числа 10 и 12?
"""
def MySum(x: int) -> int:
    '''
    Функция для подсчета суммы цифр числа
    :param x: Принимает цело число
    :return: Возвращает сумму цифр этого числа
    Пример: 12345 = 15
    '''
    summ = sum([int(i) for i in str(x)])
    return summ

r = MySum(12345)
print(r)
"""


M = [1, 2, 3]
M.clear()
print(M.clear.__doc__)  # Remove all items from list.

'''
def F(a, b):
    if a > b:
        return 0
    elif a == b:
        return 1
    else:
        return F(a+1, b) + F(a*3, b) + F(a+2, b)


print(F(1, 10) * F(10, 12) * F(12, 15))


def F(a, b):
    if a >= b:
        return a == b  # False -> 0  # True -> 1
    return F(a+1, b) + F(a*3, b) + F(a+2, b)


print(F(1, 10) * F(10, 12) * F(12, 15))


print(True + True + False + True)
'''
# Ответ: 504


# Тип 15 № 18594
# Для какого наименьшего целого неотрицательного числа A выражение
#
# (2m + 3n > 43) ∨ (m < A) ∨ (n ≤ A)
#
# тождественно истинно при любых целых неотрицательных m и n?
'''
def F(m, n, A):
    return (2*m + 3*n > 43) or (m < A) or (n <= A)

for A in range(0, 1000):
    flag = True
    for m in range(0, 100):
        for n in range(0, 100):
            if F(m, n, A) == False:
                flag = False
                break
        if flag == False:
            break
    if flag == True:
        print(A)
        break
'''

'''
def F(m, n, A):
    return (2*m + 3*n > 43) or (m < A) or (n <= A)

for A in range(0, 1000):
    if all(F(m, n, A) for m in range(0, 100) for n in range(0, 100)):
        print(A)
        break
 '''

'''
def F(m, n, A):
    return (2*m + 3*n > 43) or (m < A) or (n <= A)

R = []
for A in range(0, 1000):
    if all(F(m, n, A) for m in range(0, 100) for n in range(0, 100)):
        R.append(A)
print(min(R))
'''

'''
print(min([A for A in range(0, 1000) if all(((2*m + 3*n > 43) or (m < A) or (n <= A)) for m in range(0, 100) for n in range(0, 100))]))
'''
# Ответ: 9


# endregion Урок: ******************************************************************************


# todo:    Иван  =  []
# todo: Иван КЕГЭ = []
# на прошлом уроке:
# на следующем уроке:
