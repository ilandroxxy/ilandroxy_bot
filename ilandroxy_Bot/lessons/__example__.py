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


NumberFroSimple = 0
import math

M = []
M.append(4)
print(M)

print(NumberFroSimple)










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
type = '1'
task = 34523
name = 'ilya'
user = 124142
print(f"#" + name + f": tg://user?id={user} \nполучил домашку: (" + type + ") " + str(task))
print(f"#{name}: tg://user?id={user} \nполучил домашку: ({type}) {M[x]}")












