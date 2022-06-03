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

# with open('numbers.txt') as file:
#     temp = ''
#     n = 0
#     for c in file.read():
#         if c.isdigit():
#             temp += c
#         elif temp != '':
#             n += int(temp)
#             temp = ''
#     print(n)

# ----------------- 13 --------------------

# with open('file.txt') as file:
#     res = [line.strip() for line in file.readlines()]
#     lines = len(res)
#     words = 0
#     letters = 0
#     for i in res:
#         result = i.split()
#         words += len(result)
#         for j in i:
#             if j.isalpha():
#                 letters += 1
#     print('Input file contains:')
#     print(f"{letters} letters")
#     print(f"{words} words")
#     print(f"{lines} lines")

# ----------------- 14 --------------------

# import random
#
# with open('first_names.txt') as names, open('last_names.txt') as surnames:
#     name, surname = [line.strip() for line in names.readlines()], [line.strip() for line in surnames.readlines()]
#     [print(random.choice(name), random.choice(surname)) for i in range(3)]

# ----------------- 15 --------------------

# with open('population.txt') as file:
#     data = [s.strip().split('\t') for s in file.readlines()]
#
# for line in filter(lambda x: x[0][0].upper() == 'G' and int(x[1]) > 500000, data):
#     print(line[0])

# ----------------- 16 --------------------

# def read_csv():
#     with open('data.csv') as File:
#         res = [line.strip() for line in File.readlines()]
#         print(res)

# import csv
#
# def read_csv():
#     results = []
#     with open('data.csv') as File:
#         reader = csv.DictReader(File)
#         for row in reader:
#             results.append(row)
#         return results

# def read_csv():
#     with open('data.csv') as f:
#         keys = f.readline().strip().split(',')
#         return [dict(zip(keys, line.strip().split(','))) for line in f]
#
#
# print(read_csv())

# ----------------- 17 --------------------

# with open('lines.txt', encoding='utf-8') as file:
#     text = file.readlines()
#
# n = len(max(text, key=len))
# print(*filter(lambda x: len(x) == n, text), sep='')

# ----------------- 18 --------------------

# import random
# with open('random.txt', 'w') as output:
#     print(*random.sample(range(111, 777), 25), sep='\n', file=output)

# ----------------- 19 --------------------

# with open('input.txt') as inp, open('output.txt', 'w') as out:
#     data = inp.readlines()
#     out.writelines([f'{i + 1}) {data[i]}' for i in range(len(data))])

# ----------------- 20 --------------------

# with open('class_scores.txt') as inn, open('new_scores.txt', 'w') as out:
#     for line in inn:
#         name, value = line.split()
#         out.write(f'{name} {min(100, int(value) + 5)}\n')

# ----------------- 21 --------------------

# names = [input() for i in range(int(input()))]
# with open('output.txt', 'w') as out:
#     for i in names:
#         with open(i, 'r') as inpt:
#             res1 = inpt.readlines()
#             for j in res1:
#                 out.write(j)

# ----------------- 22 --------------------

# def minutes(x):
#     res = [int(i) for i in x.split(':')]
#     return res[0] * 60 + res[1]
#
#
# with open('logfile.txt', 'r', encoding='utf-8') as log, open('output.txt', 'w', encoding='utf-8') as out:
#     data = [line.strip().split(',') for line in log.readlines()]
#     for i in data:
#         if minutes(i[2]) - minutes(i[1]) >= 60:
#             out.write(i[0] + '\n')

# ----------------- 23 --------------------

with open('goats.txt') as file:
    text = [line.strip() for line in file.readlines()]

print(text)


