# ---------------- 1 --------------------

# result = {key : key**2 for key in range(1, 16)}
# print(result)

# ---------------- 2 --------------------

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# dict1.update(dict2)
# result = {dict1}
# print(result)

# ---------------- 3 --------------------

text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
letters = [c for c in text]
result = {}
for let in letters:
    result[let] = result.get(let, 0) + 1

print(result)