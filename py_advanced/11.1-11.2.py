# ---------------- 1 --------------------

# import random
#
# n = int(input())    # количество попыток
# for i in range(n):
#     print(random.choice(['Орел','Решка']))

# ---------------- 2 --------------------

# import random
#
#
# def password(length):
#     upper = [chr(_) for _ in range(65, 91)]
#     lower = [chr(_) for _ in range(97, 123)]
#     for i in range(length):
#         yield random.choice(upper+lower)
#
#
# length = int(input())  # длина пароля
# for i in password(length):
#     print(i, end='')
# # print(password(length), end='')

# ---------------- 3 --------------------

# import random
#
# a = []
# for i in range(7):
#     a.append(random.randint(1, 49))
# print(*sorted(a))

# ---------------- 4 --------------------
# import random
#
#
# def generate_ip():
#     # res = []
#     # for i in range(4):
#     #     res.append(str(random.randint(0, 255)))
#     # return '.'.join(res)
#     return '.'.join(str(random.randint(0, 255)) for _ in range(4))
#
#
# result = generate_ip()
# print(generate_ip())
# # result = [str(x) for x in result]
# # print(result)
# # print('.'.join(result))

# ---------------- 5 --------------------
# import random
# import string
#
#
# def generate_index():
#     lln = [str(random.choice(string.ascii_uppercase) + (str(random.choice(string.ascii_uppercase))) + str(
#         random.randint(0, 99))), str(random.randint(0, 99)) + str(random.choice(string.ascii_uppercase)) + str(
#         random.choice(string.ascii_uppercase))]
#     return '_'.join(lln)
#
#
# generate = generate_index()
# print(generate)

# ---------------- 6 --------------------

# import random
#
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# random.shuffle(matrix)
# [random.shuffle(i) for i in matrix]
# [print(*res) for res in matrix]

# ---------------- 7 --------------------

# import random
#
# x = [1, 2, 3, 4, 5, 6, 7]
# res = []
#
# while len(res) < 100:
#     choice = random.sample(x, len(x))
#     if choice not in res:
#         res.append(choice)
# [print(*res, sep='') for res in res]
# print(f'{i}={*random.sample(x, len(x))}', sep='')

# ---------------- 8 --------------------
# import random
#
# numbers = input()
#
# print(*random.sample(numbers, len(numbers)), sep="")

# ---------------- 9 --------------------

# first
# from random import shuffle
#
# lst = list(range(1, 76))
# shuffle(lst)
# m = [[lst.pop() for _ in range(5)] for _ in range(5)]
# m[2][2] = 0
# [print(*res) for res in m]
# second
# nums = [i for i in range(1, 76)]
# res = [[0 for _ in range(5)] for _ in range(5)]
# for i in range(5):
#     for j in range(5):
#         result = random.sample(nums, 1)
#         res[i][j] = result
#         # while True:
#         #     result = random.randint(1, 75)
#         #     if result not in res:
#         #         res[i][j] = result
#         #         break
# res[2][2] = 0
# for i in range(5):
#     for j in range(5):
#         print(str(res[i][j]).ljust(6), end='')
#     print()

# ---------------- 10 --------------------

# import random
#
# res, resF, resS = [], [], []
#
# for i in range(int(input())):
#     res.append(input())
#
# res1 = res.copy()
# random.shuffle(res1)
# i = 0
# while i < len(res):
#     First = random.choice(res)
#     Second = random.choice(res1)
#     if First != Second and First not in resF and Second not in resS:
#         resF.append(First)
#         resS.append(Second)
#         i += 1
# for i in range(len(resF)):
#     print(f"{resF[i]} - {resS[i]}")
