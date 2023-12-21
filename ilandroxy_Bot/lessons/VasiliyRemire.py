
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************


# todo Разобраться почему три варианта решения 17, 18, 19

'''
s = open('24.txt').readline()
s = s.replace('B', 'A').replace('C', 'A').replace('9', '8')

while 'AA' in s: s = s.replace('AA', 'A A')
while '88' in s: s = s.replace('88', '8 8')
print(max(len(x) for x in s.split()))
'''
'''
s = open('24.txt').readline().upper()
s = s.replace('TXA', '***').replace('XY', '**').replace('XA', '**')
for a in set(s):
    if a != '*':
        s = s.replace(a, ' ')

print(max([len(x) for x in s.split()]))
'''
'''
# Чтение строки из файла '24.txt' и приведение её к верхнему регистру.
s = open('24.txt').readline().upper()

# Замена определенных подстрок в строке.
s = s.replace('TXA', '***').replace('XY', '**').replace('XA', '**')

# Замена всех символов, кроме '*', на пробел.
s = ''.join([' ' if a != '*' else '*' for a in s])

# Вывод максимальной длины слова после разделения строки.
print(max([len(x) for x in s.split()]))
'''


# Тип 25 №27855
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [95632; 95700],
# числа, имеющие ровно шесть различных чётных натуральных делителей
# (при этом количество нечётных делителей может быть любым).
# Для каждого найденного числа запишите эти шесть делителей в шесть соседних столбцов на экране с новой строки.
# Делители в строке должны следовать в порядке возрастания.
'''
def divisors(num):
    div = set()
    for j in range(1, int(num**0.5)+1):
        if num % j == 0:
            if j % 2 == 0:
                div.add(j)
            if (num // j) % 2 == 0:
                div.add(num // j)
    return sorted(div)


for n in range(95632, 95700+1):
    d = divisors(n)
    if len(d) == 6:
        print(*d)
'''
# Ответ:
# 2 10 50 3826 19130 95650
# 2 26 338 566 7358 95654
# 2 4 8 23918 47836 95672

# from time import time
# start = time()

'''
def divisors(num):
    div = []
    for j in range(1, num+1):
        if num % j == 0:
            div.append(j)
    return div


print(divisors(100_000_000))

end = time() - start
print(end)  # 0.29619503021240234
'''

'''
def divisors(num):
    div = set()
    for j in range(1, int(num**0.5)+1):
        if num % j == 0:
            div.add(j)
            div.add(num // j)
    return sorted(div)


print(divisors(100_000_000))


end = time() - start
print(end)  # 0.00033092498779296875


print(divisors(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(24 / 4)  # 6.0
print(24 / 6)  # 4.0
print(divisors(16))  # [1, 2, 4, 8, 16]
'''




# endregion Урок: ******************************************************************


# Василий = [2.1, 5.1, 6.1, 8.1, 12.1, 14.1, 15.1, 16.1, 17.1, 23.1, 24.1]
# КЕГЭ  = []
# на следующем уроке:
