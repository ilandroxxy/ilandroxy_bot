
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************
'''
def F(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    if a < b:
        return F(a+1, b) + F(a+2, b) + F(a*2, b)

print(F(4, 11) * F(11, 13) * F(13, 15))
'''

'''
# Вариант 2
def F(a, b):
    if a >= b:
        return a == b
    return F(a+1, b) + F(a+2, b) + F(a*2, b)

print(F(4, 11) * F(11, 13) * F(13, 15))
'''

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************


# endregion Разобрать: *************************************************************


# Геля = [1, 2, 3, 4, 5, 6, 8, 12, 13, 14, 15, 16, 17, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [5, 8, 9, 13, 14, 18, 19-21, 23]
# на следующем уроке: 17, 22, 24, 25
