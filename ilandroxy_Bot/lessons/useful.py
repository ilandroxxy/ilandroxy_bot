import random
from string import *


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

