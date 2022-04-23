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
import random


def generate_ip():
    # res = []
    # for i in range(4):
    #     res.append(str(random.randint(0, 255)))
    # return '.'.join(res)
    return '.'.join(str(random.randint(0, 255)) for _ in range(4))


result = generate_ip()
print(generate_ip())
# result = [str(x) for x in result]
# print(result)
# print('.'.join(result))
