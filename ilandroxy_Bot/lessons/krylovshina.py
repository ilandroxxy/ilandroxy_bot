# region Домашка: ***************************************************************


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************
'''
print('x y z w')
for x in range(2):  # range(START=0, STOP=2-1, STEP=1)
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x <= y) or (y == w)) and ((x or z) == w)
                if F == True:
                    print(x, y, z, w)
'''

'''
i = (900 * 2**13) / (1200*900)
i = 6
Colors = 2**i
print(Colors)
'''

'''
s = '2' + '9' * 100  # исходная срока
while '19' in s or '299' in s or '3999' in s:
    s = s.replace('19', '2', 1)
    s = s.replace('299', '3', 1)
    s = s.replace('3999', '1', 1)

print(s)  # получившееся строка 
'''
'''
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n > 3:
        return F(n-3) * n

print(F(10))  # 280
'''


x = 16**18 * 4**10 - 4**6 - 16
M = []
while x > 0:
    M.append(x % 4)
    x //= 4
M.reverse()
print(M.count(3))  # 43

# endregion Урок: ***************************************************************


# Анастасия = [2.1, 5.1, 6.1, 8.1, 12.1, 14.1, 16.1, 17.1, 23.1]
# КЕГЭ  = []
# на следующем уроке:
