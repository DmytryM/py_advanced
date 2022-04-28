# ---------------- 1 --------------------

# from decimal import *
# s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 ' \
#     '5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50'
#
# numbers = [Decimal(i) for i in s.split()]
# print(max(numbers) + min(numbers))

# ----------------- 2 --------------------
# from decimal import *
# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 ' \
#     '2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
# numbers = [Decimal(i) for i in s.split()]
# print(sum(numbers))
# print(*sorted(numbers)[-1:-6:-1])

# ----------------- 3 --------------------

# from decimal import *
#
# num = abs(Decimal(input()))
# if num < 1:
#     result = num.as_tuple().digits
#     print(max(result))
# else:
#     print(max(num.as_tuple().digits) + min((num.as_tuple().digits)))

# ----------------- 4 --------------------

# from decimal import *
#
# num = Decimal(input())
#
# print(num.exp() + num.ln() + num.log10() + num.sqrt())

# ----------------- 5 --------------------

# from fractions import Fraction
#
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14', '4.29',
#            '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02', '6.95', '1.62',
#            '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31', '4.63', '7.84', '2.25',
#            '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
#
# [print(f'{i} = {Fraction(i)}') for i in numbers]

# ----------------- 6 --------------------

# from fractions import Fraction
#
# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 1.46 ' \
#     '5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 0.03 9.60 ' \
#     '8.86 2.73 5.83 6.50 0.123 0.00021'
# numbers = [Fraction(i) for i in s.split()]
# print(Fraction(max(numbers) + min(numbers)))

# ----------------- 7 --------------------

# from fractions import Fraction as F
#
# print(F(int(input()), int(input())))

# ----------------- 8 --------------------

# from fractions import Fraction
#
# n, m = input(), input()
# n1, m1 = Fraction(n), Fraction(m)
#
# print(f'{n} + {m} = {n1 + m1}')
# print(f'{n} - {m} = {n1 - m1}')
# print(f'{n} * {m} = {n1 * m1}')
# print(f'{n} / {m} = {n1 / m1}')

# ----------------- 9 --------------------

# from fractions import Fraction
#
# n, res = int(input()), 0
# for i in range(1, n + 1):
#     res += Fraction(1, i ** 2)
# print(res)

# ----------------- 10 --------------------

# from fractions import Fraction
# from math import factorial
# # n = int(input())
# # res = 0
# # fuck_list = [1]
# # def fuck(s):
# #     result = 0
# #     result = fuck_list[-1] * s
# #     fuck_list.append(result)
# #     return result
# # # print(fuck(n))
# #
# # for i in range(1, n + 1):
# #     res += Fraction(1, fuck(i))
# # print(res)
#
# n, res = int(input()), 0
#
# for i in range(1, n + 1):
#     res += Fraction(1, factorial(i))
# print(res)

# ----------------- 11 --------------------

# from fractions import Fraction
#
# def nod(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
#
# n = int(input())
# a = n // 2
# b = n - a
# while nod(a, b) != 1:
#     a -= 1
#     b += 1
# res = Fraction(a, b)
# print(res)

# ----------------- 12 --------------------

# from fractions import Fraction
# n = int(input())
# result = set()
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i < j or i == j:
#             continue
#         res = Fraction(j, i)
#         result.add(res)
#
# print(*sorted(result), sep='\n')

# ----------------- 13 --------------------

# z1, z2 = complex(input()), complex(input())
# print(f"{z1} + {z2} = {z1 + z2}")
# print(f"{z1} - {z2} = {z1 - z2}")
# print(f"{z1} * {z2} = {z1 * z2}")

# ----------------- 14--------------------

numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j, 1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]
for i in numbers:
    print()