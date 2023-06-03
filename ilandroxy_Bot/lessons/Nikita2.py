
# region Домашка: ******************************************************************



# endregion Домашка: ******************************************************************



# region Урок: ******************************************************************
print(hex(123)[-2:])


# № 8952 02062023 (ключ неверный) (Уровень: Базовый)
# (Е. Джобс) Обозначим через m&n поразрядную конъюнкцию неотрицательных целых чисел m и n.
# Так, например, 14&5 = 11102&01012 = 01002 = 4.
#
# Найдите минимальное значение А, при котором значение выражения
# (x & 103 = 0) ∧ (x & 94 ≠ 0) → (x & A ≠ 0)
# тождественно истинно, то есть принимает значение 1 при любом натуральном значении х.

def f(x, A):
    return (x & 103 == 0) and (x & 94 != 0) <= (x & A != 0)
for A in range(1, 10000000):
    if all(f(x, A) for x in range(1, 1000)):
        print(A)
        break

# № 8949
for n in range(4, 1000):
  s = "2" + "5" * n
  while "25" in s or "35" in s or "555" in s:
    if "25" in s:
      s = s.replace("25", "53", 1)
    if "35" in s:
      s = s.replace("35", "2", 1)
    if "25" in s:
      s = s.replace("555", "23", 1)
  summ = sum([int(i) for i in s])
  if summ % 7 == 0:
    print(n)
    break


'''
for N in range(6, 36):
    if (7 ** 500 - int("53", N)) % 6 == 0:
        print(N)
        break

# №8951
# ответ 8
'''


'''
def f(n):
  if n >= 10000:
    return 1
  if n < 10000 and n % 2 == 0:
    return f(n+3)+7
  if n < 10000 and n % 2 != 0:
    return f(n+1)-3
print(f(50)-f(57))

# f(50) = f(53)+7
# 
# f(53) = f(54)-3
# 
# f(54) = f(57)+7 - f(57) = 7-3+7=11
# 
# №8953 ответ 11
'''

########8958
'''
def f(a,b):    
    if a < b or a == 22:
        return 0    
    elif a == b:
        return 1    
    else:
        return f(a - 2,b) + f(a // 2,b) + f(a // 3, b)
print(f(40, 2))
'''

# №8950 13 задание ответ: 27

# №8937 1 задание ответ: 15


########8954
'''
M = [int(i)for i in open('17_8954.txt')]
A = max([i for i in M if hex(i)[-2:] == '0f'])
count = 0
maxi = 0
for i in range(len(M) - 1):    
    if (M[i] % 7 == 0 and M[i+1] % 7 !=0) or (M[i] % 7 != 0 and M[i+1] % 7 == 0):
        if (M[i] + M[i+1]) % A == 0:            
            count += 1
            maxi = max(maxi, M[i] + M[i+1])
print(count, maxi)
'''


#######8943
'''
import turtle as t
l = 50
t.speed(100)
t.left(90)
t.left(15)
for _ in range(7):
    t.left(30)    
    t.forward(10 * l)
    t.left(60)
t.penup()
for x in range(-15, 100):
    for y in range(-10, 10):        
    t.goto(x * l, y * l)
        t.dot(3, 'red')t.update()
t.done()
'''

#########8938
'''
print('x y z w')
for x in range(2):
    for y in range(2):        
    for w in range(2):
        for z in range(2):                
            if not(((x or y) == (y <= z)) or w):
                print(x,y,z,w)
'''


##########8942
'''
for n in range(1,1000):    
    s = bin(n)[2:]
    if s.count('1') % 4 == 0:        
        s += '10'
    else:        
        s += '11'
    if int(s, 2) % 2 != 0:        
        s += '0'
    else:        
        s += '1'
    if int(s, 2) <= 250:        
    print(n)
'''


########8952
'''
def f(x, A):    
    return (x & 103 == 0) and (x & 94 != 0) <= (x & A != 0)
for A in range(0, 10000):    
    if all(f(x, A) for x in range(0, 1000)):
        print(A)        
        break
'''

# endregion Урок: ******************************************************************

import useful
print(useful.Who_Is_Name())

# todo:    Никита2   = [5, 3, 9, 17, 19-21, 22, 24.1]
# todo: Никита2 КЕГЭ = [16, 25]
# на прошлом уроке: Прорешивали Джобса от 03.06.2023.
# Никита2:  14, 12, 13, 16, 1
# Владек: 6, 17, 15, 2, 5, 23
# на следующем уроке:
