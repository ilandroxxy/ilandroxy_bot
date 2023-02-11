
# region Домашка:  **************************************************

# Тип 9 № 27406
'''
A = []
for s in open('files/9_27406.txt'):
    M = [float(i) for i in s.replace(',','.').split()]
    A += M
print(max(A) - sum(A)/len(A))
# Answer: 14
'''

# Тип 9 № 27518
'''
A = [float(i) for i in open('files/9_27517.txt').read().replace(',','.').split()]
print(min(A) - sum(A)/len(A))
# Answer: -16
'''

# Тип 9 № 27519
'''
count = 0
A = [float(i) for i in open('files/9_27517.txt').read().replace(',','.').split()]
sred = sum(A)/len(A)
for i in range(0, len(A)):
    if A[i] == round(sred, 1):
        count +=1
print(count)
# Answer: 0
'''

# Тип 9 № 27527
'''
count = 0
A = [float(i) for i in open('files/9_27522.txt').read().replace(',','.').split()]
sred = sum(A)/len(A)
double = 2 * min(A)
for i in range(0, len(A)):
    if A[i] < round(sred, 1) and A[i] > double:
        count += 1
print(count)
# Answer: 640
'''

# Тип 9 № 27526
'''
count = 0
A = [float(i) for i in open('files/9_27522.txt').read().replace(',','.').split()]
sred = sum(A)/len(A)
deli = 0.5 * max(A)
for i in range(0, len(A)):
    if A[i] > round(sred, 1) * 0.5 and A[i] < deli:
        count += 1
print(count)
# Answer: 526
'''


# Тип 24 № 36879
'''
s = open('files/inf_26_04_21_24.txt').readlines()
alphabet = 'AZQSWXXDCFTGYHNUJMIKOLP'
maxi = 0
for i in s:
    if i.count('G') < 25:
        for a in alphabet:
            if maxi <= i.rindex(a) - i.index(a):
                maxi = i.rindex(a) - i.index(a)
                print(maxi, a)
# Answer: 1001
'''

# Тип 24 № 38602
'''
# Текстовый файл состоит из символов P, Q, R и S
# Определите максимальное количество идущих подряд символов в прилагаемом файле, среди которых нет идущих подряд символов P.
s = open('files/24.txt').readline()
count = 1
max_count = 0
for i in range(0, len(s)-1):
    if s[i] == 'P' and s[i+1] == 'P':
        count = 1
    else:
        count += 1
        if count > max_count:
            max_count = count
print(max_count)
# Answer: 188
'''


# Тип 24 № 47228
# Текстовый файл состоит из символов A, C, D, F и O.
# Определите максимальное количество идущих подряд пар символов вида согласная + гласная.
'''
s = open('24.txt').readline()

maxi = 0
count = 0
glas = 'AO'
sogl = 'CDF'
for i in range(0, len(s) - 1):
    if (s[i] in sogl and s[i + 1] in glas) or (s[i+1] in sogl and s[i] in glas):
        count += 1
        if maxi <= count:
            maxi = count
    else:
        count = 0

print(maxi/2)
'''

'''
s = open('24.txt').readline()
s = s.replace('CA', '*').replace('DA', '*').replace('FA', '*').replace('CO', '*').replace('DO', '*').replace('FO', '*')
s = s.replace('A', ' ').replace('O', ' ').replace('C', ' ').replace('D', ' ').replace('F', ' ')
M = [len(i) for i in s.split()]
print(max(M))
'''
# Ответ: 95

# Тип 15 № 9322 i
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».
# Для какого наименьшего натурального числа А формула
#
# ДЕЛ(x, А) → (¬ДЕЛ(x, 21) + ДЕЛ(x, 35))
'''
def F(x):
    return (x % A == 0) <= ((x % 21 != 0) or (x % 35 == 0))

for A in range(1, 1000):
    if all(F(x) for x in range(1, 1000)):
        print(A)
        break




for A in range(1, 1000):
    if all(((x % A == 0) <= ((x % 21 != 0) or (x % 35 == 0))) for x in range(1, 1000)):
        print(A)
        break


R = []
for A in range(1, 1000):
    if all(((x % A == 0) <= ((x % 21 != 0) or (x % 35 == 0))) for x in range(1, 1000)):
        R.append(A)
print(min(R))


print(min([A for A in range(1, 1000) if all(((x % A == 0) <= ((x % 21 != 0) or (x % 35 == 0))) for x in range(1, 1000))]))
'''
# Ответ: 5

# Тип 15 № 18594 i
# Для какого наименьшего целого неотрицательного числа A выражение
# (2m + 3n > 43) ∨ (m < A) ∨ (n ≤ A)
# (((2*m + 3*n) > 43) or (m < A) or (n <= A))
# тождественно истинно при любых целых неотрицательных m и n?
'''
print(min([A for A in range(0, 1000) if all((((2*m + 3*n) > 43) or (m < A) or (n <= A)) for m in range(0, 100) for n in range(0, 100))]))
'''
# Ответ: 5


# endregion Домашка: **************************************************



# region Урок:  **************************************************


# endregion Урок:  **************************************************


# todo: Татьяна = [2, 3, 5, 8, 9.1, 12, 14+, 15+, 16, 17, 22, 23, 24, 25.2]
# на прошлом уроке: Решили 15 номер в одну строчку и разобрали 3, 22 номера на ВПР (решу ЕГЭ)
# на следующем уроке: