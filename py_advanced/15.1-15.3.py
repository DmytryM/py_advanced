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
