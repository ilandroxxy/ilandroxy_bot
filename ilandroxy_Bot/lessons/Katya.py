# region Домашка:  ******************************************************************************

'''
#Тип 8 № 3233
#Все 5-буквенные слова, составленные из букв А, К, Р, У, записаны в алфавитном порядке. Вот начало списка:
#1. ААААА
#2. ААААК
#3. ААААР
#4. ААААУ
#5. АААКА
#Запишите слово, которое стоит на 250-м месте от начала списка.
s = 'АКРУ'
M = ['0']
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    M.append(temp)
print(M[250])
#ответ:aуурк
'''

'''
#Тип 8 № 10473 Добавить в вариант
#Шифр кодового замка представляет собой последовательность из пяти символов,
# каждый из которых является цифрой от 1 до 4.
# Сколько различных вариантов шифра можно задать, если известно, что цифра 1 встречается ровно два раза,
#а каждая из других допустимых цифр может встречаться в шифре любое количество раз или не встречаться совсем?
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

#ответ:270
'''

'''
##Тип 8 № 3227 Добавить в вариант
#Все 5-буквенные слова, составленные из букв И, О, У, записаны в алфавитном порядке и пронумерованы.
# Вот начало списка:
#1.ИИИИИ
#2.ИИИИО
#3.ИИИИУ
#4.ИИИОИ
#Запишите слово, которое стоит под номером 240.
s = 'ИОУ'
M =[0]
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    M.append(temp)
print(M[240])
#ответ:уууоу
'''

'''
#Тип 8 № 9162 Добавить в вариант
#Все 4-буквенные слова, составленные из букв М, С, Т, Ф, записаны
#в алфавитном порядке.
#Вот начало списка:
#1.#ММММ
#2.МММС
#3.МММТ
#4.МММФ
#5.ММСМ
#Запишите слово, которое стоит на 138-м месте от начала списка.
s = 'МСТФ'
M =[0]
for a in s:
    for b in s:
        for c in s:
            for d in s:
                    temp = a + b + c + d
                    M.append(temp)
print(M[138])
#ответ: тмтс
'''

'''
#Тип 8 № 8658 Добавить в вариант
#Все 5-буквенные слова, составленные из букв А, Н, П, записаны в алфавитном порядке.
#Вот начало списка:
#1.ААААА
#2.ААААН
#3.ААААП
#4.АААНА
#5.АААНН
#Запишите слово, которое стоит на 201-м месте от начала списка.
s = 'АНП'
M =[0]
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    M.append(temp)
print(M[201])
#ответ: пннап
'''


#Тип 8 № 3230
'''
#Все 5-буквенные слова, составленные из букв А, К, Р, У, записаны в алфавитном порядке. Вот начало списка:
#1.ААААА
#2.ААААК
#3.ААААР
#4.ААААУ
#5.АААКА
#Укажите номер слова УКАРА.
s = 'АКРУ'
i = 1
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for f in s:
                    temp = a + b + c + d + f
                    if temp == 'УКАРА':
                        print(i, temp)
                    i += 1

#ответ: 841
'''

'''
#Тип 8 № 16037
#Вася составляет 5-буквенные слова, в которых есть только буквы З, И, М, А,
# причём в каждом слове есть ровно одна гласная буква и она встречается ровно 1 раз.
# Каждая из допустимых согласных букв может встречаться в слове любое количество раз или не встречаться совсем.
# Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
#Сколько существует таких слов, которые может написать Вася?

s = 'ЗИМА'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    temp = a + b + c + d + e
                    if temp.count('И') == 1 and temp.count('А') == 0 or temp.count('А') == 1 and temp.count('И') == 0:
                        count += 1
print(count)
#ответ: 160
'''

# endregion Домашка:  ******************************************************************************



# region Урок:  ******************************************************************************

# Теория строк
'''
import string  # в библиотеке string есть методы выводящие элементы строк
print(string.ascii_uppercase)
print(string.digits)
print(string.punctuation)
'''

# Строки очень похожи на списки и кортежи - у них есть порядковые номера элементов, но менять элементы строки через индекс – нельзя
# s[0] = '*'   TypeError: 'str' object does not support item assignment
'''
s = '123456'
print(s[0], s[-1])

for x in s:
    print(x, end=' ')
print()

for i in range(0, len(s)):
    print(s[i], end=' ')
print()
'''

# Срезы строк и списков
'''
s = '12345678'  # Задача все таким поменять "3" на "*"
s = s[:2] + '*' + s[3:]  # срезы
print(s)

print(s[2:6])  # *456 - вывели подстроку от строки s
# левый включая, правый - не включая

print(s[:6])
print(s[2:])
print(s[::2])  # пробежать строку через один элемент STEP
print(s[::-1])  # по факту перевернули строку аля reverse()

n = 8
s = bin(n)[2:]
print(s)
'''


# Методы строк str()
'''
s = '1234225'
print(len(s))  # функция len() возвращает длину коллекций и строк

print(s.count('2'))  # кол-во элементов в строке
print(s.index('2'), s.rindex('2'))  # вернул индексы первого и последнего вхождения элементов

s = s.replace('2', '*')  # поменяли сразу все элементы
print(s)
s = s.replace('*', '2', 2)  # заменили первые две звездочки на "2"
print(s)

ip = '192.23.54.234'
M = ip.split('.')  # разбили строку на список строк по символу "."
print('M:', M)

A = [int(i) for i in ip.split('.')]  # получили список int-овых значений из строки
print('A:', A)

R = '_'.join(M)  # это обратный к split() метод - список строк преобразовал к строке
print('R:', R)


s = '   123РукгшГРКАУЦГШАРJFiefjUIEHJFREuj    '
print(s)
print(s.strip())
print(s.strip().lower())  # здесь мы не меняем строку!
print(s.strip().upper())
print(s)

s = s.strip().lower()  # вот тут я создал новую - поменял строку 
print(s)
'''





# Тип 24 № 27693
# Текстовый файл состоит не более чем из 10**6 символов A, B и C.
# Определите максимальное количество идущих подряд символов C.
#
# Для выполнения этого задания следует написать программу.
# Ниже приведён файл, который необходимо обработать с помощью данного алгоритма.

'''
f = open('24.txt', 'r')
s = f.readline()
print(s)
'''

# print(max([len(i) for i in open('24.txt', 'r').readline().replace('A', ' ').replace('B', ' ').split()]))
# Ответ: 1.


# Тип 12 № 40728
'''
# Дана программа для редактора:
# ПОКА нашлось (1111)
#   заменить (1111, 22)
#   заменить (222, 1)
# КОНЕЦ ПОКА
#
# Известно, что исходная строка содержала больше 200 единиц и не содержала других цифр.
# При какой наименьшей длине исходной строки результат работы данной программы будет содержать
# наибольшее возможное число единиц?

maxi = 0
for x in range(200+1, 1000):
    s = '1' * x

    while '1111' in s:
        s = s.replace('1111', '22', 1)
        s = s.replace('222', '1', 1)

    if maxi < s.count('1'):
        maxi = s.count('1')
        print(s.count('1'), x)
'''
# Ответ: 201


# Тип 12 № 14273
'''
# Какая строка получится в результате применения приведённой ниже программы к строке,
# состоящей из 85 идущих подряд цифр 7? В ответе запишите полученную строку.
#
# ПОКА нашлось (333) ИЛИ нашлось (777)
# ЕСЛИ нашлось (333)
#   ТО заменить (333, 7)
# ИНАЧЕ заменить (777, 3)
# КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА

s = '7' * 85
while '333' in s or '777' in s:  # ПОКА нашлось (333) ИЛИ нашлось (777)
    if '333' in s:  # # ЕСЛИ нашлось (333)
        s = s.replace('333', '7', 1)  # заменить (333, 7)
    else:
        s = s.replace('777', '3', 1)  # # ИНАЧЕ заменить (777, 3)

print(s)
'''
# Ответ: 377


# Тип 12 № 10388
'''
# Ниже приведена программа для исполнителя Редактор.
#
# ПОКА нашлось (722) ИЛИ нашлось (557)
#   ЕСЛИ нашлось (722
#     ТО заменить (722, 57)
#     ИНАЧЕ заменить (557, 72)
#   КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
#
# На вход этой программе подается строка, состоящая из 55 цифр; последняя цифра в строке — цифра 7,
# а остальные цифры — пятёрки. Какая строка получится в результате применения программы к этой строке?
# В ответе запишите полученную строку.

s = '5' * 54 + '7'

while '722' in s or '557' in s:
    if '722' in s:
        s = s.replace('722', '57', 1)
    else:
        s = s.replace('557', '72', 1)
print(s)
'''
# Ответ: 572


# Какая строка получится в результате применения приведённой ниже программы к строке вида 1…12…2 (45 единиц и 45 двоек)?
# s = '1' * 45 + '2' * 45



# Тип 12 № 47216
'''
# Дана программа для Редактора:
#
# ПОКА нашлось (>1) ИЛИ нашлось (>2) ИЛИ нашлось (>0)
#     ЕСЛИ нашлось (>1)
#         ТО заменить (>1, 22>)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (>2)
#         ТО заменить (>2, 2>)
#     КОНЕЦ ЕСЛИ
#     ЕСЛИ нашлось (>0)
#         ТО заменить (>0, 1>)
#     КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
#
# На вход приведённой выше программе поступает строка, начинающаяся с символа «>»,
# а затем содержащая 39 цифр «0», n цифр «1» и 39 цифр «2», расположенных в произвольном порядке.
#
# Определите наименьшее значение n, при котором сумма числовых значений цифр строки,
# получившейся в результате выполнения программы, является простым числом.

def simpler(x):
    for j in range(2, x):
        if x % j == 0:
            return False
    return True

for n in range(1, 1000):
    s = '>' + '0' * 39 + '1' * n + '2' * 39

    while ">1" in s or '>2' in s or ">0" in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)

    summ = s.count('1') + s.count('2') * 2
    if simpler(summ) == True:
        print(n)
        break
'''
# Ответ: 5




# endregion Урок:  ******************************************************************************


# todo: Екатерина = [2, 5, 8, 14+], на следующем уроке: Продолжаем разбирать 12 номера
