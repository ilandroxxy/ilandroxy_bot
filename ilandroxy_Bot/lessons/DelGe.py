# region Домашка: ************************************************************
'''
x = 766**66 + 15**13 - 22
M = []
while x > 0:
    M.append(x % 13)
    x //= 13
M.reverse()
print(M.count(12))  # 10 - A, 11 - B, 12 - C
'''

'''
alphabet = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")
for x in alphabet[:15]:
    A = int(f"97531{x}19", 15)
    B = int(f"3{x}519", 15)
    if (A + B) % 11 == 0:
        print((A + B) // 11)
        exit()
'''

'''
alphabet = sorted("0123456789QWERTYUIOPASDFGHJKLZXCVBNM")
for y in alphabet[:15]:
    for x in alphabet[:15]:
        A = int(f"123{x}5", 15)
        B = int(f"67{y}9", 17)
        if (A + B) % 131 == 0:
            print((A + B) // 131)
            exit()
'''
'''
for x in range(1, 10000):
    n = 4**2015 + 2**x - 2**2015 + 15
    if bin(n)[2:].count('1') == 500:
        print(x)
        exit()
'''

'''
s = 95 * "1" + 31 * "7"
while "1111" in s:
    s = s.replace("1111", "7", 1)
    s = s.replace("77", "1", 1)
print(s)
'''

'''
for n in range(301, 1000):
    s = '8' * n
    while "555" in s or "888" in s:
        s = s.replace("555", "8", 1)
        s = s.replace("888", "55", 1)
    if s.count('5') == 1 and s.count('8') == 1:
        print(n)
        exit()
'''

# КЕГЭ № 2383 (Уровень: Базовый)
#
# На вход приведённой ниже программе поступает строка, начинающаяся с символа «>»,
# а затем содержащая 11 цифр 1, 12 цифр 2 и 30 цифр 3, расположенных в произвольном порядке.
#
# Определите сумму числовых значений цифр строки, получившейся в результате выполнения программы.

# ПОКА  нашлось (>1)  ИЛИ нашлось (>2)  ИЛИ нашлось (>3)
#    ЕСЛИ  нашлось (>1)
#       ТО заменить (>1, 22>)
#    ЕСЛИ  нашлось (>2)
#       ТО заменить (>2, 222>)
#    ЕСЛИ  нашлось (>3)
#       ТО заменить (>3, 1>)


# endregion Домашка: ************************************************************


# region Урок: ************************************************************


# endregion Урок: ************************************************************


# Евгений = [2.1, 8.1, 12.1, 14.1]
# КЕГЭ = []
# на следующем уроке:
