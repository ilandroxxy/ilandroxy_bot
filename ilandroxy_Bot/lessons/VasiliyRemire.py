
# region Домашка: ******************************************************************

# № 7083 OpenFIPI (Уровень: Базовый)
'''
s = "1" + "0" * 55

while "1" in s:
    if "10" in s:
        s = s.replace("10", "001", 1)
    else:
        s = s.replace("1", "00", 1)

print(s.count('0'))
'''
# Ответ: 112

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

'''
def F(x, A):
    return x ** 2, A ** 3

print(F(4, 5))

c, b = F(4, 5)
print(c, b)
'''

# Напишите функции для проверки числа на простоту
'''
def Prime(num):
    for j in range(2, num):
        if num % j == 0:
            return False
    return True

print(Prime(7))

'''


# Тип 15 №27412
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
#
# Для какого наибольшего натурального числа А формула
#
# ¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 9))
#
# тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?

'''
def F(x, A):
    return (x % A != 0) <= ((x % 6 == 0) <= (x % 9 != 0))


# Вариант 1
Result = []
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not F(x, A):  # if F(x, A) == False:
            flag = False
            break
    if flag:  # if flag == True:
        Result.append(A)
print(max(Result))

# Вариант 2
Result = []
for A in range(1, 1000):
    if all(F(x, A) for x in range(1, 1000)):
        Result.append(A)
print(max(Result))

# Вариант 3
print(max([A for A in range(1, 1000) if all(F(x, A) for x in range(1, 1000))]))
'''
# Ответ: 18


# Тип 15 №34540
# На числовой прямой даны два отрезка: Р = [12, 62] и Q = [52, 92].
# Какова наименьшая возможная длина интервала A, что логическое выражение
# ¬(¬(х ∈ А) ∧ (х ∈ Р)) ∨ (х ∈ Q)
# тождественно истинно, то есть принимает значение 1 при любом значении переменной х.
'''
def F(x, a1, a2):
    P = 12 <= x <= 62
    Q = 52 <= x <= 92
    A = a1 <= x <= a2
    return (not((not A) and P)) or Q

R = []
for a1 in range(5, 100):
    for a2 in range(a1, 100):
        flag = True
        for x in range(5, 100):
            if F(x, a1, a2) == False:
                flag = False
                break
        if flag == True:
            R.append(abs(a2-a1))
print(min(R))
'''
'''
def F(x, a1, a2):
    P = 12 <= x <= 62
    Q = 52 <= x <= 92
    A = a1 <= x <= a2
    return (not((not A) and P)) or Q


R = []
M = [i/3 for i in range(5*3, 100*3)]

for a1 in M:
    for a2 in M:
        if all(F(x, a1, a2) for x in M):
            R.append(a2-a1)
print(min(R))
'''
# Ответ: 39.8 -> 40
# endregion Урок: ******************************************************************


# todo: Василий = [2.1, 5.1, 8.1, 12.1, 14.1, 15.1]
# todo:   КЕГЭ  = []
# на прошлом уроке: Разобрали все 12-ые номера с РЕШУ ЕГЭ от и до.
# на следующем уроке: Повторяем и проверяем домашки по 5, 14, 8, 12 номерам!
