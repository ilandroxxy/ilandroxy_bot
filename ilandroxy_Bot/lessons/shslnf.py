

# region Домашка: ***************************************************************


# endregion Домашка: ************************************************************


# region Урок: ******************************************************************

# Условные операторы (ветвление): if, elif, else
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0 and y > 0:    # if (если)
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:   # else (иначе)
    print('Лежит на осях')
'''

# Каскадные условные операторы
'''
x = int(input('x: '))
y = int(input('y: '))

if x > 0:
    if y > 0:  # x > 0 and y > 0
        print('Первая четверть')
    else:  # x > 0 and y <= 0
        print('Четвертая четверть')
else:
    if y > 0:  # x <= 0 and y > 0
        print('Вторая четверть')
    else:  # x <= 0 and y <= 0
        print('Третья четверть')
'''

a = int(input('a: '))
s = input('s: ')
b = int(input('b: '))

if s == '+':
    print(f'{a} + {b} = {a + b}')
elif s == '-':
    print(f'{a} - {b} = {a - b}')

# endregion Урок: ***************************************************************


# todo: Саяд = []
# todo: КЕГЭ  = []
# на прошлом уроке: Проработали команды: mkdir, echo >, rmdir, cd, notepad
# на следующем уроке:


