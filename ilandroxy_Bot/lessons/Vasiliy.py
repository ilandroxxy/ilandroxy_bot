# region Домашка: ************************************************************

# 1.КЕГЭ № 6016 ФИПИ 03.02.23
# Откройте файл электронной таблицы, содержащей в каждой строке три натуральных числа.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# – все числа в строке различны;
# – квадрат максимального числа строки меньше суммы квадратов оставшихся чисел.
# В ответе запишите только число.

'''
file = [i[:-1].split("\t") for i in open("ДЗ 12.04.23/1. № 6016.txt").readlines()]      # (´ ∀ ` *)

for i in range(len(file)):          # целыми числа сделать не получилось, значит сделаем тут
    for j in range(len(file[i])):
        file[i][j] = int(file[i][j])

counter = 0
for i in range(len(file)):
    flag = True

    for j in range(len(file[i])-1):
        if file[i][j] == file[i][j+1]:
            flag = False
            break

    maximal = max(file[i][0], file[i][1], file[i][2])
    minimal = min(file[i][0], file[i][1], file[i][2])
    num = file[i][0] + file[i][1] + file[i][2] - maximal - minimal

    if maximal ** 2 >= (minimal ** 2 + num ** 2):
        flag = False

#    print(f'{minimal} {num} {maximal}; {maximal ** 2} {minimal ** 2 + num ** 2} {maximal ** 2 < (minimal ** 2 + num ** 2)}')

    if flag:
        counter += 1
print(counter)
'''



#  КЕГЭ № 6016 ФИПИ 03.02.23 (Уровень: Базовый)
# Откройте файл электронной таблицы, содержащей в каждой строке три натуральных числа.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# – все числа в строке различны;
# – квадрат максимального числа строки меньше суммы квадратов оставшихся чисел.
# В ответе запишите только число.
'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    if len(set(M)) == len(M):
        sred = sum(M) - max(M) - min(M)
        if max(M) ** 2 < sred ** 2 + min(M) ** 2:
            count += 1
print(count)
'''
'''
count = 0
for s in open('9.txt'):
    M = sorted([int(i) for i in s.split()])
    if len(set(M)) == len(M):
        if M[2] ** 2 < M[1] ** 2 + M[0] ** 2:
            count += 1
print(count)
'''
# [25, 45, 93] {25, 93, 45}
# [72, 93, 72] {72, 93}


# Показать ответ: 1312 (было), теперь 1354
# В какой-то момент я решил упростить решение и всё поломал...


# 2.КЕГЭ № 6081 02.2023
# (А. Рогов) Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
# – в строке только одно число повторяется ровно два раза, остальные числа различны;
# – шесть чисел можно разбить на две тройки с равными суммами.
# В ответе запишите только число — количество подходящих строк.
'''
import itertools
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    if len(set(M)) == len(M) - 1:
        if any(sum(A[:3]) == sum(A[3:]) for A in itertools.permutations(M, 6)):
            count += 1
print(count)
'''
# Ответ: 127

'''
f = [i[:-1].split("\t") for i in open("ДЗ 12.04.23/2. № 6081.txt").readlines()]

for i in range(len(f)):
    for j in range(len(f[i])):
        f[i][j] = int(f[i][j])

counter = 0
for i in range(len(f)):

    # 1-е условие:

    flag = True
    rep_flag = False
    rep_num = -1

    for j in range(len(f[i])):
        if f[i].count(f[i][j]) > 2:
            flag = False
        elif f[i].count(f[i][j]) == 2:
            if rep_num == -1:
                rep_num = f[i][j]
                rep_flag = True
            elif f[i][j] != rep_num and rep_flag == True:
                flag = False
    if not rep_flag:
        flag = False

    # 2-е условие (ничего хорошего не вышло) (；￣Д￣)

    if flag:
        counter += 1

    print(f[i], rep_num, flag, counter)

print(counter)
'''

# Показать ответ: ...


# 3.КЕГЭ № 6262 Danov2302
# (А.Богданов Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнено строго одно из условий:

#  – в строке есть повторяющиеся числа;
#  – в строке есть ровно три нечетных числа.
'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    nechet = [i for i in M if i % 2 != 0]
    if (len(set(M)) != len(M) and len(nechet) != 3) or (len(set(M)) == len(M) and len(nechet) == 3):
        count += 1
print(count)
'''
# Ответ: 1852

'''
f = [i[:-1].split("\t") for i in open("ДЗ 12.04.23/2. № 6081.txt").readlines()]

for i in range(len(f)):
    for j in range(len(f[i])):
        f[i][j] = int(f[i][j])

counter = 0
for i in range(len(f)):

    flag_1 = False
    flag_2 = False
    nechet_counter = 0

    for j in range(len(f[i])):
        if f[i].count(f[i][j]) >= 2:
            flag_1 = True
        if f[i][j] % 2 != 0:
            nechet_counter += 1
            if nechet_counter == 3:
                flag_2 = True
            else:
                flag_2 = False

    if flag_1 != flag_2 or flag_1 or flag_2:
        counter += 1

print(counter)
'''

# Показать ответ: 1852 (должно было быть), 1900 с чем-то было, теперь 4632
# И опять я решил оптимизировать код, видимо часть ограничений только казались ненужными...


# 4.КЕГЭ № 6783
# (PRO100 ЕГЭ) Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
#     – в строке только одно число повторяется ровно три раза, остальные числа различны;
#     – среднее арифметическое неповторяющихся чисел строки меньше суммы повторяющихся чисел.
# В ответе запишите только число.


'''
f = [i[:-1].split("\t") for i in open("ДЗ 12.04.23/4. № 6783.txt").readlines()]

for i in range(len(f)):
    for j in range(len(f[i])):
        f[i][j] = int(f[i][j])

counter = 0
for i in range(len(f)):

    rep_flag = False
    flag = True
    rep_num = 0
    for j in range(len(f[i])):
        if f[i].count(f[i][j]) == 3:
            rep_flag = True
            rep_num = f[i][j]
        elif rep_num != f[i][j] and f[i].count(f[i][j]) == 2 and rep_flag == True:
            flag = False
    if not rep_flag:
        flag = False

    if flag:
        summa = 0
        rep_summa = 3 * rep_num
        for j in range(len(f[i])):
            if f[i][j] != rep_num:
                summa += f[i][j]
        if rep_summa <= summa / 3:
            flag = False
    else:
        continue

    if flag:
        counter += 1
print(counter)
'''

# Показать ответ: 125


# endregion Урок: ************************************************************


# todo: Василий = [2, 3, 5, 6, 8, 9, 12, 14+, 15, 16, 17, 18, 19-21, 22, 23, 24, 25.1]
# на прошлом уроке: Рассматривали номера с домашки: 17 и 9 номера
# на следующем уроке:
