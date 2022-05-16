# ----------------- 1 --------------------

# file = open(input(), 'r')
# print(file.read())
# file.close()

# ----------------- 2 --------------------

# with open(input()) as output:
#     print(output.readlines()[-2])
# output.close()

# ----------------- 3 --------------------
# import random
#
# path = "lines.txt"
# file = open(path, 'r', encoding='utf-8')
# languages = [line.strip() for line in file.readlines()]
# print(random.choice(languages))
# file.close()

# ----------------- 4 --------------------

# print(__import__('random').choice(list(open("lines.txt", encoding='utf-8'))))
