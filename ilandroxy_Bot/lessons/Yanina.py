'''
def NOD(x, y):
    """
Функция NOD ищет Наибольший общий делитель

:param x: Первое число
:param y: Второе число
:return: Возвращает наибольший делитель для x, y
    """
    max_delit = 0
    for j in range(1, min(x, y)+1):
        if x % j == 0 and y % j == 0:
            max_delit = j
    return max_delit
'''




