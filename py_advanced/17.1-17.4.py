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

# ----------------- 5 --------------------

# file = open('numbers.txt')
# print(sum(map(int, file)))
# file.close()

# ----------------- 6 --------------------

# file = open('nums.txt')
# print(sum(map(int, file.read().split())))
# file.close()

# ----------------- 7 --------------------

# file = open('prices.txt')
# lines = map(str.split, file)
# print(sum(map(lambda line: int(line[1]) * int(line[2]), lines)))
# file.close()

# ----------------- 8 --------------------

# with open('text.txt') as f:
#     print(f.read()[::-1])

# ----------------- 9 --------------------

# with open('data.txt', encoding='utf-8') as file:
#     print(*file.readlines()[::-1], sep='')

# ----------------- 10 --------------------

# file = open('lines.txt')
# lines = [line.strip() for line in file.readlines()]
# print(lines, key=len)
# file.close()

# ----------------- 11 --------------------

# with open('numbers.txt') as f:
#     for line in f:
#         print(sum(map(int, line.split())))

# ----------------- 12 --------------------
import re

with open('nums.txt') as f:
    res = []
    sum = 0
    sp = [re.findall('\d+', i) for i in f.readlines()]
    # print(sp)
    for i in sp:
        for j in i:
            sum += int(j)
    print(sum)


