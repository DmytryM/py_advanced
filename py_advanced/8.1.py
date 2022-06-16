# ---------------- 1 --------------------

# numbers = {9089, -67, -32, 1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111, 111, 1, 23}
#
# sum(map(lambda x: x ** 2, numbers))

# ---------------- 2 --------------------

# fruits = {'apple', 'banana', 'cherry', 'avocado', 'pineapple', 'apricot', 'banana', 'avocado', 'grapefruit'}
#
# sortfr = sorted(fruits, reverse=True)
# print(*sortfr, sep='\n')

# ---------------- 3 --------------------

# print(len(set(input())))

# ---------------- 4 --------------------

# n = input()
# print('YES' if len(n) == len(set(n)) else 'NO')

# ---------------- 5 --------------------

# numbers = set(input() + input())
# print('YES' if len(numbers) == 10 else 'NO')

# ---------------- 6 --------------------

# print('YES' if set(input()) == set(input()) else 'NO')

# ---------------- 7 --------------------

# a = input().split()
# print('YES' if set(a[0]) == set(a[1]) == set(a[2]) else 'NO')

# ---------------- 8 --------------------

# [print(len(set(input().lower()))) for x in range(int(input()))]

# ---------------- 9 --------------------

# res = set()
# for i in range(int(input())):
#     res.update(input().lower())
# print(len(res))

# ---------------- 10 --------------------

# a = [word.lower().strip('.,;:-?!') for word in input().split()]
# print(len(set(a)))

# ---------------- 11 --------------------

# s = set()
# for item in input().split():
#   print(["NO", "YES"][item in s])
#   s.add(item)

# ---------------- 12 --------------------

# print(len(set(input().split()) & set(input().split())))

# ---------------- 13 --------------------

# print(*sorted(set(map(int, input().split())) & set(map(int, input().split()))))

# ---------------- 14 --------------------

# print(*sorted(set(map(int, input().split())) - set(map(int, input().split()))))

# ---------------- 15 --------------------

# s = set('1234567890')
#
# for i in range(int(input())):
#     s &= set(input())
# print(*sorted(s))

# ---------------- 16 --------------------

# print(("YES", "NO")[set(input()).isdisjoint(input())])

# ---------------- 17 --------------------

# print(("NO", 'YES')[set(input()).issuperset(input())])

# ---------------- 18 --------------------

# a, b, c = [set(map(int, input().split())) for _ in range(3)]
#
# print(*sorted((a & b) - c, reverse=True))

# ---------------- 19 --------------------

# items = [10, '30', 30, 10, '56', 34, '12', 90, 89, 34, 45, '67', 12, 10, 90, 23, '45', 56, '56', 1, 5, '6', 5]
#
# myset = {int(i) for i in items}
#
# print(*sorted(myset))

# ---------------- 20 --------------------

# words = ['Plum', 'Grapefruit', 'apple', 'orange', 'pomegranate', 'Cranberry', 'lime', 'Lemon', 'grapes', 'persimmon', 'tangerine', 'Watermelon', 'currant', 'Almond']
#
# myset = {i[0].lower() for i in words}
#
# print(*sorted(myset))

# ---------------- 21 --------------------

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
#
# res = {sentence.strip(':,.!?();').lower() for sentence in sentence.split()}
#
# print(*sorted(res))


# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''
# res = {sentence.strip(':,.!?();').lower() for sentence in sentence.split()}
# result = [x for x in res if len(x) < 4]
# print(*sorted(result))

files = ['python.png', 'qwerty.py', 'stepik.png', 'beegeek.org', 'windows.pnp', 'pen.txt', 'phone.py', 'book.txT', 'board.pNg', 'keyBoard.jpg', 'Python.PNg', 'apple.jpeg', 'png.png', 'input.tXt', 'split.pop', 'solution.Py', 'stepik.org', 'kotlin.ko', 'github.git']
result = {c.lower() for c in files if c.lower().endswith('.png')}

print(*sorted(result))