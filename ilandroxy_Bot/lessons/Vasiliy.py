# region Домашка: ************************************************************

# endregion Домашка: ************************************************************



# region Урок: ************************************************************


# № 5946 (Уровень: Средний)
# Откройте файл электронной таблицы, содержащей в каждой строке шесть натуральных чисел.
# Определите количество строк таблицы, содержащих числа, для которых выполнены оба условия:
#
# – в строке все числа различны;
# – количество чётных чисел превышает количество нечётных чисел.
'''
count = 0
for s in open('9.txt'):
    M = [int(i) for i in s.split()]
    if len(set(M)) == len(M):  # – в строке все числа различны;
        chet = [i for i in M if i % 2 == 0]
        nechet = [i for i in M if i % 2 != 0]
        if len(chet) > len(nechet):
            count += 1
print(count)
'''
# Ответ: 1078


# № 5947 (Уровень: Базовый)

#    ПОКА нашлось(>1) ИЛИ нашлось(>2) ИЛИ нашлось(>3)
#       ЕСЛИ нашлось(>1)
#          ТО заменить(>1, 22>3)
#       ЕСЛИ нашлось(>2)
#          ТО заменить(>2, 2>)
#       ЕСЛИ нашлось(>3)
#          ТО заменить(>3, 11>2)

# На вход приведённой выше программы поступает строка, начинающаяся с символа «>»,
# а затем содержащая n цифр 1, n цифр 2 и n цифр 3 (3 ≤ n ≤ 50), расположенных в произвольном порядке.
# Определите количество значений n, при котором сумма числовых значений цифр строки,
# получившейся в результате выполнения программы кратна 7.
'''
count = 0
for n in range(3, 50+1):
    s = '>' + '1' * n + '2' * n + '3' * n

    while '>1' in s or '>2' in s or '>3' in s:
        if '>1' in s:
            s = s.replace('>1', '22>3', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>3' in s:
            s = s.replace('>3', '11>2', 1)

    # summ = sum([int(i) for i in s if i.isdigit()])
    summ = s.count('1') + s.count('2') * 2 + s.count('3') * 3
    
    if summ % 7 == 0:
        count += 1
print(count)
'''
# Показать ответ: 48


# № 5953 (Уровень: Средний)
# (П. Волгин) Операнды арифметического выражения записаны в системах счисления с основанием 17:
#
# 10x0_17 + F0xFF_17
#
# В записи чисел переменной x обозначена неизвестная цифра из алфавита 17-ричной системы счисления.
# Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 13.
# Для найденного значения x вычислите частное от деления значения арифметического выражения на 13
# и укажите его в ответе в десятичной системе счисления. Основание системы счисления в ответе указывать не нужно.
'''
ALPHABET = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')

for x in ALPHABET[:17]:
    A = int(f'10{x}0', 17)
    B = int(f'F0{x}FF', 17)
    if (A + B) % 13 == 0:
        print((A + B) // 13)
'''
# Показать ответ: 97028


# № 4986 (Уровень: Базовый)
# Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m»;
# и пусть на числовой прямой дан отрезок B = [50; 70].
# Для какого наибольшего натурального числа А формула
# ДЕЛ(x, A) ∨ (ДЕЛ(x, 23) → ¬(x ∈ B))
# тождественно истинна (т.е. принимает значение 1) при любом натуральном значении переменной х?
'''
def F(x, A):
    # B = x in [i for i in range(50, 70+1)]
    B = 50 <= x <= 70
    return (x % A == 0) or ((x % 23 == 0) <= (not B))

for A in range(1, 10000):
    if all(F(x, A) for x in range(1, 1000)):
        print(A)
'''
'''
def DEL(n, m):
    if n % m == 0:
        return True
    else:
        return False


B = [int(i) for i in range(50, 71)]

for A in range(10000, 1, -1):
    if all((DEL(x, A) or (DEL(x, 23) <= (not(x in B)))) for x in range(1, 10001)):
        print(A)
        break
'''
# Показать ответ: 69



# № 2491 (Уровень: Базовый)
# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно.
# Определите количество троек, в которых хотя бы один из трёх элементов меньше,
# чем среднее арифметическое всех чисел в файле, и десятичная запись всех трёх элементов тройки содержит цифру 9.
# В ответе запишите два числа: сначала количество найденных троек, а затем – максимальную сумму элементов таких троек.
# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
'''
M = [int(i) for i in open('17.txt')]
sred = sum(M) / len(M)  # среднее арифметическое всех чисел в файле
count = 0
maxi = 0
for i in range(0, len(M)-2):
    if M[i] < sred or M[i+1] < sred or M[i+2] < sred:
        if '9' in str(M[i]) and '9' in str(M[i+1]) and '9' in str(M[i+2]):
            count += 1
            maxi = max(maxi, M[i] + M[i+1] + M[i+2])
print(count, maxi)
'''
# Ответ: 345 17460


# № 5835 (Уровень: Базовый)
# (Д. Статный) Исполнитель Калькулятор преобразует число, записанное на экране.
# У исполнителя есть три команды, которым присвоены номера:
#
# А. Прибавить 3.
# Б. Прибавить 1.
# С. Умножить на 3.

# Сколько существует таких программ, которые исходное число 1 преобразуют в число 333,
# и при этом 3 последние команды – A, C, C?
'''
def F(a, b, h: str):
    if a > b:
        return 0
    elif a == b:
        if h[-3:] == 'ACC':
            return 1
        else:
            return 0
    else:
        return F(a+3, b, h+'A') + F(a+1, b, h+'B') + F(a*3, b, h+'C')

print(F(1, 333, ''))
'''
# Показать ответ: 329312




# endregion Урок: ************************************************************




# todo:   Василий    = [1, 2, 3, 4, 5, 6, 8, 9, 11, 12, 14+, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# todo: Василий КЕГЭ = [25]
# на прошлом уроке: Закрыли задачи с Джобс варианта, номера: 9,12,14,15,17,23
# на следующем уроке:
