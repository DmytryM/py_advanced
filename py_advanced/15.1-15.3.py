# ----------------- 1 --------------------

# def matrix(n=1, m=None, value=0):
#     if m is None:
#         m = n
#     return [[value] * m for _ in range(n)]
#
#
# print(matrix())  # матрица 1 × 1 из 0
# print(matrix(3))  # матрица 3 × 3 из 0
# print(matrix(2, 5))  # матрица 2 × 5 из 0
# print(matrix(3, 4, 9))  # матрица 3 × 4 из 9

# ----------------- 2 --------------------

# def func(*args):
#     return max(args) + min(args)
#
#
# print(func(10, 15, *[31, 42, 5, 1], *(17, 28, 19, 100), 13, 12))

# ----------------- 2 --------------------

# def count_args(*args):
#     return len(args)
#
#
# print(count_args())
# print(count_args(10))
# print(count_args('stepik', 'beegeek'))
# print(count_args([], (''), 'a', 12, False))

# ----------------- 3 --------------------

# def sq_sum(*args):
#     return sum([i ** 2 for i in args])
# print(sq_sum())
# print(sq_sum(2))
# print(sq_sum(1.5, 2.5))
# print(sq_sum(1, 2, 3))
# print(sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# ----------------- 4 --------------------

# def mean(*args):
#     s = [float(i) for i in args if type(i) in (int, float)]
#     if len(s) > 0:
#         return sum(s) / len(s)
#     else:
#         return 0.0
#
#
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# ----------------- 5 --------------------

# def greet(name, *args):
#     res = f"Hello, {name}"
#     for i in args:
#         res += f" and {i}"
#     return res + '!'
#
#
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))

# ----------------- 6 --------------------

# def print_products(*args):
#     res = [i for i in args if type(i) == str and i != '']
#     if res:
#         print(*[f"{i + 1}) {res[i]}" for i in range(len(res))], sep='\n')
#     else:
#         print("Нет продуктов")
#
#
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)
# print_products([4], {}, 1, 2, {'Beegeek'}, '')

# ----------------- 7 --------------------

# def info_kwargs(**kwargs):
#     for key, value in sorted(kwargs.items()):
#         print(f"{key}: {value}")
#
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')

# ----------------- 8 --------------------

# def comparator(pair):
#     return pair[1]
#
#
# pairs = [(5, 4), (3, 2), (1, 7), (8, 2)]
# pairs.sort(key=comparator)
# print(pairs)

# ----------------- 9 --------------------

# def mid(number):
#     return sum(number) / len(number)
#
#
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
#            (10, 20, 30, -2),
#            (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
#
# print(min(numbers, key=mid))
# print(max(numbers, key=mid))

# ----------------- 10 --------------------

# def distance(coords):
#     x, y = coords
#     return x ** 2 + y ** 2
#
#
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
#
# print(sorted(points, key=distance))

# ----------------- 11 --------------------

# def mean(numbers):
#     x,y = max(numbers), min(numbers)
#     return x + y
# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
# print(sorted(numbers,key=mean))

# ----------------- 12 --------------------

# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
#
# def sort_name(athlete):
#     return athlete[0]
#
#
# def sort_age(athlete):
#     return athlete[1]
#
#
# def sort_height(athlete):
#     return athlete[2]
#
#
# def sort_weight(athlete):
#     return athlete[3]
#
# sort_by = {1: sort_name, 2: sort_age, 3: sort_height, 4: sort_weight}
#
# for i in sorted(athletes, key=sort_by[int(input())]):
#     print(*i)

# ----------------- 13 --------------------

# from math import sin
#
#
# def f1(number):
#     return abs(number) ** 2
#
#
# def f2(number):
#     return number ** 3
#
#
# def f3(number):
#     return abs(number) ** 0.5
#
#
# def f4(number):
#     return abs(number)
#
#
# def f5(number):
#     return sin(number)
#
#
# number, figure = int(input()), input()
#
# commands = {'квадрат': f1, 'куб': f2, 'корень': f3, 'модуль': f4, 'синус': f5}
#
# print(commands[figure](number))

# ----------------- 14 --------------------

# def summ(n):
#     res = {}
#     new = 0
#     for i in n:
#         for j in i:
#             new += int(j)
#         res[i] = new
#         new = 0
#     return res
#
#
# n = input().split()
# result1 = summ(n)
# for i,y in sorted(result1.items(), key=lambda para: para[1]):
#     print(i,end=' ')
# print(result1)

# ----------------- 15 --------------------

# def comparator(n):
#     return sum([int(i) for i in str(n)])
#
#
# numbers = [int(i) for i in input().split()]
#
# numbers.sort()
# print(*sorted(numbers, key=comparator))

# ----------------- 16 --------------------

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item,2))
#     return result
#
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
#
# print(*map(round, numbers), sep='\n')

# ----------------- 17 --------------------

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# def condition(items):
#     return 1 <= items // 100 < 10 and items % 5 == 2
#
#
# def cube(item):
#     return item ** 3
#
#
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434,
#            1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289,
#            1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013,
#            898,
#            669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268,
#            351,
#            1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
#
# result = map(cube, filter(condition, numbers))
# print(*result, sep='\n')

# ----------------- 18 --------------------

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
#
# def x_to_xx(number):
#     return number**2
#
# def add(x, y):
#     return x + y**2
#
#
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35,
#            11,
#            -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72,
#            34,
#            82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54,
#            31,
#            95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
#
# result = reduce(add, numbers, 0)
# print(result)
# new = sum(map(x_to_xx, numbers))
# print(new)
# print(sum(numbers))

# ----------------- 19 --------------------

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
#
#
# def condition(items):
#     return len(str(abs(items))) == 2 and items % 7 == 0
#
#
# def x_to_xx(number):
#     return number ** 2
#
#
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202,
#            58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208,
#            231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128,
#            143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71,
#            135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228,
#            129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269,
#            94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123,
#            -105]
#
# print(sum(map(x_to_xx, filter(condition, numbers))))

# ----------------- 20 --------------------

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# def add3(x):
#     return x + 3
#
#
# def mul7(x):
#     return x * 7
#
#
# def func_apply(function, numbers):
#     result = map(function, numbers)
#     return result
#
# print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))

# ----------------- 21 --------------------

# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num**2, 1), floats))
# filter_result = list(filter(lambda name: name if len(name) > 4 and name == name[::-1] else None, words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)

# ----------------- 22 --------------------

# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# res1 = list(filter(lambda city: city[1] > 10000000 and city[2] == 'primary', data))
# city_result = list(map(lambda city: city[0], res1))
# c = sorted(city_result)
# print(reduce(lambda x, y: f'{x} {y},', c, 'Cities:').strip(','))

# ----------------- 23 --------------------

# func = lambda x: True if x % 19 == 0 or x % 13 == 0 else False
# print(func(20))

# ----------------- 24 --------------------

# func = lambda x: x[0].lower() == x[-1].lower() == 'a'
# print(func('bcdA'))
# print(func('abcdA'))

# ----------------- 25 --------------------

# # def is_non_negative_num(n):
# #   try:
# #     n = float(n)
# #   except ValueError:
# #     return False
# #   return n >= 0
# is_non_negative_num = lambda s: s.count('.') <= 1 and set(s) <= set('.1234567890')
# print(is_non_negative_num('10.34ab'))
# print(is_non_negative_num('10.45'))
# print(is_non_negative_num('-18'))
# print(is_non_negative_num('-34.67'))
# print(is_non_negative_num('987'))
# print(is_non_negative_num('abcd'))
# print(is_non_negative_num('123.122.12'))
# print(is_non_negative_num('123.122'))

# ----------------- 25.2 --------------------

# def is_num(x):
#     try:
#         return float(x) >= 0 or float(x) <= 0
#     except:
#         return False
#
# # is_num = lambda s: s.count('.') <= 1 and set(s) <= set('.1234567890')
#
# print(is_num('10.34ab'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))
# print(is_num('--13.2'))

# ----------------- 26 --------------------

