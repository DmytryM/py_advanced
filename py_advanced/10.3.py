# ---------------- 1 --------------------

# result = {key : key**2 for key in range(1, 16)}
# print(result)

# ---------------- 2 --------------------

# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = dict1.copy()
# for key, value in dict2.items():
#     result[key] = result.get(key, 0) + value
#
# print(result)


# ---------------- 3 --------------------

# text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
# letters = [c for c in text]
# result = {}
# for let in letters:
#     result[let] = result.get(let, 0) + 1
#
# print(result)

# ---------------- 4 --------------------

# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
#
# s = list(s.split())
# result = {}
# for num in s:
#     result[num] = result.get(num, 0) + 1
# max = 0
# reskey = 0
# for key, value in result.items():
#     if value >= max:
#         max = value
#         reskey = key
#
# print(reskey)

# ---------------- 5 --------------------
