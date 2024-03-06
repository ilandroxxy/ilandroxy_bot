# region Домашка: ************************************************************


# endregion Домашка: *********************************************************

# region Урок: ************************************************************

# Тип 9 №61355
# В каждой строке электронной таблицы записаны шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых одновременно выполнены все следующие условия:
# — все числа в строке различны;
# — среднее арифметическое наибольшего и наименьшего чисел в строке
# больше среднего арифметического всех остальных чисел.
#
# В ответе запишите число — количество строк, удовлетворяющих заданным условиям.
'''
cnt = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if len(M) == len(set(M)):
        if ((M[0] + M[-1]) / 2) > (sum(M[1:-1]) / len(M[1:-1])):
            cnt += 1
print(cnt)
'''
# Ответ: 6840


# Тип 9 №58476
# В каждой строке электронной таблицы записаны шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых одновременно выполнены все следующие условия:
#
# — максимальное число встречается в строке ровно один раз;
# — хотя бы одно число в строке повторяется более одного раза;
# — максимальное число в строке превышает среднее арифметическое всех остальных чисел этой строки более чем в три раза.
# В ответе запишите число — количество строк, для которых выполнены эти условия.
'''
cnt = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if M.count(max(M)) == 1:
        if len(M) != len(set(M)):
            if max(M) > (sum(M[:-1]) / len(M[:-1])) * 3:
                cnt += 1
print(cnt)
'''

# № 12918 PRO100 ЕГЭ 26.01.24 (Уровень: Средний)
# Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# Определите сумму чисел в строке таблицы с наименьшим номером, для которой выполнены все условия:
#
# в строке есть два числа, которые повторяются дважды, остальные два числа различны;
# максимальное число строки не повторяется;
# произведение максимального и минимального чисел строки больше суммы оставшихся четырёх чисел.
# В ответе запишите только число.
'''
cnt = 0
for s in open('9.txt'):
    M = sorted([int(x) for x in s.split()])
    if len([x for x in M if M.count(x) == 2]) == 4:
        if M.count(max(M)) == 1:
            if (M[0] * M[-1]) > sum(M[1:-1]):
                print(sum(M))
                exit()
'''


# № 10026 (Уровень: Средний)
# (С. Чайкин) Откройте файл электронной таблицы, содержащей в
# каждой строке пять натуральных чисел.
# Определите сумму номеров строк таблицы, для чисел которой выполнено хотя бы одно условие:
# – числа в строке расположены в порядке возрастания;
# – в строке есть повторяющиеся числа.
'''
num = 1
R = []
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    if len(set(M)) != len(M) or M[0] < M[1] < M[2] < M[3] < M[4]:
        R.append(num)
    num += 1
print(sum(R))
'''


# № 9062 Danov2306 (Уровень: Средний)
# (А.Богданов) В файле электронной таблицы в каждой строке записаны 4 натуральных числа.
# Определите количество строк таблицы, содержащих числа, для которых выполнены следующие условия:
# – в строке первое и последнее число не являются минимальным и максимальным числом строки;
# – разность максимального и минимального числа кратна разности оставшейся пары чисел.
'''
cnt = 0
for s in open('9.txt'):
    M = [int(x) for x in s.split()]
    # if M[0] not in [max(M), min(M)] and M[-1] not in [max(M), min(M)]:
    if all(x not in [max(M), min(M)] for x in [M[0], M[-1]]):
        M = sorted(M)  # M.sort()
        try:
            if (M[-1] - M[0]) % (M[-2] - M[1]) ==  0:
                cnt += 1
        except Exception as e:
            print(M, e)
print(cnt)
'''


# Тип 16 №60258
# Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:
# F(n)  =  n при n > 2024;
# F(n)=n·F(n+1), если n ≤ 2024.
#
# Чему равно значение выражения F(2022) / F(2024)?
'''
import sys 
sys.setrecursionlimit(10000)

def F(n):
    if n > 2024:
        return n
    if n <= 2024:
        return n * F(n + 1)


print(F(2022) / F(2024))
'''


from functools import *

@lru_cache(None)
def f(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return 2 * f(n-2) - f(n-1) + 2
    if n > 2 and n % 2 != 0:
        return 2 * f(n-1) + f(n-2) - 2

print(f(170))



# endregion Урок: ************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Максим = [2.1, 6.1, 5.1, 8.1, 9.1, 12.1, 14.1, 15.1, 16.1, 23.1, 25.1]
# КЕГЭ = []
# на следующем уроке:
