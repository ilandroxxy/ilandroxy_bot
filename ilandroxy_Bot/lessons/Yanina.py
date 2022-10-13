
# Проверка на аннаграмму
"""
s1 = input()
s2 = input()

base1 = {}
for i in s1:
    base1[i] = base1.get(i, 0) + 1
print(base1)

base2 = {}
for i in s2:
    base2[i] = base2.get(i, 0) + 1
print(base2)

if base1 == base2:
    print('YES')
else:
    print('NO')
"""

# Проверяем и выводим синонимы из словаря
"""
n = int(input('n: '))

base = {}
for i in range(n):
    M = [i for i in input().split()]
    base[M[0]] = M[1]
print(base)

s = input('s: ')
for key in base:
    if s == key:
        print(base[s])
    if s == base[s]:
        print(s)
"""


# Страны и города

n = int(input('Введите кол-во стран: '))

base = {}
for i in range(n):
    M = [i for i in input("Введите страну и ее города: ").split()]
    base[M[0]] = M[1:]
print(base)

# for i in base["Россия"]:
#     print(i)

m = int(input("Введите кол-во городов: "))

for i in range(m):
    town = input('Введите город: ')
    for key in base:
        if town in base[key]:
            print(key)



