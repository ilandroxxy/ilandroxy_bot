import random
import string
from string import *

ALPHABET = '0123456789' + string.ascii_uppercase


def who_is_name():
    names = [i for i in input('Введите имена студентов: ').split()]
    emojes = ['🫵', '👾', '🌚', '💥', '🎉', '✨', '💫', '😇', '🤣']
    return f'\nЗадачу решает: {random.choice(names)} {random.choice(emojes)}'


def valid_parentheses(paren_str):
    s = (ascii_letters + digits + punctuation).replace('()', ' ')
    for x in s:
        paren_str = paren_str.replace(x, '')

    while '()' in paren_str:
        paren_str = paren_str.replace('()', '')
    return len(paren_str) == 0


def my_convert(number: int, system: int) -> str:
    """
Универсальная функция для перевода в системы счисления от 2-ой до 36-ой
    :param number: Переводимое 10-ное число
    :param system: Система счисления в которую будем переводить
    :return: Результат вернем в виде строки
    """
    alphabet = sorted('0123456789QWERTYUIOPASDFGHJKLZXCVBNM')
    result = ''
    while number > 0:
        result += alphabet[number % system]
        number //= system
    return result[::-1]


def orel_or_reshka():
    results = ['Орел 🪙', 'Решка 🪙']
    return random.choice(results)


if __name__ == '__main__':
    print("Hello, world!")
