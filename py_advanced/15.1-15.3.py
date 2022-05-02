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
