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