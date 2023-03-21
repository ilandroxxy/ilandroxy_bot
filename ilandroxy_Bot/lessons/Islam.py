# region Домашка:  ******************************************************************************


# endregion Домашка: ******************************************************************************


# region Урок:  ******************************************************************************

# ((x → w) ∧ (¬ y → z)) → ((z ≡ x) ∨ (w ∧ ¬ y)).

# y → z  ---> y <= z  ---> ¬ y ∨ z
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                # F = ((x <= w) and (y or z)) <= ((z == x) or (w and (not y)))
                F = ((x <= w) and ((not y) <= z)) <= ((z == x) or (w and (not y)))
                if F == False:
                    print(x, y, z, w)
                        # 0  0  1  0
                        # 0  1  1  0
                        # 0  1  1  1
                        # 1  1  0  1
'''



# Автомат обрабатывает натуральное число N по следующему алгоритму.
# 1. Строится двоичная запись числа N.
# 2. Все значащие цифры инвертируются (‘0’ заменяется на ‘1’, а ‘1’ на ‘0’).
# 3. К полученному результату слева добавляется ‘1’.
# 4. К двоичной записи полученного числа справа дописывается бит
# четности: ‘1’, если количество единиц в двоичной записи нечетно,‘0’ - если четно.
# 5. Полученное в результате этих операций число переводится в десятичную систему счисления.
# Полученная таким образом запись является результатом работы алгоритма: R.

# Укажите такое наименьшее число N, для которого результат работы данного
# алгоритма больше числа 180. В ответе это число запишите в десятичной системе счисления.
'''
for n in range(1, 10000):
    s = bin(n)[2:]  # 1
    s = s.replace('1', '*').replace('0', '1').replace('*', '0') # 2
    s = '1' + s  # 3
    if s.count('1') % 2 == 0:    # 4
        s = s + '0'
    else:
        s = s + '1'
    r = int(s, 2)  # 5
    if r > 180:
        print(n)
        break
'''
# Ответ: 32


# Определите количество пятизначных чисел, записанных в семеричной
# системе счисления, в записи которых:
# 1. только одна цифра 6;
# 2. сумма четных цифр числа меньше суммы нечетных цифр числа.
'''
s = [0, 1, 2, 3, 4, 5, 6]
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    M = [a, b, c, d, e]
                    if M.count(6) == 1 and a != 0:  # только одна цифра 6
                        CHET = [i for i in M if i % 2 == 0]
                        NECHET = [i for i in M if i % 2 != 0]
                        print(f'Весь список: {M}, четные: {CHET}, нечетные: {NECHET}')
                        if sum(CHET) < sum(NECHET):
                            count += 1
print(count)
'''
# Ответ: 1390


# Откройте файл электронной таблицы, содержащей в каждой строке шесть
# натуральных чисел. Определите количество строк таблицы, содержащих
# числа, для которых выполнены оба условия:
# – в строке только одно число повторяется ровно два раза, остальные числа различны;
# – среднее арифметическое неповторяющихся чисел строки не меньше суммы повторяющихся чисел.
# В ответе запишите только число.
'''
count = 0
for s in open('9.txt'):
    # M = s.split()
    # M = [i for i in s.split()]   - аналогичные записи
    M = [int(i) for i in s.split()]
    if len(M) - len(set(M)) == 1:  # в строке только одно число повторяется ровно два раза, остальные числа различны;
        repeat = sum(M) - sum(set(M))
        sred = (sum(set(M)) - repeat) / 4
        if sred >= repeat + repeat:
            count += 1
print(count)
'''
# Ответ: 64

'''
for a in range(100, 0, -1):
    k = 0
    for x in range(1, 1000):
        if ((x % 3 == 0) <= (x % 2 != 0) or (x - a >= 4 )):
            k += 1
    if k == 999:
        print(a)
        break
'''

'''
def F(x):
    return ((x % 3 == 0) <= (x % 2 != 0)) or (x - A >= 4)

for A in range(1, 1000):
    if all(F(x) for x in range(1, 1000)):
        print(A)
'''
# Ответ: 2

'''
for x in '0123456789abc':
    a = int(f'735{x}2', 13)
    b = int(f'2{x}173', 13)

    if (a + b) % 12 == 0:
        print((a + b) // 12)
        break
'''
# Ответ: 22615


'''
M = ['']
import itertools
for t in range(1, 3+1):
    for s in itertools.product('0123456789', repeat=t):
        s = ''.join(s)
        M.append(s)

R = []
for x in range(0, 10):
    for y in M:
        A = int(f'1{x}2139{y}4')
        if A % 3052 == 0:
            R.append([A, A//3052])

for x in sorted(R):
    print(*x)
'''
# Ответ
# 1421398804 465727
# 1521397584 498492
# 1621396364 531257
# 1721395144 564022
# 1821393924 596787
# 1921392704 629552

# Тип 16
print((2*516-3) * (2 * 515 - 3) * (2 * 514-3))
# Ответ: 1083202575


# Тип 23
'''
numbers = set()

def F(a, h):
    if h == 13:
        numbers.add(a)
    else:
        F(a - 3, h + 1)
        F(a * (-3), h + 1)
F(333, 0)

M = [i for i in numbers if i < 0]
print(M)
print(len(M))
'''
# Ответ: 2224

# endregion Урок:  *************************************************************************


# todo: Ислам = [2, 3, 5, 6, 8, 12, 14+, 15, 16, 19-21, 22, 23, 25]
# на прошлом уроке: Разбирали теорию игр 19-21 на 1 и 2 кучи
# на следующем уроке:
