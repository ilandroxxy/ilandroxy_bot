
# region Домашка: ******************************************************************


# endregion Домашка: ******************************************************************


# region Урок: ******************************************************************

# Условные операторы (ветвления): if, elif, else

'''
x = 0
y = 8

if x > 0 and y > 0:  # if - ЕСЛИ
    print('Первая четверть')
elif x < 0 and y > 0:  # elif - ИНАЧЕ ЕСЛИ
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:  # else - ИНАЧЕ
    print('Лежит на осях')

print('Конец программы')
'''

# Логические связки: and, or, not
'''
flag = True
print(not flag)  # False

a = 5
b = -4

if a > 0 and b > 0:
    print('YES1')
if a > 0 or b > 0:  # хотя бы одно условие должно выполняться
    print('YES2')


x = 0
y = 8

if x > 0 and y > 0:  # if - ЕСЛИ
    print('Первая четверть')

if x > 0:  # вложенность условий
    if y > 0:
        print('Первая четверть')
'''


# Задание ака 17-ый номер
# Выведите на экран только четные числа
'''
import random
M = [random.randint(0, 100) for _ in range(10)]
for x in M:
    if x % 2 == 0:
        print(x, end=' ')
print()
'''

# Цикл for: "повтори n раз", "пробеги диапазон чисел от a до b"
'''
for i in range(10):  # range(START=0, STOP=10-1, STEP=1)
    print(i, end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for i in range(2, 10):  # range(START=2, STOP=10-1, STEP=1)
    print(i, end=' ')  # 2 3 4 5 6 7 8 9
print()

for i in range(2, 10+1, 2):  # range(START=2, STOP=11-1, STEP=2)
    print(i, end=' ')  # 2 4 6 8 10
print()

for i in range(10, 0, -1):  # range(START=10, STOP=0+1, STEP=-1)
    print(i, end=' ')  # 10 9 8 7 6 5 4 3 2 1
print()

# i   0    1    2    3    4
M = ['a', 'b', 'c', 'd', 'e']
# -i -5   -4   -3   -2   -1

for i in range(0, len(M)):  # функция len() - возвращает длину последовательности (кол-во элементов)
    # print(i, end=' ')  # 0 1 2 3 4
    print(M[i], end=' ')  # a b c d e
print()

s = 'abcde'
for i in range(0, len(s)):
    print(s[i], end=' ')  # a b c d e
print()
'''

# через индексы можно менять элементы списков
'''
for i in range(0, len(M)):
    M[i] = M[i] * i
print(M)  # ['', 'b', 'cc', 'ddd', 'eeee']
'''

'''
for x in M:
    print(x, end=' ')  # a b c d e
print()

for x in M:
    if x in 'ae':
        print(x, end=' ')  #  a e 
print()
'''

'''
words = ['wfuh', 'wefe', 'rger', 'ergre']
print(words[2].index('g'))  # 1
'''


# Цикл while: "цикл с условием: Выполняй действие, пока условие верно", "бесконечный цикл"

# Перевод из 10-ной в 2-ную систему:
'''
x = int(input('x: '))
n = 2
M = []
while x > 0:
    M.append(x % n)  # добавление нового элемента в конец списка
    x //= n
M.reverse()  # метод для разворота элементов списка
print(M)
'''

# Бесконечные циклы
'''
i = 0
while i < 10:
    print(i)
'''
'''
k = 1
while True:
    if k == 100000000:
        break
    k += 1
    print(k)
'''

'''
import random
import time

answers = ['Ошибка, введите пароль заново: ',
           'Попробуйте повторить ввод пароля:',
           'Повторите попытку снова:']

pas = 'qwerty'
count = 0
password = input('Введите пароль для входа: ')
while True:
    if pas == password:
        print('Welcome!')
        break
    count += 1
    if count == 3:
        print('Пройдите проверку на робота:')
        a = random.randint(0, 100)
        b = random.randint(0, 100)
        x = int(input(f'{a} + {b} = '))
        if x == a + b:
            print('Проверка успешно пройдена!')
            count = 0
        else:
            print('Повторите попытку через 20 секунд.')
            time.sleep(20)
    password = input(random.choice(answers))
'''

# endregion Урок: ******************************************************************


# todo: Марго = []
# todo:   КЕГЭ  = []
# на прошлом уроке:
# на следующем уроке:
