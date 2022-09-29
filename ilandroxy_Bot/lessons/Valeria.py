# Разбираем 2, 6, 22 номера

# HOMEWORK
'''
a = int(input())
b = int(input())
if a == 1:
    a += 1
for num in range(a, b+1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)
'''

'''
a = int(input())
b = int(input())
if a == 1:
    a += 1
for num in range(1, 15+1):
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    if flag == True:
        print(num)
'''

'''
m = int(input())
n = int(input())
if m < n:
    for i in range(m, n+1):
        print(i)
else:
    for i in range(m, n-1, -1):
        print(i)
'''


'''
n = int(input())
summ = 0
count = 0
mltpl = 1
first_digit = 0

flag = True
while n != 0:
    if flag == True:
        last = n % 10
        flag = False
    last_digit = n % 10
    summ += last_digit
    count += 1
    if last_digit != 0:
        mltpl *= last_digit
        first_digit = last_digit
        n = n // 10
print(summ)
print(count)
print(mltpl)
print(summ / count)
print(first_digit)
print(first_digit+last)
'''


# Тип 22 № 3274
'''
# Ниже записана программа. Получив на вход число x, эта программа печатает два числа, L и M.
# Укажите наименьшее из таких чисел x, при вводе которых алгоритм печатает сначала 3, а потом 8.

for i in range(0, 1000000):
    x = i
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if x % 2 == 0:
            M = M + x % 10
        x = x // 10
    if L == 3 and M == 8:
        #print(i, L, M)  # L = 3, M = 8
        print(f'x = {i}, L = {L}, M = {M}')  # L = 3, M = 8
'''
# Ответ: 108



# Тип 2 № 47206
# Миша заполнял таблицу истинности логической функции F
#
# ¬(y→x)∨(z→w)∨¬z,
#
# но успел заполнить лишь фрагмент из трёх различных её строк, даже не указав,
# какому столбцу таблицы соответствует каждая из переменных w, x, y, z.



# Действия в математической логике
# отрицание ¬z  <---->  (not(z))
# конъюнкция x ∧ y   <---->   x and y
# дизъюнкция  x ∨ y   <---->  x or y
# импликация  z → w   <---->   z <= w
# тождество  x ≡ w   <---->   x == w


print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (not(y <= x)) or (z <= w) or (not(z))
                if F == False:
                    print(x, y, z, w, F)
                # ¬(y→x)∨(z→w)∨¬z

