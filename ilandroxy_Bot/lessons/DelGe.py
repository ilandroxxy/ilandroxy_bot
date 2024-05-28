# region Домашка: ************************************************************


# endregion Домашка: ************************************************************


# region Урок: ************************************************************

'''
maxi = 0
for n in range(4, 10000):
    s = '8' + '4' * n
    while '11' in s or '444' in s or '8888' in s:
        if '11' in s:
            s = s.replace('11', '4', 1)
        if '444' in s:
            s = s.replace('444', '88', 1)
        if '8888' in s:
            s = s.replace('8888', '1', 1)
    summa = sum([int(x) for x in s])
    summa = sum(map(int, s))
    if maxi < summa:
        maxi = summa
        print(maxi)
'''


# Определите значение суммы числовых значений цифр в строке
'''
s = '3721893721'

# Вариант 1
summa1 = 0
for x in s:
    summa1 += int(x)
print(summa1)

# Вариант 2
# summa2 = s.count('1') + s.count('2') * 2 + ...
summa2 = 0
for i in range(0, 10):
    summa2 += s.count(str(i)) * i
print(summa2)

# Вариант 3
summa3 = sum(map(int, s))
print(summa3)

# Вариант 4
summa4 = sum([int(x) for x in s])
# summa4 = sum([int(x) for x in s if x.isdigit()])
print(summa4)
'''





# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Евгений = [1, 2, 3, 4, 5, 7, 8, 9-, 11, 12, 14, 15, 16, 17-, 18, 19-21, 22, 23]
# КЕГЭ = [12]
# на следующем уроке:
