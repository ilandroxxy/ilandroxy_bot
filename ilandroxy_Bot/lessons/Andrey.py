

# Списки в Python - list()
'''
M = []  # пустой список
print(len(M))  # функция len() - возвращает длину списка (кол-во элементов в нем)

# i  0  1  2
A = [1, 2, 3]
# -i -3 -2 -1
print(A, A[0], A[-1])

print(A[0])  # = 1

for x in A:  # цикл пробегает список напрямую по элементам
    print(x)

for i in range(0, len(A)):  # [0, 3) # цикл пробегает индексы элементов
    print(A[i])

for i in range(0, len(A)):
    A[i] = A[i] ** 2
print(A)
'''


# Срезы
'''
M = [1, 3, 8, 12, 5, 32]
print(M)
print(*M)
print(M[1:3+1])
print(M[1:])
print(M[:3+1])
print(M[::-1])
'''

# Функции работающие со списками:
'''
print(sum(M))
print(min(M))
print(max(M))
print(len(M))
print(sum(M) / len(M))

M = sorted(M)
M = sorted(M, reverse=True)
'''

# Методы списков
'''
M = [1, 3, 8, 12, 5, 32]
M.append(0)
M.append(1)
print(M)
M.reverse()
print(M)
M.sort()
print(M)

print(M.count(1))
print(M.index(1))

x = M.pop(4)
print(M, x)
'''

# Список хранит в себе все что угодно:
'''
A = [1, '1', 1.0, True, 2-3, '-3'*2, 7/2, 4 < 10, [1, 2, [1, 2, 3]], (1, 2, 3), {1, 2, 3}, {1: 'one', 2: 'two', 3: 'three'}]
for x in A:
    print(x, type(x))

print(A[8][2][2])
'''


'''
n = int(input("введите длину списка"))
M = []
for i in range(n):
    x = int(input(f"{i+1}. введите число: "))
    M.append(x)
print(*M)
'''

# Списочный выражения
# print([int(i) for i in input('Введите числа через пробел: ').split()])
# print(A)
A = []
while True:
    A += [message for message in input().split() if 'заказ' in message]
    print (A)

# todo: На следующем уроке: Методы списков, Решить задачи по спискам, Функции списков, Списочные выражения

# todo: Бот игра для тренировки устного счета (вычислений)