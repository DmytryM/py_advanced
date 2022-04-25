# ---------------- 1 --------------------
'''Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь фигуры, задаваемой с помощью системы неравенств:'''
# import random
#
# n = 10 ** 6  # количество испытаний
# k = 0
# s0 = 16
# for _ in range(n):
#     x = random.uniform(-2, 2)
#     y = random.uniform(-2, 2)
#
#     if (x ** 3) + (y ** 4) + 2 >= 0 and (3 * x) + y ** 2 <= 2:
#         k += 1
#
# print((k / n) * s0)

# ---------------- 2 --------------------

'''Напишите программу, которая при помощи метода Монте-Карло определяет приближённое значение числа \piπ.'''
import random

n = 10**6   # количество испытаний
R = 1
k = 0
s0 = 4
for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        k += 1

print((k/n)*s0)