# Домашка

'''
# Самописный калькулятор
a = int(input('a: '))
s = input('s: ')
b = int(input('b: '))
'''
'''
if s == '+':
    print(f'{a} {s} {b} = {a + b}')
elif s == '-':
    print(f'{a} {s} {b} = {a - b}')
elif s == '*':
    print(f'{a} {s} {b} = {a * b}')
elif s == "/"  and b == 0:
    print('На ноль делить нельзя')
elif s == "/":
    print(f'{a} {s} {b} = {a / b}')
else:
    print('Ошибка')
'''
'''
# Принадлежность 3
x = int(input())
if(x > -30 and x <= -2) or (x > 7 and x <= 25):
    print('yes')
else:
    print('no')
'''
'''
# красивое число
x = int(input())
if(x % 17 == 0 or x % 7 == 0) and ( x > 1000 or x < 9999):
    print('yes')
else:
    print('no')
'''








