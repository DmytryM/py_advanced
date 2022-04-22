# ---------------- 1 --------------------

# dictionary = {}
# keys = []
# words = []
#
# for i in range(int(input())):
#     pair = input().split(': ')
#     keys.append(pair[0].lower())
#     words.append(pair[1].strip())
#
# dictionary = dict(zip(keys, words))
#
# for i in range(int(input())):
#     quest = input().lower()
#     final = dictionary.get(quest, "Не найдено")
#     print(final)

# ---------------- 2 --------------------

# result1 = {}
# result2 = {}
# for let in input():
#     result1[let] = result1.get(let, 0) + 1
# for let in input():
#     result2[let] = result2.get(let, 0) + 1
#
# print('YES' if result1 == result2 else 'NO')

# ---------------- 3 --------------------

# def compare(a, b):
#     result1 = {}
#     result2 = {}
#
#     for let in a:
#         if let.isalpha():
#             result1[let] = result1.get(let, 0) + 1
#     for let in b:
#         if let.isalpha():
#             result2[let] = result2.get(let, 0) + 1
#
#     print('YES' if result1 == result2 else 'NO')
#
#
# a = input().lower()
# b = input().lower()
# compare(a, b)

# ---------------- 4 --------------------

# res = {}
# for i in range(int(input())):
#     key, value = input().split()
#     res[key] = value
#     res[value] = key
#
# print(res[input()])

# ---------------- 5 --------------------

# res = {}
# for i in range(int(input())):
#     country, *city = input().split()
#     res[country] = city
# for i in range(int(input())):
#     find = input()
#     for key, values in res.items():
#         if find in values:
#             print(key)

# ---------------- 6 --------------------

# result = {}
# for i in range(int(input())):
#     number, name = input().split()
#     result.setdefault(name, []).append(number)
# for i in range(int(input())):
#     quest = input().capitalize()
#     print(*result.get(quest, ["абонент не найден"]))

# ---------------- 7 --------------------

result = {}
line = {}
line1 = {}
letters = input()
for let in letters:
    line[let] = line.get(let, 0) + 1
for i in range(int(input())):
    char, value = input().split(': ')
    line1[int(value)] = char
for i, j in line.items():
    for i1, j1 in line1.items():
        if j == i1:
            result[i] = j1

print(*(result[let] for let in letters), sep='')

