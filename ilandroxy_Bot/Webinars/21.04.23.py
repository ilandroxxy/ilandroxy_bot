
#
# № 7717 (Уровень: Сложный)
# (Н. Сафронов) В файле содержится последовательность целых неотрицательных чисел, не превышающих 10000.
# Определите количество пар элементов последовательности, в которых все цифры первого элемента
# в паре больше всех цифр второго элемента в паре (первый элемент – крайний левый элемент в паре),
# а сумма текущей пары не больше максимального элемента последовательности,
# запись которого содержит одинаковое количество четных и нечетных цифр.

# В ответе запишите два числа: сначала количество найденных пар,
# затем максимальную сумму элементов этих пар. В данной задаче под
# парой подразумевается два идущих подряд элемента последовательности.
'''
# Вариант 1
M = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
for i in range(0, len(M)-1):
    A = sorted([int(i) for i in str(M[i])])  # M[i]
    B = sorted([int(i) for i in str(M[i+1])])  # M[i+1]
    if min(A) > max(B):
        if (M[i] + M[i+1]) <= max(M):
            # print(A, B)
            count += 1
            maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)

# Вариант 2
M = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
for i in range(0, len(M)-1):
    A = sorted([int(i) for i in str(M[i])])  # M[i]
    B = sorted([int(i) for i in str(M[i+1])])  # M[i+1]
    if all(a > b for a in A for b in B):
        if (M[i] + M[i+1]) <= max(M):
            count += 1
            maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)


# Вариант 3
M = [int(i) for i in open('17.txt')]
count = 0
maxi = 0
for i in range(0, len(M)-1):
    if all(a > b for a in str(M[i]) for b in str(M[i+1])):
        if (M[i] + M[i+1]) <= max(M):
            count += 1
            maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)
'''
# Ответ: 11 9881


# № 7716 (Уровень: Средний)
# (Н. Сафронов) В файле содержится последовательность целых неотрицательных чисел, не превышающих 10000.
# Определите количество пар элементов последовательности, в которых запись хотя бы одного элемента из двух состоит
# только из четных цифр, а сумма текущей пары больше максимального элемента последовательности,
# состоящего только из нечетных цифр. В ответе запишите два числа: сначала количество найденных пар,
# затем максимальную сумму элементов этих пар. В данной задаче под парой подразумевается
# два идущих подряд элемента последовательности.
'''
M = [int(i) for i in open('17.txt')]
A = [i for i in M if all(int(x) % 2 != 0 for x in str(i))]
print(A)
count = 0
maxi = 0
for x in range(0, len(M)-1):
    # if all(int(i) % 2 == 0 for i in str(M[x])) or all(int(i) % 2 == 0 for i in str(M[x+1])):
    # if any(int(i) % 2 != 0 for i in str(M[x])) == False or any(int(i) % 2 != 0 for i in str(M[x + 1])) == False:
    if (len([int(i) for i in str(M[x]) if int(i) % 2 == 0]) == len(str(M[x]))) or (len([int(i) for i in str(M[x+1]) if int(i) % 2 == 0]) == len(str(M[x+1]))):
        if (M[x] + M[x+1]) > max(A):
            count += 1
            maxi = max(maxi, M[x] + M[x+1])
print(count, maxi)
'''
# Ответ: 56 18612




# № 7350 (Уровень: Средний)
# (Л. Шастин) Откройте файл электронной таблицы, содержащей в каждой строке три двузначных натуральных числа.
# Определите количество строк таблицы, в которых произведение цифр всех чисел больше суммы всех чисел.
#
# Например, в строке: 15, 22, 36 произведение цифр = 1*5*2*2*3*6, а сумма всех чисел = 15+22+36.
'''
def F(M):
    r = 1
    for x in M:
        r *= x
    return r

count = 0
for s in open('9.txt'):
    A = [int(i) for i in ''.join(s.split())]
    B = [int(i) for i in s.split()]
    if F(A) > sum(B):
        count += 1
print(count)
'''
# Ответ: 3649


# № 6925 (Уровень: Сложный)
# (Д. Статный) Откройте файл электронной таблицы, содержащей в каждой строке шесть неотрицательных целых чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнено только одно из условий:
#
# – в строке только одно число повторяется дважды, а остальные не повторяются;
# – в строке среднее арифметическое чётных чисел отличается от среднего арифметического нечётных чисел более чем на 50.
#
# В ответе запишите только число.
# *Среднее арифметическое для 0 чисел принять равным нулю.
'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]

    chet = [i for i in M if i % 2 == 0]
    nechet = [i for i in M if i % 2 != 0]

    if len(chet) == 0:
        sred_chet = 0
    else:
        sred_chet = sum(chet) / len(chet)

    if len(nechet) == 0:
        sred_nechet = 0
    else:
        sred_nechet = sum(nechet) / len(nechet)

    if (len(set(M)) == len(M) - 1 and abs(sred_chet - sred_nechet) <= 50) or len(set(M)) != len(M) - 1 and abs(sred_chet - sred_nechet) > 50:
        count += 1

print(count)
'''
# Ответ: 862


#
# № 6094 /dev/inf 02.2023 (Уровень: Средний)
# (А. Рогов) Текстовый файл состоит не более чем из 1 200 000 символов X, Y, и Z.
# Определите максимальное количество идущих подряд пар символов вида
# согласная + гласная
#
# среди которых нет подстроки XYZY.
#
# Для выполнения этого задания следует написать программу.
# Примечание. Букву Y считайте всегда гласной.
'''
# s = 'XYXYXYXYXYXYZY'
s = open('24.txt').readline()
s = s.replace('XYZY', '*#')
s = s.replace('XY', '*').replace('ZY', '#')
for x in 'XYZ':
    s = s.replace(x, ' ')
print(s)
print(max(s.split()))
'''
# Ответ: 7


# № 5955 (Уровень: Средний)
# Текстовый файл состоит из символов A, C, D, F и O.
# Определите максимальное количество идущих подряд символов, среди которых нет подстроки вида
#
# согласная + гласная + гласная + согласная
#
# в прилагаемом файле.
#  Для выполнения этого задания следует написать программу.
'''
import itertools
M = []
for s in itertools.product('ACDFO', repeat=4):
    if s[0] in 'CDF' and s[1] in 'AO' and s[2] in 'AO' and s[3] in 'CDF':
        s = ''.join(s)
        M.append(s)
        
s = open('24.txt').readline()
for x in M:
    s = s.replace(x, ' ')
M = [len(i) for i in s.split()]
print(3 + max(M) + 3)
'''
# Ответ: 599

