# region Домашка: ******************************************************************
'''
# №12246
x = 2*729**333 + 2*243**334 - 81**335 + 2*27**336 - 2*9**337 - 338
s = ''
while x != 0:
    s += str(x % 9)
    x //= 9
s = s[::-1]
print(len(s)-(s.count("0")))
'''
# endregion Домашка: ******************************************************************


# region Урок: ********************************************************************
'''
from random import randint

print('Вас приветствует игра "Камень, ножницы, бумага"!')
name = input('Введите своё имя: ')
count_win_user = 0
count_win_comp = 0
count_draw = 0


def game():
    print('\nИгра начинается!')
    print('Варианты хода:\n'
          '1 - Камень\n'
          '2 - Ножницы\n'
          '3 - Бумага\n'
          '0 - Выйти в главное меню')

    values = ['Камень', 'Ножницы', 'Бумага']

    user_value = int(input(f'{name}, ваш выбор: '))
    comp_value = randint(1, 3)

    print(f'{name}, ваш ход - ', values[user_value - 1])
    print('Ход компьютера - ', values[comp_value - 1])

    if user_value == 0:
        return 3
    elif user_value == 1 and comp_value == 2:
        print('Ура, Победа!')
        return 1
    elif user_value == 2 and comp_value == 3:
        print('Ура, Победа!')
        return 1
    elif user_value == 3 and comp_value == 1:
        print('Ура, Победа!')
        return 1
    elif user_value == comp_value:
        print('Ничья!')
        return 2
    else:
        print(f'{name}, вы проиграли =(')
        return 0


def results(user, comp, draw):
    print(f'{name}, ваши победы: ', user)
    print('Победы компьютера: ', comp)
    print(f'Кол-во нечейных результатов: {draw}')


while True:
    print('\nМеню:\n'
          '1 - Играть\n'
          '2 - Результат\n'
          '3 - Выход')
    key = int(input(f'{name}, выберите действие: '))

    while key < 1 or key > 3:
        print('Ошибка ввода!')
        key = int(input(f'{name}, выберите действие: '))

    if key == 1:
        while True:
            n = game()
            if n == 3:
                break
            elif n == 1:
                count_win_user += 1
            elif n == 0:
                count_win_comp += 1
            elif n == 2:
                count_draw += 1

    elif key == 2:
        results(count_win_user, count_win_comp, count_draw)

    elif key == 3:
        print(f'Игра окончена, спасибо за игру, {name}!')
        break
'''


# Вместо "Ваш", "Вам" и т.д. выводить имя (напр. "Сергей, Ваш ход:"
# В результаты добавить статистику по ничьей
# Играть пока не захочу закончить игру и выйти в меню
'''
from random import randint
count_win_user = 0
count_win_comp = 0


def game(name):
    print('\nИгра начинается!')
    print('Варианты хода:\n'
          '1 - Камень\n'
          '2 - Ножницы\n'
          '3 - Бумага')

    values = ['Камень', 'Ножницы', 'Бумага']

    user_value = int(input(f'{name}, ваш выбор: '))
    comp_value = randint(1, 3)

    print(f'{name}, ваш ход - ', values[user_value - 1])
    print('Ход компьютера - ', values[comp_value - 1])

    if user_value == 1 and comp_value == 2:
        print('Ура, Победа!')
        return 1
    elif user_value == 2 and comp_value == 3:
        print('Ура, Победа!')
        return 1
    elif user_value == 3 and comp_value == 1:
        print('Ура, Победа!')
        return 1
    elif user_value == comp_value:
        print('Ничья!')
    else:
        print(f'{name}, вы проиграли =(')
        return 0


def results(user, comp, name):
    print(f'{name}, ваши победы: ', user)
    print('Победы компьютера: ', comp)


print('Вас приветствует игра "Камень, ножницы, бумага"!')
name = input('Введите своё имя: ')


while True:
    print('\nМеню:\n'
          '1 - Играть\n'
          '2 - Результат\n'
          '3 - Выход')
    key = int(input(f'{name}, выберите действие: '))

    while key < 1 or key > 3:
        print('Ошибка ввода!')
        key = int(input(f'{name}, выберите действие: '))

    if key == 1:
        n = game(name)
        if n == 1:
            count_win_user += 1
        elif n == 0:
            count_win_comp += 1

    elif key == 2:
        results(count_win_user, count_win_comp, name)

    elif key == 3:
        print(f'Игра окончена, спасибо за игру, {name}!')
        break
'''

# endregion Урок: ******************************************************************


# region Разобрать: *************************************************************

# endregion Разобрать: *************************************************************


# Варя = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19-21, 22, 23, 24, 25]
# КЕГЭ  = [14]
# на следующем уроке:

