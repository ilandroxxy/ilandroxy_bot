
# region Домашка: ******************************************************************************



# endregion Домашка:  ******************************************************************************



# region Урок:  ******************************************************************************

# Тип 18 № 29666
'''
# Дана последовательность вещественных чисел.
# Из неё необходимо выбрать несколько подряд идущих чисел так, чтобы каждое следующее число было меньше предыдущего.
# Какую максимальную сумму могут иметь выбранные числа?

f = open('18.txt', 'r')
M = [float(i) for i in f.read().replace(',', '.').split()]
summ = 0
maxi_summ = 0
for i in range(0, len(M)-1):
    if M[i] > M[i+1]:
        summ += M[i+1]
        maxi_summ = max(maxi_summ, summ)
    else:
        summ = M[i+1]
print(maxi_summ)
'''
# Ответ: 358


# Тип 18 № 33190
'''
# Дана последовательность вещественных чисел. 
# Из неё необходимо выбрать несколько подряд идущих чисел так, чтобы каждое следующее число отличалось от предыдущего не более чем на 10. 
# Какую максимальную сумму могут иметь выбранные числа?

f = open('18.txt', 'r')
M = [float(i) for i in f.read().replace(',', '.').split()]
summ = 0
maxi_summ = 0
for i in range(0, len(M)-1):
    if summ > 0:
        if abs(M[i+1] - M[i]) <= 10:
            summ += M[i+1]
            maxi_summ = max(maxi_summ, summ)
        else:
            summ = M[i+1]
    else:
        summ = M[i+1]
print(round(maxi_summ, 2))
'''
# Ответ: 80



# (№ 5438) (А. Сардарян)

# На вход алгоритма подаётся два натуральных числа N и M. Алгоритм строит по ним новое число R следующим образом.
# 1) Вычисляется произведение P1 всех ненулевых чётных цифр чисел N и M.
# 2) Вычисляется произведение P2 всех нечётных цифр чисел N и M.
# 3) Результат R вычисляется как модуль разности P1 и P2.
# Например, для N = 256 и M = 108 получаем P1 = 2·6·8 = 96 и P2 = 5·1 = 5, так что R = |96 - 5|= 91.
# Укажите минимальное число M, при котором для N = 120 получается R = 29.

'''
for M in range(1, 1000):
    for N in range(120, 120+1):
        n = [int(i) for i in str(N) if int(i) != 0]
        m = [int(i) for i in str(M) if int(i) != 0]
        p1 = 1
        p2 = 1
        for x in n:
            if x % 2 == 0:
                p1 *= x
            else:
                p2 *= x
        for y in m:
            if y % 2 == 0:
                p1 *= y
            else:
                p2 *= y
        r = abs(p1 - p2)
        
        if r == 29:
            print(M)
            exit()
'''

'''
def F(M):
    r = 1
    for x in M:
        r *= x
    return r

for M in range(1, 1000):
    n1 = [int(i) for i in str(120) if int(i) != 0 and int(i) % 2 == 0]
    m1 = [int(i) for i in str(M) if int(i) != 0 and int(i) % 2 == 0]

    n2 = [int(i) for i in str(120) if int(i) != 0 and int(i) % 2 != 0 ]
    m2 = [int(i) for i in str(M) if int(i) != 0 and int(i) % 2 != 0]
    p1, p2 = 1, 1

    p1 = F(n1) * F(m1)
    p2 = F(n2) * F(m2)

    r = abs(p1 - p2)
    if r == 29:
        print(M)
        break
'''
# Ответ: 238



# (№ 3525) (Е. Джобс)

# Автомат обрабатывает десятичное натуральное число N по следующему алгоритму:
# 1) Строится двоично-десятичное представление: каждый разряд десятичного числа кодируется с помощью 4 битов,
# затем полученные коды записываются друг за другом с сохранением незначащих нулей.
# 2) Полученная двоичная последовательность инвертируется – все нули меняются на единицы, а все единицы на нули.
# 3) Полученное в результате этих операций число переводится в десятичную систему счисления.
# Пример. Дано число 13. Оно преобразуется следующим образом:
# 13 → 00010011ДД → 111011002 → 236.
# Здесь нижний индекс «ДД» обозначает двоично-десятичную систему.
# Укажите число N, в результате обработки которого с помощью этого алгоритма получается число 151.

'''
def F(x):
    s = bin(x)[2:]
    while len(s) < 4:  # 1
        s = '0' + s
    return s

for n in range(1, 1000):
    M = [int(i) for i in str(n)]  # 1
    s = ''
    for x in M:
        s += F(x)

    s = s.replace('1', '*')
    s = s.replace('0', '1')  # 2
    s = s.replace('*', '0')

    r = int(s, 2)  # 3

    if r == 151:
        print(n)
'''
# Ответ: 68


# (№ 3524) (Е. Джобс)

# Автомат обрабатывает десятичное натуральное число N по следующему алгоритму:
# 1) В шестеричной записи числа N дублируется последняя цифра.
# 2) Получившееся число переводится в двоичное представление.
# 3) В получившейся записи дублируется последняя цифра.
# 4) Полученное в результате этих операций число переводится в десятичную систему счисления.
# Пример. Дано число 13. Оно преобразуется следующим образом:
# 13 → 21_6 → 211_6 → 1001111_2 → 100111112 → 159.
# Укажите максимальное число, меньшее 344, которое может являться результатом выполнения алгоритма.

# Вариант 1
'''
for n in range(13, 14):
    M = []
    while n > 0:
        M.append(n % 6)
        n //= 6
    M.reverse()
    print(M)

    M.append(M[-1])
    print(M)

    x = ''.join(map(str, M))
    x = int(x, 6)
    f = bin(x)[2:]
    print(f)
    f = f + f[-1]
    print(f)

    r = int(f, 2)
    print(r)
    if r < 344:
        print(r)
'''

# Вариант 2
'''
def systems(m, n):
    alphabet = '0123456789ABCDEF'
    M = []
    while m > 0:
        M.append(alphabet[m % n])
        m //= n
    M.reverse()
    return ''.join(M)

for n in range(1000-1, -1, -1):
    m = systems(n, 6)
    m = m + m[-1]

    x = int(m, 6)

    f = systems(x, 2)

    f = f + f[-1]

    r = int(f, 2)

    if r < 344:
        print(r)
        break
'''
# Ответ: 331




# endregion Урок:  ******************************************************************************

# Слава
# todo: РЕШУ ЕГЭ = [1, 2, 5, 6, 8, 9, 12, 13, 14+, 15+, 16, 17, 18, 19, 20, 21, 23, 24+, 25.2]
# todo: КЕГЭ [1, 5, 8, 13]
# на прошлом уроке: Прорешали 3 номер через функцию ВПР, начали разбирать 22 - разобрали простейшие с РЕШУ ЕГЭ
# на следующем уроке:
# рассмотреть: 6, 9, 22, 17 КЕГЭ