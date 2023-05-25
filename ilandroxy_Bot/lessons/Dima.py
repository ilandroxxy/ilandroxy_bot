
# region Домашка: ******************************************************************************



# endregion Домашка: ******************************************************************************


# region Урок: ******************************************************************************

'''
count = 0
for s in open('9.txt'):
    m = [int(i) for i in s.split()]
    if len(m) == len(set(m)):
        m = sorted(m)
        if 3 * (m[0] + m[4]) >= 2 * (m[1] + m[2] + m[3]):
            count += 1
print(count)
'''
'''
count = 0
mx_s = 0
m = [int(i) for i in open('17.txt')]
n = [x for x in m if len(str(x)) == 3 and abs(x) % 10 == 5]
for i in range(len(m)-1):
    if len(str(m[i])) == 3 or len(str(m[i+1])) == 3:
        if (m[i] + m[i+1]) % min(n) == 0:
            count += 1
            mx_s = max(mx_s, m[i] + m[i+1])
print(count, mx_s)
'''
'''
s = 'NN OO PP NO ON PO OP NP PN'.split()
m = open('24.txt').readline()
for x in s:
    m = m.replace(x, '* *')
n = [len(i) for i in m.split()]
print(max(n))
'''


'''
count = 0
mx_s = 0
s = open('26.txt')
m = [int(i) for i in s]
for i in m:
    for j in m:
        if i > j:
            if i % 2 != 0 and j % 2 != 0:
                if (i + j) // 2 in m:
                    count += 1
                    mx_s = max(mx_s, (i + j) / 2)
                    print(count, mx_s)
'''

# endregion Урок: ******************************************************************************


# todo:    Дмитрий   = [1, 2, 3, 4, 5+, 6, 7, 8+, 9.1, 11, 12, 13, 14+, 15+, 16+, 17, 18, 19-21, 22, 23, 24, 25.2]
# todo: Дмитрий КЕГЭ = [5, 14, 16, 25]
# на прошлом уроке: Прорешиваи .txt задачи с демоверсии варианта от 17.05 числа. Затронули 26 номера. И Повторили 18 номерс Ладьей.
# на следующем уроке:
