# Задача C. Сколько букв в строке?
# Напишите программу, которая выводит количество букв в введенной  строке.
'''
s = input()
count = 0
for i in s:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        count += 1
print(count)
'''


'''
a = input()
b = 0
for i in range(65, 91):
    if chr(i) in a:
        b += 1
for i in range(97, 123):
    if chr(i) in a:
        b += 1
print(b)
'''




# Задача L. Следующая строка
'''
# Вам на вход подается строка s. Вам необходимо заменить все вхождения букв на следующие
# по алфавиту с соблюдением регистра. А все вхождения цифр необходимо заменить на предыдущие
# цифры. В остальном строку необходимо оставить без изменений.

# Hello, World222!

s = input()
res = ''
for i in s:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        if ord(i) == 90:
            res += 'A'
        elif ord(i) == 122:
            res += 'a'
        else:
            res += chr(ord(i) + 1)
    elif 48 <= ord(i) <= 57:
        if ord(i) == 48:
            res += '9'
        elif ord(i) == 57:
            res += '0'
        else:
            res += chr(ord(i) - 1)
    else:
        res += i
print(res)
'''

s1 = 'hello'
s2 = 'hello '
print(s2 + s1)


# Задача G. Замена a-b
# Напишите  программу,  которая  заменяет  в  символьной  строке  все  буквы  a  на  буквы  b  (латинские,
# строчные). Программа   должна   заменить   во   всей   строке   строчные   буквы   a   на   буквы   b   и   вывести   в   первой
# строке  получившуюся  символьную  строку,  а  во  второй  –  количество  выполненных  замен.

s = input()
res = ''
count = 0
for i in s:
    if ord(i) == 97:
        res += 'b'  # chr(98)
        count += 1
    else:
        res += i
print(res)
print(count)


