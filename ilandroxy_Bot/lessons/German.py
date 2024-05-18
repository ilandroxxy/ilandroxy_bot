# region Домашка: ************************************************************


# endregion Домашка: *********************************************************


# region Урок: ************************************************************


# ¬(((x → y ∧ w) ∧ (z → x ∨ y)) ≡ w)
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x == (w or y)) or ((w <= z) and (y <= w))
                if F == 0:
                    print(x, y, z, w)
'''


'''
def F(a1, a2, x):
    P = 22 <= x <= 35
    Q = 15 <= x <= 30
    A = a1 <= x <= a2
    return (P <= A) and ((not Q) or A)

R = []
M = [x / 4 for x in range(0, 100*4)]
for a1 in M:
    for a2 in M:
        if all(F(a1, a2, x) for x in M):
            R.append(a2-a1)
print(min(R)) 
'''
# Ответ: 20


'''
def F(A, x):
    return (x % 18 == 0) <= ((x % A != 0) <= (x % 12 != 0))

for A in range(1, 10000):
    if all(F(A, x) for x in range(1, 10000)):
        print(A)
'''
# Ответ: 36

'''
def F(x, y, A):
    return (2*y + 4*x < A) or (x + 2*y > 80)

for A in range(0, 10000):
    if all(F(x, y, A) for x in range(100) for y in range(100)):
        print(A)
        break
'''
# Ответ: 321

'''
a = set(range(0, 1000))

def F(x):
    P = x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    Q = x in {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
    A = x in a
    return (A <= P) and (Q <= (not A))


for x in range(0, 10000):
    if F(x) == False:
        a.remove(x)
print(len(a))
'''
# Ответ: 7

# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************

# Герман = []
# КЕГЭ = []
# на следующем уроке:
