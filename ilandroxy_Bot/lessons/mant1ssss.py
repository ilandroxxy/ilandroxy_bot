# region Домашка: ******************************************************************

# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************
'''
def per(N, n):
    s = ''
    while N > 0:
        s = str(N % n) + s
        N //= n
    return s

chisla = []
for N in range(1, 10**5):
    R = per(N, 4)
    if len(R) % 2 == 0:
        R = R[:len(R) // 2] + '0' + R[len(R) // 2:]
    chislo = int(R, 4)
    if chislo < 180:
        chisla.append(N)
print(max(chisla))

for n in range(1, 10**5):
    n_4 = per(n, 4)
    count_d = len(n_4)
    if count_d % 2 == 0:
        n_4 = n_4[:count_d//2] + '0' + n_4[count_d//2:]
    r = int(n_4)
    if r <= 180:
        print(n)
'''


from itertools import product
a1 = '1357'
a2 = '2468'
cnt = 0
for a in a1:
    for b in a2:
        for c in a1:
            for d in a2:
                for e in a1:
                    for f in a2:
                        for g in a1:
                            for h in a2:
                                for k in a1:
                                    s = a + b + c + d + e + f + g + h + k
                                    if all(s.count(x) <= 3 for x in s):
                                        cnt += 1
print(cnt * 2)
# endregion Урок: *******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Марк = [1.1, 2.1, 3.1, 6.1, 4.1, 5.1, 7.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 17.1, 22.1, 23.1, 24.1, 25.1]
# КЕГЭ  = [5.1, 8.1, 9.1, 14.1, 16.1, 23.1]
# на следующем уроке:
