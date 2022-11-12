
'''

s1 = 'красный синий'
s2 = 'красный желтый'
s3 = 'синий желтый'

M = [i for i in input().split()]
x = M[0]
y = M[1]

if x == y:
    print(f'Получится: {x}')
elif x in s1 and y in s1:
    print('Получился: фиолетовый')
elif x in s2 and y in s2:
    print('Получился: оранжевый')
elif x in s3 and y in s3:
    print('Получился: зеленый')
else:
    print('Ошибка')
'''


# Циклы

# for - цикл "повтори n раз"
'''
for i in range(5):  # [0, 5)     # range(START == 0, STOP, STEP == 1)
    print(i, end=' ')
print()

for i in range(1, 10):  # [1, 10)   # range(START, STOP, STEP == 1)
    print(i, end=' ')
print()

for i in range(1, 10+1):  # [1, 10]
    print(i, end=' ')
print()

for i in range(0, 10+1, 2):  # [1, 10]    # range(START, STOP, STEP)
    print(i, end=' ')
print()

for i in range(10-1, 0-1, -1):  # пробежали отрезок в обратном порядке
    print(i, end=' ')
print()


s = '654321'
# i  012345
M = [6, 5, 4, 3, 2, 1]
# i  0  1  2  3  4  5

print(M[0], s[0])

for x in s:
    print(x, end=' ')
print()
'''



# len() - функция возвращающая длину списка или строки
'''
for i in range(0, len(s)):  # [0, 6)
    print(s[i], end=' ')
print()

for i in range(0, len(M)):  # [0, 6)
    print(M[i], end=' ')
print()

print(M)
for i in range(0, len(M)):  # через такой список можно легко изменять элементы списка (но только списка)
    M[i] = M[i] ** 2
print(M)
'''


# while - цикл с условием (если условие истинно, то выполняем действие) - (пока условие истинно)
'''
for i in range(0, 10+1, 2):  # [1, 10]    # range(START, STOP, STEP)
    print(i, end=' ')
print()


i = 0
while i <= 10:
    print(i, end=' ')
    i += 2
print()


M = [1, 0, 1, 0, 1]
N = [1, 0]

while len(N) != len(M):
    if len(N) < len(M):
        N.reverse()
        N.append(0)
        N.reverse()
    else:
        M.reverse()
        M.append(0)
        M.reverse()

print(M)
print(N)
'''

import random

password = 'qwerty'
count = 0
while True:
    pas = input("Введите пароль: ")
    if pas == password:
        print('Welcome')
        break
    print('Пароль неверный, попробуйте снова!')
    count += 1
    if count == 3:
        symbol = '+-*'
        a = random.randint(1, 100)
        s = random.choice(symbol)
        b = random. randint(1, 100)
        print(f'Пройдите проверку на робота:\n{a}{s}{b} =')
        x = int(input())

        if s == '+':
            if x == a + b:
                count = 0
                print("Проверка пройдена")
                continue
            else:
                print('BANNED')
                break
        elif s == '-':
            if x == a - b:
                count = 0
                print("Проверка пройдена")
                continue
            else:
                print('BANNED')
                break
        elif s == '*':
            if x == a * b:
                count = 0
                print("Проверка пройдена")
                continue
            else:
                print('BANNED')
                break




# todo: На следующем уроке: continue, break, порешать задачки с циклами

# todo: Бот игра для тренировки устного счета (вычислений)