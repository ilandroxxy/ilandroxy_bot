# region Домашка: ***************************************************************


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************

# Тип 23 №5785
# У исполнителя Удвоитель две команды, которым присвоены номера:
# 1. прибавь 1,
# 2. прибавь 4.
# Сколько есть программ, которые число 3 преобразуют в число 15?
'''
def F(start, stop):
    if start > stop:
        return 0
    elif start == stop:
        return 1
    else:
        return F(start + 1, stop) + F(start + 4, stop)

print(F(3, 15))
'''

'''
def F(start, stop):
    if start >= stop:
        return start == stop  
    return F(start + 1, stop) + F(start + 4, stop)

print(F(3, 15))  
'''
# Ответ: 26

# Тип 23 №47227
# 1. Прибавить 1
# 2. Умножить на 2
# Сколько существует программ, для которых при исходном числе 1 результатом является число 35,
# при этом траектория вычислений содержит число 10 и не содержит 17?
'''
def F(start, stop):
    if start > stop or start == 17:
        return 0
    elif start == stop:
        return 1
    else:
        return F(start + 1, stop) + F(start * 2, stop)


print(F(1, 10) * F(10, 35))


def F(start, stop):
    if start >= stop or start == 17:
        return start == stop
    return F(start + 1, stop) + F(start * 2, stop)


print(F(1, 10) * F(10, 35))
'''
# Ответ: 98


# Тип 23 №7347
# 1. прибавь 1
# 2. сделай чётное
# 3. сделай нечетное
# 4. умножь на 10
#
# Первая из них увеличивает на 1 исходное число x,
# вторая умножает это число на 2,
# третья переводит число x в число 2x+1,
# четвертая умножает его на 10.

# Сколько существует программ, которые число 1 преобразуют в число 14?
'''
def F(start, stop):
    if start > stop:
        return 0
    elif start == stop:
        return 1
    else:
        return F(start+1, stop) + F(start*2, stop) + F(start*2 + 1, stop) + F(start*10, stop)

print(F(1, 14))
'''
# Ответ: 71


# Тип 23 №11123
# 1. Вычти 2
# 2. Вычти 5
# Сколько есть программ, которые число 22 преобразуют в число 2?
'''
def F(start, stop):
    if start < stop:
        return 0
    elif start == stop:
        return 1
    else:
        return F(start-2, stop) + F(start-5, stop)

print(F(22, 2))
'''
# Ответ: 23


# Тип 15 №18087
# Для какого наименьшего целого неотрицательного числа A выражение
# (y + 2x < A) ∨ (x > 15) ∨ (y > 30)
# тождественно истинно при всех вещественных значениях x и y?
'''
# Вариант 1
def F(x, y, A):
    return (y + 2*x < A) or (x > 15) or (y > 30)


for A in range(0, 1000):
    flag = True
    for x in range(0, 100):
        for y in range(0, 100):
            if F(x, y, A) == False:
                flag = False
                break
    if flag == True:
        print(A)
        break

# Вариант 2
def F(x, y, A):
    return (y + 2*x < A) or (x > 15) or (y > 30)


for A in range(0, 1000):
    if all(F(x, y, A) for x in range(0, 100) for y in range(0, 100)):
        print(A)
        break

# Вариант 3
for A in range(0, 1000):
    if all(((y + 2*x < A) or (x > 15) or (y > 30)) for x in range(0, 100) for y in range(0, 100)):
        print(A)
        break

# Вариант 4
R = []
for A in range(0, 1000):
    if all(((y + 2*x < A) or (x > 15) or (y > 30)) for x in range(0, 100) for y in range(0, 100)):
        R.append(A)
print(min(R))

# Вариант 5
print(min([A for A in range(0, 1000) if all(((y + 2*x < A) or (x > 15) or (y > 30)) for x in range(0, 100) for y in range(0, 100))]))
'''

# Тип 15 №27412
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# Для какого наибольшего натурального числа А формула
# ¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 9))
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?
'''
def F(A, x):
    return (x % A != 0) <= ((x % 6 == 0) <= (x % 9 != 0))


for A in range(1, 1000):
    if all(F(A, x) for x in range(1, 1000)):
        print(A)
'''
# Ответ: 18


# Тип 15 №38949
# Для какого наименьшего неотрицательного целого числа А формула
#
# x & 85 = 0 → (x & 54 ≠ 0 → x & А ≠ 0)
#
# тождественно истинна (т. е. принимает значение 1 при любом неотрицательном целом значении переменной x)?

def F(A, x):
    return (x & 85 == 0) <= ((x & 54 != 0) <= (x & A != 0))


for A in range(0, 1000):
    if all(F(A, x) for x in range(0, 1000)):
        print(A)
        break

# endregion Урок: ***************************************************************


# Анастасия = [2.1, 5.1, 6.1, 8.1, 12.1, 14.1, 16.1, 23.1]
# КЕГЭ  = []
# на следующем уроке:
