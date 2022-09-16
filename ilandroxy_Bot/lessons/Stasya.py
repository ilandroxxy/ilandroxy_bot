
# Проверили домашку
'''
# целочисленное деление //
# вещественное /
# деление с остатком %


x = int(input('x: '))
print(x)

print(x // 10) # 12
print(x % 10)  # 3

a1 = x // 100
a2 = (x // 10) % 10
a3 = x % 10

print(a1, a2, a3)

print(f'Сумма цифр числа {x} равна {a1+a2+a3}')
print(f'Произведение цифр числа {x} равна {a1*a2*a3}')
'''




#  Условные операторы (Ветвления)
# if, elif, else
# логические связки and - и, or - или
# логические высказывания:
'''
< 
> 
<= 
>=
==  -  сравнение "равно ли ?"
!=  -  "неравно ? "
=   -  присваивание
'''



'''
x = int(input('x: '))
y = int(input('y: '))

if x < 0 and y < 0:
    print('3 half')
elif x > 0 and y > 0:
    print('1 half')
elif x < 0 and y > 0:
    print('2 half')
elif x > 0 and y < 0:
    print('4 half')
else:
    print('Точка лежит на осях')

# Каскадные условные операторы
if x > 0:
    if y > 0:  # x > 0 and y > 0
        print('1 half')
    else:  # x > 0 and y <= 0
        print('4 half')
else:
    if y > 0:  # x <= 0 and y > 0
        print("2 half")
    else:  # x <= 0 and y <= 0
        print('3 half')
'''

#M = [i for i in input().split()]
#print(f'{int(M[0])} {M[1]} {int(M[2])}')

'''
a = int(input('Введите первое число: '))
s = input('Введите знак действия: ')
b = int(input('Введите второе число: '))
#print(f'{a} {s} {b}')

if s == '+':
    print(f'{a} {s} {b} = {a + b}')
elif s == '-':
    print(f'{a} {s} {b} = {a - b}')
elif s == '*':
    print(f'{a} {s} {b} = {a * b}')
#elif s == '/' and b == 0:
#    print('На ноль делить нельзя!')
#elif s == '/':
#    print(f'{a} {s} {b} = {a / b}')


# ZeroDivisionError
# исключения
elif s == '/':
    try:
        print(f'{a} {s} {b} = {a / b}')
    except ZeroDivisionError:
        print('На ноль делить нельзя!')


else:
    print("Error")
'''


x1 = int(input('x1: '))
y1 = int(input('y1: '))

x2 = int(input('x2: '))
y2 = int(input('y2: '))

if x1 == x2 and y1 == y2:
    print("Фигурой надо обязательно походить!")
elif x1 == x2 or y1 == y2:  # либо какое-то одно условие верно, либо оба верны
    print("YES")
else:
    print('NO')


