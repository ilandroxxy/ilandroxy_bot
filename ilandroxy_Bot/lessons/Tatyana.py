
# region Домашка:  **************************************************

# Тип 9 № 38943
'''
count = 0
for s in open('papka/91.txt'):
    M = [int(i) for i in s.split()]
    maxi = max(M)2
    summ = sum(M) - max(M) - min(M)
    if summ  2 + min(M)**2 > maxi:
        count += 1
print(count)
# Answer: 1074
'''
# № 35898

# Тип 9 № 35898 Добавить в вариант
# Электронная таблица содержит результаты ежечасного измерения температуры воздуха на протяжении трёх месяцев.
# Определите, сколько раз за время измерений результат очередного измерения оказывался ниже результата предыдущего на 2 и более градусов.
'''
count = 0
A = []
for s in open('9.txt'):
    M = [float(i) for i in s.replace(',', '.').split()]
    A += M

for i in range(0, len(A)-1):
    if A[i] - A[i+1] >= 2:
        count += 1
print(count)
'''
#Answer: 458

# № 38588
'''
count = 0
for s in open('papka/93.txt'):
    M = [int(i) for i in s.split()]
    maxi = max(M)
    summ = sum(M) - max(M) - min(M)
    if summ + min(M) > maxi:
        count += 1
print(count)
# Answer: 2453
'''

# № 27522
'''
A = []
count = 0
for s in open('papka/9_27522.txt'):
    M = [float(i) for i in s.replace(',','.').split()]
    A += M
    sred = round(sum(A)/len(A), 1)
    for i in A:
        if A[i] > sred:
            count += 1
print(count)
'''

# Тип 24 № 27690
'''
s = open('papka/zadanie24_1.txt').readline()
count  = 1
max_count = 0
for i in range(0, len(s) - 1):
    if s[i] != s[i+1]:
        count += 1
        max_count = max(max_count, count)
    else:
        max_count = max(max_count, count)
        count = 1
print(max_count)
#Answer: 42
'''

# № 36037
'''
s = open('papka/24.txt').readline()
s = s.replace('XZZY', ' ')
M = [len(i) for i in s.split()]
print(3 + max(M) + 3)
#Answer: 1713
'''
# № 27699
'''
s = open('papka/zadanie24_2.txt').readline()
print(s)
print(len('LDRLDRLDRLDRLDR'))
#Answer: 15
'''

# endregion Домашка: **************************************************



# region Урок:  **************************************************


# endregion Урок:  **************************************************


# todo: Татьяна = [2, 5, 8, 9.1, 12, 14+, 15+, 16, 17, 23, 24.1, 25.2]
# на прошлом уроке: Продолжили решать 24 номера, решала Таня, решили очень много!
# на следующем уроке: Пора переходить к Экселям