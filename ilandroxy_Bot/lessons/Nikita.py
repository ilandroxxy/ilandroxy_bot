# region Домашка


# endregion Домашка


# region Урок

# тип коллекции Словарь dict()
'''
A = {}  # пустой словарь
B = set()

B = {1, 2, 3, 4}
A = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 'five': 5}

print(A[4])
print(A['five'])

Students = {}
Students['Никита'] = ['Nikita.py', '8x6800', 'Monday']
print(Students)

Students['Никита'][1] = '4x3600'
print(Students)

Students['Никита'].append(1000)
print(Students)

Students['Никита'] += ['Ghbd', 123, True]
print(Students)
'''




# Тип 25 № 47022
'''
# Пусть M(N) — пятый по величине делитель натурального числа N без учёта самого числа и единицы. Например, M(1000)=100.
#
# Если у числа N меньше 5 различных делителей, не считая единицы и самого числа, считаем, что M(N)=0.
#
# Найдите 5 наименьших натуральных чисел, превышающих 300000000, для которых M(N)>0.
# В ответе запишите найденные значения M(N) в порядке возрастания соответствующих им чисел N.

from math import sqrt
A = []
count = 0
for i in range(300000000+1, 500000000):
    M = []

    for j in range(2, round(sqrt(i)) + 1):
        if i % j == 0:
            M.append(i // j)
                if len(M) == 5:
                    A.append(M)
                    count += 1
                    break
    if count == 5:
        break

for x in A:
    print(x)


'''

# endregion Урок


# todo: Никита = [2, 5, 6, 8, 12, 14, 15, 16, 17, 23, 24], на следующем уроке: порешиваем 25
