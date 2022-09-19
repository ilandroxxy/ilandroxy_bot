list1 = [1,  2.5,  '4', True]
# type: int, float, str, bool


list2 = [3 + 4, 7 / 2, '4' * 5, 4 < 10]
# type:  int  , float,   str  ,  bool


list3 = [[1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 'один', 2: 'два', 3: 'три'}]
# type:    list   ,   tuple  ,    set   ,        dict


Setter = list1 + list2 + list3
for i in Setter:
    print(f'{i} <-----> {type(i)}')