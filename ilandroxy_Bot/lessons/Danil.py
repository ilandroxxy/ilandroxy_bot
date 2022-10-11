# Условные операторы (ветвление)
# Ключевые слова: if elif else, and or not

# - однострочный комментарий (закрывает строчку для программы)

"""
Многострочный комментарий - позволяет скрыть кусок кода от программы
"""


# Пример математической функции модуль
"""
x = -5
if x < 0:  # IF - ЕСЛИ, если условие истинно (True) то выполняем тело условного оператора
    print(-x)
if x > 0:
    print(x)
if x == 0:
    print(0)


x = -5
if x < 0:  # IF - ЕСЛИ, если условие истинно (True) то выполняем тело условного оператора
    print(-x)
elif x > 0:  # ELIF - ИНАЧЕ ЕСЛИ
    print(x)
elif x == 0:
    print(0)


x = -5
if x < 0:  # IF - ЕСЛИ, если условие истинно (True) то выполняем тело условного оператора
    print(-x)
elif x > 0:  # ELIF - ИНАЧЕ ЕСЛИ, проверяется ТОЛЬКОЕ ЕСЛИ if ложно
    print(x)
else:  # ELSE - ИНАЧЕ - выполняется в противовес всем остальным условиям, не имеет условия по этой причине
    print(0)
"""




# Декартова система координат
"""
x = int(input('x: '))
y = int(input('y: '))

if x > 0 and y > 0:  # and гарантирует выполнение условия, только если оба условия будут истинны
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
else:
    print('Лежит на оси.')
"""


# if и else образуют условие между собой, то есть else работает на ближайший сверхустоящий (вертикально) if
# если нужно прописать большое условие с взаимосвязью и else - используйте elif.

# Каскадные условные операторы
"""
x = int(input('x: '))
y = int(input('y: '))

if x > 0:
    if y > 0:  # x > 0 and y > 0
        print(1)
    else:  # x > 0 and y <= 0
        print(4)
else:  # x <= 0 and y > 0
    if y > 0:
        print(2)
    else:  # x <= 0 and y <= 0
        print(3)
"""

# Логические связки
"""
s1 = 'Danil'
s2 = 'Daniil'
# == - сравнение (равны ли два элемента?)
print(s1 == s2)

# != - отризательное сравнение (не равны ли элементы)
print(s1 != s2)

# = - присваивание переменной значения (данных)

a = 5
b = 0
c = 8

if a > 0 and b < 0 and c == 0:
    print('YES_1')
if (a > 0 and b < 0) or c == 0:
    print('Yes_2')
if (a > 0 and b < 0) or (not(c == 0)):
    print('Yes_3')
else:
    print('NO')
# and - все условия связанные ей - должны выполняться

# or - хотя бы одно из условий должно быть истинно (либо оба)

# (not(c == 0))  - любые условия кроме c == 0
"""



# Самописный калькулятор
"""
a = int(input("a: "))
s = input('s: ')
b = int(input('b: '))

if s == '+':
    print(f'{a} {s} {b} = {a + b}')
elif s == '-':
    print(f'{a} {s} {b} = {a - b}')
elif s == '*':
    print(f'{a} {s} {b} = {a * b}')
elif s == '/' and b == 0:
    print(f'На ноль делить нельзя!')
elif s == '/':
    print(f'{a} {s} {b} = {a / b}')
"""


# ZeroDivisionError: division by zero
"""
a = int(input("a: "))
s = input('s: ')
b = int(input('b: '))

try:
    if s == '/':
        print(f'{a} {s} {b} = {a / b}')
except ZeroDivisionError:
    print('На ноль делить нельзя!')   
"""

# Ход Ладьи
"""
x1 = int(input('x1: '))
y1 = int(input('y1: '))

x2 = int(input('x2: '))
y2 = int(input('y2: '))

if x1 == x2 and y1 == y2:
    print('Надо обязательно сделать ход!')
elif x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')
"""






