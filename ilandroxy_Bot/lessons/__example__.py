'''
text = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
s = [i for i in text. split()]
base = {}
for i in s:
    base[i] = base.get(i, 0) + 1
print(base)

for i in base:
    if base[i] == max(base.values()):
        base[i] = base[i]

res = sorted(base)
print(res)
result = {0: res[0]}
print(result)
'''
import random
import zipimport

'''


MondayStudents = {683943897: "Tanya.py", 811476623: "Georgie.py", 826004697: 'Nikita.py'}
TuesdayStudents = {1949653479: "Yanina.py", 1208542295: "Sasha.py", 1537718492: "Aleksandr.py"}
ThursdayStudents = {1949653479: "Yanina.py", 1477701439: "Valeria.py", 811476623: "Georgie.py", 799740089: "Bulat.py", 1537718492: "Aleksandr.py"}
FridayStudents = {1314375732: "Vasiliy.py", 644645774: "Stasya.py", 719571990: "Stepan.py", 1029532016: 'Maria.py'}
SaturdayStudents = {871237277: "Vladek.py"}

Students = MondayStudents | ThursdayStudents | ThursdayStudents | FridayStudents | SaturdayStudents
print(Students)

for i in Students:
    print(type(i))

print(Students[1029532016])
'''











# Тип 15 № 34506
'''
# Обозначим через m&n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Так, например, 14&5 = 1110_2 & 0101_2 = 01002 = 4.
#
# Для какого наименьшего неотрицательного целого числа А формула
#
# x&25 ≠ 0 → (x&17 = 0 → x&А ≠ 0)
#
#
# тождественно истинна (т. е. принимает значение 1 при любом неотрицательном целом значении переменной х)?

def Conc(x, y):
    X = []
    while x > 0:
        X.append(x % 2)
        x //= 2
    X.reverse()

    Y = []
    while y > 0:
        Y.append(y % 2)
        y //= 2
    Y.reverse()

    while len(X) != len(Y):
        if len(X) < len(Y):
            X.reverse()
            X.append(0)
            X.reverse()
        else:
            Y.reverse()
            Y.append(0)
            Y.reverse()

    M = []
    for i in range(0, len(X)):
        if X[i] == 1 and Y[i] == 1:
            M.append(1)
        else:
            M.append(0)

    M.reverse()
    summ = 0
    for i in range(0, len(M)):
        summ += M[i] * 2 ** i

    return summ


def F(A, x):
    return (Conc(x, 25) != 0) <= ((Conc(x, 17) == 0) <= (Conc(x, A) != 0))


M = []
for A in range(0, 1000):
    flag = True
    for x in range(0, 100):
        if F(A, x) == False:
            flag = False
            break
    if flag == True:
        M.append(A)
print(min(M))
'''
# Ответ: 8





# Тип 24 № 36879
'''
# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт.
# Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
#
# В строках, содержащих менее 25 букв G, нужно определить и вывести максимальное расстояние между
# одинаковыми буквами в одной строке.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.


f = open('24.txt', 'r')
s = f.readlines()
alphabet = 'QWERTYUIOPASDFGHJKLZXCVBNM'
M = []

for strings in s:
    maxi = 0
    if strings.count('G') < 25:
        # print(strings.count('G'), strings)
        for i in alphabet:
            if maxi < strings.rindex(i) - strings.index(i):
                maxi = strings.rindex(i) - strings.index(i)
        M.append(maxi)
print(max(M))
'''
# Ответ: 1001




# Тип 15 № 9699
'''
# На числовой прямой даны два отрезка: P = [4, 15] и Q = [12, 20].
#
# Укажите наименьшую возможную длину отрезка A, для которого выражение
#
# ((x ∈ P) ∧ (x ∈ Q)) → (x ∈ A)
#
# тождественно истинно, то есть принимает значение 1 при любом значении переменной х.

def F(a1, a2, x):
    return ((4 <= x <= 15) and (12 <= x <= 20)) <= (a1 <= x <= a2)

M = []
for a1 in range(1, 100):
    for a2 in range(1, 100):
        flag = True
        for x in range(1, 100):
            if F(a1,a2,x) == False:
                flag = False
                break
        if flag == True:
            M.append(a2-a1)

print(min(M))
'''
# Ответ 3

