# region Домашка: ************************************************************

# endregion Домашка: ************************************************************

# region Урок: **************************************************************

# № 8696 (Уровень: Средний)
'''
def divisors(x):
    div = []
    for j in range(2, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))


k = 0
for x in range(1_273_547+1, 10**10):
    M = sum(divisors(x))
    if M != 0:
        if len(divisors(M % 100_000)) == 0:
            print(x, M)
            k += 1
            if k == 5:
                break
'''

# 24 {1, 2, 3, 4, 6, 8, 12, 24}


# № 8960 Джобс 02.06.2023 (Уровень: Базовый)
'''
from fnmatch import *

def divisors(x):
    div = []
    for j in range(1, int(x**0.5)+1):
        if x % j == 0:
            div += [j, x // j]
    return sorted(set(div))

k = 0
for x in range(500_001, 10**10):
    summa = sum(divisors(x))
    if fnmatch(str(summa), '*7?'):
        print(x, summa)
        k += 1
        if k == 5:
            break
'''
# Ответ:
# 500001 666672
# 500048 968874
# 500069 500070
# 500079 666776
# 500114 750174


# № 9076 Danov2306 (Уровень: Базовый)
from fnmatch import *
for x in range(2023, 10**9, 2023):
    if fnmatch(str(x), '20*23'):
        summa = sum([int(i) for i in str(x)])
        # summa = sum(map(int, s))
        if summa % 7 == 0 and summa < 20:
            print(x)



# endregion Урок: ************************************************************


# region Разобрать: ***************************************************************

# endregion Разобрать: *************************************************************

# Никита = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ = []
# на следующем уроке:
