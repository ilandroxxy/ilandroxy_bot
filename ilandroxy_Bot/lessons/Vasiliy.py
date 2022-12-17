
# region Домашка: ************************************************************


# endregion Домашка: ************************************************************


# region Урок: ************************************************************
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (x == (not y)) <= ((z <= (not w)) and (w <= y))
                print(x, y, z, w, F)
'''

# import random
# M = ['12', '11', '22']
# for n in range(1000):
#     r = '0'
#     while True:
#         r += random.choice(M)
#         if r.count('1') == 10:
#             break
#         if r.count('2') == 10:
#             break
#     r += '0'
#     print(r, r.count('1'), r.count('2'))

# s = '0' + '1' * 10 + '2' * 10 + '0'
# while '00' not in s:
#     s = s.replace('012', '30', 1)
#     if '011' in s:
#         s = s.replace('011', '20', 1)
#         s = s.replace('022', '40', 1)
#     else:
#         s = s.replace('01', '10', 1)
#         s = s.replace('02', '101', 1)
# print(s)

# Тип 14
'''
def INTEGER(A, B):
    a = 0
    A.reverse()
    for i in range(0, len(A)):
        a += A[i] * 37 ** i

    b = 0
    B.reverse()
    for i in range(0, len(B)):
        b += B[i] * 37 ** i

    return a, b

for x in range(2, 37+1):
    A = [1, 2, 3, x]
    B = [4, x, 5, 9]

    a, b = INTEGER(A, B)

    if (a + b) % 36 == 0:
        print((a + b) // 36)
        break

for x in range(37):
    a = list(reversed([1, 2, 3, x]))
    b = list(reversed([4, x, 5, 9]))
    for i in range(4):
        a[i] = a[i] * 37 ** i
        b[i] = b[i] * 37 ** i
    if (sum(a) + sum(b)) % 36 == 0:
        print((sum(a) + sum(b)) // 36)
        break
'''

# Тип 15
'''
def F(x, y, A):
    Q = 144 % x == 0
    W = x % y == 0
    R = (x + y) > 100
    T = (A - x) > y
    return (Q <= (not W)) or R or T

for A in range(1, 1000):
    flag = True
    for x in range(1,100):
        for y in range(1, 100):
            if F(x, y, A) == False:
                flag = False
                break
    if flag == True:
        print(A)
        break
'''


'''
with open("17.txt") as file:
    p = [int(i) for i in file]

    minim = 0
    for i in range(len(p)):
        if minim > int(p[i]) and p[i] % 10 == 5:
            minim = int(p[i])


    counter = 0
    maxim = 0
    for i in range(len(p) - 1):
        a = p[i]
        b = p[i + 1]

        if min(a, b) % 10 == 5 and (b ** 2 + a ** 2) < (minim ** 2):
            counter += 1
            if maxim < b ** 2 + a ** 2:
                maxim = b ** 2 + a ** 2

print(counter, maxim)
'''
# Ответ: 403 99805561

# 39 163709650

# endregion Урок: ************************************************************


# todo: Василий = [2, 5, 6, 8, 12, 14+, 15, 17, 19, 20, 22, 24], на следующем уроке: Добиваем новый СТАТГРАД ВАРИАНТ