'''
try:
    print(5 / 0)
except ZeroDivisionError:
    print("На ноль делить нельзя")

x = 4
NumberForSimple = 4
sumь = x + NumberForSimple
'''


# Тип 25 № 27856
'''
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [95632;95650], числа,
# имеющие ровно шесть различных нечётных натуральных делителей (при этом количество четных делителей может быть любым).
# Для каждого найденного числа запишите эти шесть делителей в шесть соседних столбцов на экране с новой строки.
# Делители в строке должны следовать в порядке возрастания.
#
# Например, в диапазоне [2;48] ровно шесть нечётных различных натуральных делителей имеет число 45, поэтому для этого
# диапазона вывод на экране должна содержать следующие значения: 1 3 5 9 15 45;
#
# в диапазоне [480;489] ровно шесть нечётных различных натуральных делителей имеет число 486, поэтому для этого
# диапазона вывод на экране должна содержать следующие значения: 1 3 9 27 81 243.

for number in range(95632, 95650+1):
    KolDel = 0
    Del = []
    for i in range(1, number+1):
        if number % i == 0 and i % 2 != 0:
            KolDel += 1
            Del.append(i)
    if KolDel == 6:
        print(Del)
'''
# Ответ:
# [1, 3, 9, 10627, 31881, 95643]
# [1, 7, 49, 61, 427, 2989]
# [1, 5, 25, 1913, 9565, 47825]



# Тип 14 № 18444
'''
# Сколько единиц содержится в двоичной записи значения выражения: 4**16 + 2**36 - 8?
x = 4**16 + 2**36 - 8
M = []
while x > 0:
    M.append(x % 2)
    x //= 2
M.reverse()
print(M, M.count(1))
'''
# Ответ: 30



# Тип 24 № 27686
'''
# Текстовый файл состоит не более чем из 10**6 символов X, Y и Z.
# Определите длину самой длинной последовательности, состоящей из символов X. Хотя бы один символ X находится в последовательности.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

f = open('24.txt', 'r')
s = f.readline()

count = 1
Maxcount = 0
for i in range(0, len(s)-1):
    if s[i] == 'X' and s[i+1] == 'X':
        count += 1
        if Maxcount < count:
            Maxcount = count
    else:
        count = 1
print(Maxcount)
'''
# Ответ: 19




'''

weather = 'облачно'
temperature = 24
# Привет, сегодня облачно, но жарко, температура 24
print('Привет, сегодня', weather, ', но жарко, температура', temperature)
print('Привет, сегодня ' + weather + ', но жарко, температура ' + str(temperature))
print('Привет, сегодня {}, но жарко, температура {}'.format(weather, temperature))
print('Привет, сегодня %s, но жарко, температура %d'%(weather, temperature))
print(f'Привет, сегодня {weather}, но жарко, температура {temperature}')
'''

'''
N = [0,0,0,1,0,1,0,1]
while N[0] == 0:
    del N[0]
print(N)
'''

'''
*!*!*?
3
а: 3
н: 2
с: 1
'''

# ПИНЧУК ЕГОР ПЕТРОВИЧ	2.9.1994	ОБЛ. НОВОСИБИРСКАЯ, Г. НОВОСИБИРСК, ПЕР. САДОВЫЙ, ДОМ 3	5014316390	ОУФМС РОССИИ ПО НОВОСИБИРСКОЙ ОБЛ. В СОВЕТСКОМ Р-НЕ
'''
f = open('Priziv1volna.txt', 'r')
s = f.readlines()
print(len(s))


for i in s:
    if 'ОБЛ. НОВОСИБИРСКАЯ, Г. НОВОСИБИРСК' in i:
        if 'БАБЕШКО' in i:
            print(i)
        #if 'ОУФМС РОССИИ ПО НОВОСИБИРСКОЙ ОБЛ. В СОВЕТСКОМ Р-НЕ' in i:
            #print(i)
'''

