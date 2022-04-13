# ---------------- 1 --------------------
# numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
# a = list(numbers)
# res = 1
# for i in a:
#     res *= i
# print(res)

# ---------------- 2 --------------------

# poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
# poet_data = list(poet_data)
# poet_data[2] = 'Москва'
# print(tuple(poet_data))

# ---------------- 3 --------------------

# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
#
# print([sum(i) / len(i) for i in numbers])

# ---------------- 4 --------------------

# a = int(input())
# b = int(input())
# c = int(input())
#
# resX = (-b) / (2 * a)
# resY = ((4 * a * c) - (b ** 2)) / (4 * a)
#
# res = (resX, resY)
#
# print(res)

# ---------------- 5 --------------------

n = int(input())
pupil = tuple(input().split() for _ in range(n))
[print(*i) for i in pupil]
print()
[print(*i) for i in pupil if int(i[1]) > 3]


