import random
import string
from string import *

ALPHABET = '0123456789' + string.ascii_uppercase


def Who_Is_Name():
    names = [i for i in input('Введите имена студентов: ').split()]
    emojes = ['🫵', '👾', '🌚', '💥', '🎉', '✨', '💫', '😇', '🤣']
    return f'\nЗадачу решает: {random.choice(names)} {random.choice(emojes)}'


def Valid_Parentheses(paren_str):
    s = (ascii_letters + digits + punctuation).replace('()', ' ')
    for x in s:
        paren_str = paren_str.replace(x, '')

    while '()' in paren_str:
        paren_str = paren_str.replace('()', '')
    return len(paren_str) == 0


def MyConvert(x: int, n: int) -> str:
    """
Функция для перевода из 10-ной в n-ную систему счисления
    :param x: 10-ное число, которое будем переводить
    :param n: система счисления в которое будем переводить x
    :return: Возвращает переведенное число в виде str
    """
    M = []
    while x > 0:
        M.append(ALPHABET[x % n])
        x //= n
    M.reverse()
    return ''.join(M)


if __name__ == '__main__':
    print("Hello, world!")