# words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse', 'bid', 'wednesday', 'able',
#          'betray', 'accident', 'abduct', 'bigot', 'bet', 'abandon', 'besides', 'access', 'friday', 'bestow', 'abound',
#          'absent', 'beware', 'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday', 'tuesday',
#          'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle', 'beside', 'accept', 'berry', 'bewilder',
#          'abrupt', 'saturday', 'accessory', 'absorb']
#
# res = list(filter(lambda x: len(x) == 6, words))
# print(*sorted(res))

# ----------------- 27 --------------------

# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80, 80, 93,
#            40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57, 53, 43,
#            35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37, 44, 2,
#            38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# res = list(filter(lambda x: not(x > 47 and x % 2 != 0), numbers))
# res2 = list(map(lambda x: x // 2 if x % 2 == 0 else x, res))
# print(*res2)

# ----------------- 28 --------------------

# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'), (1805832, 'West Virginia'),
#         (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'), (10077331, 'Michigan'), (10439388, 'Virginia'),
#         (7705281, 'Washington'), (7151502, 'Arizona'), (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
# res1 = sorted(data, key = lambda x: x[-1][-1], reverse=True)
# for i in range(len(res1)):
#     print(f"{res1[i][1]}: {res1[i][0]}")

# ----------------- 29 --------------------

# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз',
#         'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид', 'система', 'часть',
#         'город', 'отношение', 'женщина', 'деньги']
#
# print(*sorted(data, key=lambda x: (len(x), x)))

# ----------------- 30 --------------------

# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday',
#               'about', 454805,
#               'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434, 'bicycle',
#               'accelerate', 1109147, 942908,
#               'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder', 1586517, 375290, 1503450, 2713047,
#               'abnormal', 2286106, 242192, 701049,
#               2866491, 'benevolent', 'bigot', 'abuse', 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond',
#               2415643, 'aboard', 'bet', 859105,
#               'accident', 2223166, 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish',
#               'beware', 2618492, 1555062, 'access',
#               'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698,
#               'thursday', 810387, 'friday', 2576799,
#               2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326, 1499197, 2241159, 605320, 2347441]
#
#
# print(max(list(filter(lambda x: x if isinstance(x, int) else False, mixed_list))))

# ----------------- 31 --------------------

# mixed_list = ['beside', 48, 'accelerate', 28, 'beware', 'absorb', 'besides', 'berry', 15, 65, 'abate', 'thursday', 76,
#               70, 94, 35, 36, 'berth', 41, 'abnormal', 'bicycle', 'bid', 'sunday', 'saturday', 87, 'bigot', 41, 'abort',
#               13, 60, 'friday', 26, 13, 'accident', 'access', 40, 26, 20, 75, 13, 40, 67, 12, 'abuse', 78, 10, 80, 'accessory',
#               20, 'bewilder', 'benevolent', 'bet', 64, 38, 65, 51, 95, 'abduct', 37, 98, 99, 14, 'abandon', 'accept', 46, 'abide',
#               'beyond', 19, 'about', 76, 26, 'abound', 12, 95, 'wednesday', 'abundant', 'abrupt', 'aboard', 50, 89, 'tuesday', 66,
#               'bestow', 'absent', 76, 46, 'betray', 47, 'able', 11]
#
# res1 = sorted(filter(lambda x: x if isinstance(x, int) else False, mixed_list))
# res2 = sorted(filter(lambda x: x if isinstance(x, str) else False, mixed_list))
# print(*(res1 + res2))

# ----------------- 32 --------------------

# print(*(map(lambda x: 255 - int(x), input().split())))

# ----------------- 33 --------------------

# def ignore_command(command):
#     ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
#     return any([i in command for i in ignore])
#
#
# print(ignore_command('get ip'))
# print(ignore_command('select all'))
# print(ignore_command('delete'))
# print(ignore_command('trancate'))

# ----------------- 34 --------------------

# countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
# capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
# population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]
#
# for c, cap, pop in zip(countries, capitals, population):
#     print(f"{cap} is the capital of {c}, population equal {pop} people.")

# ----------------- 35 --------------------

a = input().split()
b = int(input())
res = 0
for i in range(len(a)):
    frst = i
    sec = b ** (len(a) - i - 1)
    res += frst * sec
print(res)
