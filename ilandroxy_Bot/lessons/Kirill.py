# region Домашка:  **************************************************



# endregion Домашка: **************************************************


# region Урок:  **************************************************

# Условные операторы (Ветвление)
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0 and y > 0:  # if - если
    print(1)
elif x < 0 and y < 0:
    print(3)
elif x < 0 and y > 0:
    print(2)
elif x > 0 and y < 0:
    print(4)
else:
    print('Точка лежит на оси')
'''

# Каскадные условия
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0:
    if y > 0:
        print(1)  # x > 0 and y > 0
    else:
        print(4)  # x > 0 and y <= 0
else:
    if y > 0:
        print(2)  # x <= 0 and y > 0
    else:
        print(3)  # x <= 0 and y <= 0
'''

# Условия с логическими связками
'''
a = 5
b = -4
c = 0  # присваивание (присваиваем переменной значение)
if c == 0:  # сравнение (сравниваем два числа)
    pass

if a > 0 and b < 0 and c == 0:  # все условия должны быть истинны (выполнены)
    print('YES 1')
if (a > 0 and b < 0) or c != 0:  # хотя бы одно условие должно выполняться
    print('YES 2')
if (a > 0 and b < 0) or (not(c == 0)):  # хотя бы одно условие должно выполняться
    print('YES 2')

print(not(True))
'''

# Циклы
# Цикл for - для диапазона, повтори n раз
'''
for i in range(5):  # [0, 5)    range(START == 0, STOP, STEP == 1)
    print(i)  # 0 1 2 3 4 5

for i in range(2, 10):  # [2, 10)    range(START, STOP, STEP == 1)
    print(i)  # 2 3 4 5 6 7 8 9

for i in range(2, 10, 2):  # [2, 10)    range(START, STOP, STEP)
    print(i)  # 2 4 6 8

for i in range(10, 0-1, -1):  # [10, 0]    range(START, STOP, STEP)
    print(i)  # 10 9 8 7 6 5 4 3 2 1

for _ in range(5):
    print('Kirill')

M = [1, 2, 3, 4, 5]
s = '12345'
for x in s:  # так можно пробежать коллекцию элементов
    print(x)
'''

# Цикл while - пока условие выполняется (истинно) делает действие
'''
for i in range(2, 10+1, 2):  # [2, 10]    range(START, STOP, STEP)
    print(i)  # 2 4 6 8

print('------------------------------')

i = 2
while i <= 10:
    print(i)
    i += 2

k = 0
while True:
    k += 1
    print(k)
'''


'''
import random

password = 'qwerty'
count = 0
while True:
    pas = input('Введите пароль от учетной записи: ')
    if pas == password:
        print('Welcome')
        break
    print('Пароль неверный, попробуйте снова')
    count += 1
    if count == 3:
        a = random.randint(1, 100)
        s = random.choice(['+', '-'])
        b = random.randint(1, 100)
        print(f'Решите пример: {a} {s} {b} = ?')
        x = int(input())
        if s == '+':
            if x == a + b:
                count = 0
                print('Проверка пройдена успешно!')
            else:
                print('BAN')
                break
        if s == '-':
            if x == a - b:
                count = 0
                print('Проверка пройдена успешно!')
            else:
                print('BAN')
                break
'''


'''  
break   # прерывает выполнение цикла
continue  # прерывает итерацию цикла
exit()  # прерывает выполнение программы
'''

'''
for x in range(1, 20):
    if x % 2 == 0:
        continue
    if x == 15:
        break
    print(x)
'''


# Операции математической логики на языке Пайтон
#  ¬z    ---->   (not(z))    инверсия (отрицание)
# y ∧ z  ---->   y and z     конъюнкция (логическое умножение)
# x ∨ y  ---->   x or y      дизъюнкция (логическое сложение)
# x → y  ---->   x <= y      импликация
# x ≡ z  ---->   x == z

# Тип 2 № 15097
# Логическая функция F задаётся выражением (x ≡ z) ∨ (x → (y ∧ z)).
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z.
'''
print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            F = ((x == z) or (x <= (y and z)))
            if F == False:
                print(x, y, z, F)

'''


# Тип 2 № 47206
# Миша заполнял таблицу истинности логической функции F
# ¬(y→x)∨(z→w)∨¬z,
# но успел заполнить лишь фрагмент из трёх различных её строк, даже не указав, какому столбцу таблицы соответствует каждая из переменных w, x, y, z.
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((not(y <= x)) or (z <= w) or (not(z)))
                if F == False:
                    print(x, y, z, w, F)
'''

# # region Тип 2 № 17366

# Логическая функция F задаётся выражением ((x ∧ w) ∨ (w ∧ z)) ≡ ((z → y) ∧ (y → x)).
# Дан частично заполненный фрагмент, содержащий неповторяющиеся строки таблицы истинности функции F.
# Определите, какому столбцу таблицы истинности соответствует каждая из переменных x, y, z, w.
'''
print('x y z w F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (((x and w) or (w and z)) == ((z <= y) and (y <= x)))
                if F == True:
                    print(x, y, z, w, F)
'''
# Ответ: yzwx



# endregion Урок:  **************************************************


# todo: Кирилл = [ ], на следующем уроке: Вопросы по 2-му номеру ЕГЭ, Строки и Списки