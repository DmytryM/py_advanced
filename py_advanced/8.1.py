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

a = input().split()
print('YES' if set(a[0]) == set(a[1]) == set(a[2]) else 'NO')