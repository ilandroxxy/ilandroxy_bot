
# region Тип 14 № 18444
'''
# Сколько единиц содержится в двоичной записи значения выражения: 4**16 + 2**36 - 8?
x = 4**16 + 2**36 - 8
M = []
while x > 0:
    M.append(x % 2)
    x //= 2
M.reverse()
print(M, M.count(1))
'''
# Ответ: 30
# endregion Тип 14 № 18444

# region Тип 14 № 25846
'''
#Значение арифметического выражения: 9**8·3**20 − 3**10 − 3— записали в системе счисления с основанием 3.
# Сколько цифр 2 содержится в этой записи?
x = 9 ** 8 * 3**20 - 3**10 - 3
N = []
while x > 0:
    N.append(x % 3)
    x //= 3
    N.reverse()
print(N.count(2))
'''
# Ответ: 34
# endregion Тип 14 № 25846