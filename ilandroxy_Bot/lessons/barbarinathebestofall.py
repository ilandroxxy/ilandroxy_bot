
# region Домашка: ******************************************************************
'''
result = {}  # dict
for i in range(301, 1000):
    s = i * '5'
    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '55', 1)
    n = s.count('5')
    if result.get(n) == None:
        result[n] = i

# print(result)
# print(max(result))  # максимальное кол-во пятерок
print(result[max(result)])
'''

'''
R = []
maxi = 0
for i in range(301, 500):
    s = i * '5'
    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '55', 1)
    if maxi < s.count('5'):
        maxi = s.count('5')
        R.append(i)
        # print(i, maxi)
print(max(R))
'''

'''
for i in range(301, 500):
    s = i * '5'
    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '55', 1)
    print(i, s.count('5'))
'''


from itertools import permutations
R = []
M = ['0' * 19, '1' * 13, '2' * 17]
for elem in permutations(M):
    s = ''.join(elem)
    while '10' in s or '20' in s:
        if '20' in s:
            s = s.replace('20', '00', 1)
        else:
            s = s.replace('10', '200', 1)
    R.append(s.count('0'))
print(max(R))
# endregion Домашка: ******************************************************************


# region Урок: ********************************************************************



# endregion Урок: ******************************************************************


# Варя = [2.1, 6.1, 12.1]
# КЕГЭ  = []
# на следующем уроке:
