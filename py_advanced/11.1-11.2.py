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
