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


result1 = {}
result2 = {}
for let in input():
    result1[let] = result1.get(let, 0) + 1
for let in input():
    result2[let] = result2.get(let, 0) + 1

print('YES' if result1 == result2 else 'NO')
