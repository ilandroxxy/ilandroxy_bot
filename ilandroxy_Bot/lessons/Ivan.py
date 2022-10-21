


# Тип 8 № 3195
# Все 5-буквенные слова, составленные из букв А, К, Р, У, записаны в алфавитном порядке.

# Вот начало списка:
# 1. ААААА
# 2. ААААК
# 3. ААААР
# 4. ААААУ
# 5. АААКА

# Запишите слово, которое стоит на 350-м месте от начала списка.

# вариант 1
'''
s = 'АКРУ'
count = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    #print(count, temp)
                    if count == 350:
                        print(temp)
                    count += 1
'''

# вариант 2
'''
s = 'АКРУ'
M = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    M.append(temp)

print(M[350-1])
'''
# Ответ: К К К У К





# Тип 8 № 40724
'''
# Светлана составляет коды из букв своего имени.
# Код должен состоять из 8 букв, и каждая буква в нём должна встречаться столько же раз, сколько в имени Светлана.
# Кроме того, одинаковые буквы в коде не должны стоять рядом. Сколько кодов может составить Светлана?

s = 'СВЕТЛАНА'

M = []
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        for g in s:
                            for h in s:
                                temp = a + b + c + d + e + f + g + h
                                if 'АА' not in temp and temp.count('С') == 1 and temp.count('В') == 1 and temp.count('Е') == 1 and temp.count('Т') == 1 and temp.count('Л') == 1 and temp.count('Н') == 1 and temp.count('А') == 2:
                                    if temp not in M:
                                        M.append(temp)
print(len(M))
'''



# Тип 8 № 10473
'''
# Шифр кодового замка представляет собой последовательность из пяти символов, каждый из которых является цифрой от 1 до 4.
# Сколько различных вариантов шифра можно задать, если известно, что цифра 1 встречается ровно два раза, а каждая из других
# допустимых цифр может встречаться в шифре любое количество раз или не встречаться совсем?

s = '1234'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if temp.count('1') == 2:
                        count += 1
print(count)
'''


# Тип 8 № 47005
'''
# Светлана составляет коды из букв слова ПАРАБОЛА. Код должен состоять из 8 букв, и каждая буква в нём должна встречаться столько же раз, сколько в заданном слове.
# Кроме того, в коде не должны стоять рядом две гласные и две согласные буквы. Сколько кодов может составить Светлана?

s = "ПАРАБОЛА"
s1 = 'АААО'
s2 = 'ПРБЛ'
M = []
for a in s1:
    for b in s2:
        for c in s1:
            for d in s2:
                for e in s1:
                    for f in s2:
                        for g in s1:
                            for h in s2:
                                temp = a + b + c + d + e + f + g + h
                                if temp.count('П') == 1 and temp.count('Р') == 1 and temp.count(
                                        'Б') == 1 and temp.count('О') == 1 and temp.count('Л') == 1 and temp.count('А') == 3:
                                    if temp not in M:
                                        M.append(temp)
print(len(M) * 2)
'''



# Тип 12 № 15799
'''
# Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 100 единиц?
#
# НАЧАЛО
#     ПОКА нашлось (111)
#         заменить (11, 2)
#         заменить (22, 1)
#     КОНЕЦ ПОКА
# КОНЕЦ


s = '1' * 100
while '111' in s:
    s = s.replace('11', '2', 1)
    s = s.replace('22', '1', 1)
print(s)
'''
# Ответ: 211




# Тип 12 № 33514
'''
# Дана программа для редактора:

# НАЧАЛО
#     ПОКА нашлось (01) ИЛИ нашлось (02) ИЛИ нашлось (03)
#         заменить (01, 30)
#         заменить (02, 101)
#         заменить (03, 202)
#     КОНЕЦ ПОКА
# КОНЕЦ
#

# Известно, что исходная строка начиналась с нуля, а далее содержала только единицы, двойки и тройки.
# После выполнения данной программы получилась строка, содержащая 15 единиц, 10 двоек и 60 троек. Сколько единиц было в исходной строке?

for x in range(1, 50):
    for y in range(1, 50):
        for z in range(1, 50):
            s = '0' + '1' * x + '2' * y + '3' * z
            temp = s
            while '01' in s or '02' in s or '03' in s:
                s = s.replace('01', '30', 1)
                s = s.replace('02', '101', 1)
                s = s.replace('03', '202', 1)
            if s.count('1') == 15 and s.count('2') == 10 and s.count('3') == 60:
                print(temp.count('1'))
'''



# Тип 14 № 39243
'''
# Значение выражения 4**34 + 5*4**22 + 4**13 + 2*4**9 + 82 записали в системе счисления с основанием 16.
# Сколько разных цифр встречается в этой записи?

x = 4**34 + 5*4**22 + 4**13 + 2*4**9 + 82
M = []
while x > 0:
    M.append(x % 16)
    x //= 16
M.reverse()
print(M)

# Вариант 1
A = []
for x in M:
    if x not in A:
        A.append(x)
print(A, len(A))

# Вариант 2
B = set(M)
print(B, len(B))
'''
# Ответ: 6


# Тип 16 № 5650
'''
# Алгоритм вычисления значения функции F(n), где n — натуральное число, задан следующими соотношениями:
#
# F(n) = n + 1 при n ≤ 2;
#
# F(n) = F(n− 1) + 2·F(n − 2) при n > 2.
#
# Чему равно значение функции F(4)? В ответе запишите только натуральное число

def F(n):
    if n <= 2:
        return n + 1
    if n > 2:
        return F(n - 1) + 2 * F(n - 2)

print(F(4))
'''
# Ответ: 13


# Тип 17 № 40733
'''
# Файл содержит последовательность неотрицательных целых чисел, не превышающих 10000. Назовём парой два идущих подряд элемента последовательности.
# Определите количество пар, в которых хотя бы один из двух элементов делится на 3 и хотя бы один из
# двух элементов меньше среднего арифметического всех чётных элементов последовательности.
# В ответе запишите два числа: сначала количество найденных пар, а затем — максимальную сумму элементов таких пар.

f = open('17.txt', 'r')
M = [int(i) for i in f]

summ = 0
kol = 0
for i in range(0, len(M)):
    if M[i] % 2 == 0:
        summ += M[i]
        kol += 1
sred = summ / kol


count = 0
maxi = 0
for i in range(0, len(M)-1):
    if (M[i] % 3 == 0 or M[i+1] % 3 == 0) and (M[i] < sred or M[i+1] < sred):
        count += 1
        if maxi < M[i] + M[i+1]:
            maxi = M[i] + M[i+1]
print(count, maxi)
'''
# Ответ: 2288 14875.



# Тип 17 № 37360
# В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности, у которых сумма элементов кратна 120,
# затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

f = open('17.txt', 'r')
M = [int(i) for i in f]

count = 0
maxi = 0
for i in range(0, len(M)):
    for j in range(i+1, len(M)):
        if (M[i] + M[j]) % 120 == 0:
            count += 1
            if maxi < (M[i] + M[j]):
                maxi = (M[i] + M[j])
print(count, maxi)
# Ответ: 414830 19920