'''
student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]



result = []


for i in range(0, len(student_names)):
    M = {}
    temp = {}
    temp[student_names[i]] = student_grades[i]
    M[student_ids[i]] = temp
    result.append(M)
print(result)
'''


# Тип 25 № 27851
'''
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [210235;210300], числа,
# имеющие ровно четыре различных натуральных делителя, не считая единицы и самого числа.
# Для каждого найденного числа запишите эти четыре делителя в четыре соседних столбца на экране с новой строки.
# Делители в строке должны следовать в порядке возрастания.
#
# Например, в диапазоне [10;16] ровно четыре различных натуральных делителя имеет число 12,
# поэтому для этого диапазона вывод на экране должна содержать следующие значения:
#
# 2 3 4 6


for number in range(210235, 210300+1):
    KolDel = 0
    M = []
    for i in range(2, number):
        if number % i == 0:
            KolDel += 1
            M.append(i)
    if KolDel == 4:
        print(*M)
'''
# Ответ:
# 2 4 52561 105122
# 2 4 52567 105134
# 2 4 52571 105142



# Sample Input 1:
#
# 5
# my_pycode.exe W X
# log_n X W R
# ave R
# lucky_m W R
# dnsss.py W
# 6
# execute ave
# read dnsss.py
# write log_n
# execute log_n
# read ave
# write my_pycode.exe
# Sample Output 1:
#
# Access denied
# Access denied
# OK
# OK
# OK
# OK



# Тип 25 № 27422
'''
# Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [174457;174505], числа, имеющие ровно
# два различных натуральных делителя, не считая единицы и самого числа.
# Для каждого найденного числа запишите эти два делителя в два соседних столбца на экране с новой строки в порядке
# возрастания произведения этих двух делителей. Делители в строке также должны следовать в порядке возрастания.
#
# Например, в диапазоне [5;9] ровно два различных натуральных делителя имеют числа 6 и 8,
# поэтому для этого диапазона вывод на экране должна содержать следующие значения:
# 2 3
# 2 4


for number in range(174457, 174505+1):
    KolDel = 0
    M = []
    for i in range(2, number):
        if number % i == 0:
            KolDel += 1
            M.append(i)
    if KolDel == 2:  #  два различных натуральных делителя, не считая единицы и самого числа.
        print(*M)
'''
# Ответ:
# 3 58153
# 7 24923
# 59 2957
# 13 13421
# 149 1171
# 5 34897
# 211 827
# 2 87251


# Тип 16 № 6779
'''
# Алгоритм вычисления значений функций F(n) и G(n), где n — натуральное число, задан следующими соотношениями:
#
# F(1) = 1;
# G(1) = 1;
# F(n) = F(n – 1) – G(n – 1)
# G(n) = F(n–1) + G(n – 1), при n ≥ 2
#
# Чему равно значение величины F(5)/G(5)?
# В ответе запишите только натуральное число.

def F(n):
    if n == 1:
        return 1
    if n >= 2:
        return F(n - 1) - G(n - 1)

def G(n):
    if n == 1:
        return 1
    if n >= 2:
        return F(n - 1) + G(n - 1)

x = F(5) / G(5)
print(x)
'''



# Дана программа для Редактора:
#
# НАЧАЛО
# ПОКА нашлось (21)
#     заменить (21, 5)
# КОНЕЦ ПОКА
# КОНЕЦ
#
# Исходная строка содержит десять единиц и некоторое количество двоек,
# других цифр нет, точный порядок расположения единиц и двоек неизвестен.
# После выполнения программы получилась строка с суммой цифр 34.
# Какое наименьшее количество двоек могло быть в исходной строке?
'''
3
Светлана Зуева
Аркадий Белых
Борис Боков
'''

