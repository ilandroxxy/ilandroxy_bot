
# region Домашка: ******************************************************************************


# endregion Домашка:  ******************************************************************************



# region Урок:  ******************************************************************************
'''
f = open('26.txt')
s, n = [int(i) for i in f.readline().split()]
M = sorted([int(i) for i in f])
print(s, n, M)
A = []
for i in range(n):
    if sum(A) + M[i] < s:
        A.append(M[i])
    else:
        break
print(sum(A), len(A), max(A))
x = (s - sum(A)) + max(A)
print(x)
M.reverse()
for i in range(n):
    if x not in M:
        x -= 1
    else:
        break
print(len(A), x)
'''
# Ответ: 568 50



# endregion Урок:  ******************************************************************************

# Слава
# todo: РЕШУ ЕГЭ = [1, 2, 5, 6, 8, 9, 12, 13, 14+, 15+, 16, 17, 18, 19-21, 23, 24+, 25.2]
# todo: КЕГЭ [1, 5, 8, 9, 13, 14, 17, 24, 25] # рассмотреть: 6, 9, 22, 17 КЕГЭ
# на прошлом уроке: Начали разбирать 26 номера базовой сложности через таблицы Эксель
# на следующем уроке: