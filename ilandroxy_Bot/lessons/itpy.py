

# todo Разобрать задачку, почему ответы не сходятся
# Тип 17 №59722
# Элементы ряда могут принимать целые значения в диапазоне [−10000; 10000].
# Определите количество троек элементов последовательности, в которой только одно число трехзначное,
# а сумма тройки меньше наибольшего числа, оканчивающегося на 17.
# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
'''
M = [int(x) for x in open('17.txt')]
A = [x for x in M if abs(x) % 100 == 17]
count = 0
for i in range(0, len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    if (len(str(abs(x))) == 3) ^ (len(str(abs(y))) == 3) ^ (len(str(abs(z))) == 3):
        if (x + y + z) < max(A):
            # print(x, y, z, (x + y + z) < max(A))
            count += 1
print(count)


M = [int(x) for x in open('17.txt')]
A = [x for x in M if abs(x) % 100 == 17]
count = 0
for i in range(0, len(M)-2):
    x, y, z = M[i], M[i+1], M[i+2]
    flag1, flag2, flag3 = False, False, False
    if (len(str(abs(x)))) == 3:
        flag1 = True
    if (len(str(abs(y)))) == 3:
        flag2 = True
    if (len(str(abs(z)))) == 3:
        flag3 = True
    if flag1 + flag2 + flag3 == 1:
        if (x + y + z) < max(A):
                # print(x, y, z, (x + y + z) < max(A))
                count += 1
print(count)


l = [int(x) for x in open('17.txt')]
max_dvy = max([x for x in M if abs(x) % 100 == 17])
count = 0
for i in range(len(l) - 2):
    c = 0
    s = [l[i], l[i+1],  l[i+2]]
    for x in s:
        if 99 < abs(x) < 1000:
            c += 1
    if c == 1 and sum(s) < max_dvy:
        count += 1
print(count)
'''


# todo Проверить в чем косяк (правильный ответ 273, а у нас получается 259)
'''
s = open('24.txt').readline()
s =s.replace('D', 'D ').replace('A', ' A')
M = []
for x in s.split():
    if 'A' in x and 'D' in x:
        print(x)
        M.append(x)
print(max([len(x) for x in M]))
'''


# todo придумать как положить сразу два числа в список через генератор
'''
n = int(input())
# divisors = {i for i in range(1, n + 1) if n % i == 0}     # не оптимизированный
divisors = sorted({i for i in range(1, int(n**0.5) + 1) if n % i == 0})
print(divisors)   # 24: {1, 2, 3, 4, 24**0.5,  6, 8, 12, 24}
'''
