import random

def who_is_name():
    names = [i for i in input('Введите имена студентов: ').split()]
    emojes = ['🫵', '👾', '🌚', '💥', '🎉', '✨', '💫', '😇', '🤣']
    return f'\nЗадачу решает: {random.choice(names)} {random.choice(emojes)}'


def valid_parentheses(paren_str):
    if paren_str.count('(') == paren_str.count(')'):
        while '()' in paren_str:
            paren_str = paren_str.replace('()', '', 1)
        if len(paren_str) == 0:
            return True
    return False