'''
import random

n = int(input())

M = []
for i in range(n):
    s = input()
    M.append(s)

N = M.copy()
#print(M)
for i in range(n):
    n1 = random.choice(M)
    n2 = random.choice(N)
    while n1 == n2:
        n1 = random.choice(M)
        n2 = random.choice(N)

    for i in range(len(M)):
        if M[i] == n1:
            del M[i]
            break

    res = n1 + ' - ' + n2
    print(res)
'''

"""
Students = {1208542295: ['Sasha.py', 3200/2],
            799740089: ["Bulat.py", 2280],
            811476623: ["Georgie.py", 3040],  # 2
            1949653479: ['Yanina.py', 4080],  # 2
            826004697: ['Nikita.py', 3040],
            1537718492: ['Aleksandr.py', 5760], # 2
            1314375732: ['Vasiliy.py', 6800/2],
            683943897: ["Tanya.py", 3600],
            871237277: ['Vladek.py', 6800/2],
            1477701439: ["Valeria.py", 3200],
            644645774: ['Stasya.py', 5760/2],
            719571990: ['Stepan.py', 6800/2],
            1029532016: ['Maria.py', 3600],
            1649389148: ['Slava.py', 6800/2],
            789322200: ['Katya.py', 6800/2],
            824782347: ['Daniel', 3600],
            804184353: ['Islam.py', 3600],
            5148819382: ['Tatyana.py', 3600],
            1000000001: ['_______.py', 3600],
            1000000002: ['_______.py', 3600],
            1000000003: ['_______.py', 3600],
            1000000004: ['_______.py', 3600],
            1000000005: ['_______.py', 3600],
            1000000006: ['_______.py', 3600],
            1000000007: ['_______.py', 3600],
            1000000008: ['_______.py', 3600],
            1000000009: ['_______.py', 3600],
            1000000010: ['_______.py', 3600],
            1000000011: ['_______.py', 3600],
            1000000012: ['_______.py', 3600],
            1000000013: ['_______.py', 3600],
            1000000014: ['_______.py', 3600],
            1000000015: ['_______.py', 3600],
            1000000016: ['_______.py', 3600]}


n = len(Students)+3
summ1 = 0
summ2 = 0
for key in Students:
    if Students[key][0] != '_______.py':
        summ1 += Students[key][1]
    summ2 += Students[key][1]
print(summ1, summ2)


print(8*5*3600, 8*5-n)
print(7*5*3600, 7*5-n)
print(6*5*3600, 6*5-n)
"""


'''
import random
import string

n, m = int(input()), int(input())

def generate_password(length):

    flag1 = False
    flag2 = False
    flag3 = False

    numbers = '23456789'
    n = [i for i in numbers]
    letters = 'abcdefghjkmnpqrstuvwxyz'
    l = [i for i in letters]
    LETTERS = 'ABCDEFGHJKMNPQRSTUVWXYZ'
    L = [i for i in LETTERS]

    BadSymbols = 'iIlL0oO1'
    password = ''

    while len(password) != length:
        x = random.randint(1,3)
        if x == 1:
            flag1 = True
            password += random.choice(n)
        if x == 2:
            flag2 = True
            password += random.choice(l)
        if x == 3:
            flag3 = True
            password += random.choice(L)

    if flag1 == True and flag2 == True and flag3 == True:
        print(password)
    else:
        generate_password(length)


def generate_passwords(count, length):
    for i in range(count):
        generate_password(length)

generate_passwords(n, m)
'''

MondayStudents = {811476623: ["Georgie.py", '20:00'], 826004697: ['Nikita.py', '22:00']}

print(f"{MondayStudents[826004697][0]} время урока: {MondayStudents[826004697][1]}")

Students = {}
M = [1,2,3,4 ]
Students[int(M[1])] = [M[2], M[3]]
print(Students)





