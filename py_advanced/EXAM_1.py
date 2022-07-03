# ---------------------------1---------------------------

# m, a = int(input()), input().split()
# print([a[i::m] for i in range(m)])

# ---------------------------2---------------------------

# a = int(input())
# matrix = [[int(j) for j in input().split()] for i in range(a)]
# res = []
# for i in range(a):
#     for j in range(a):
#         if (j >= i >= a - 1 - j) or (i >= j and i >= a - 1 - j):
#             res.append(matrix[i][j])
#
# print(max(res))

# [print(*matrix) for matrix in matrix]

# ---------------------------3---------------------------

# # put your python code here
# n = int(input())
#
# matrix = [[int(j) for j in input().split()] for _ in range(n)]
#
# for i in range(n):
#     for j in range(n):
#         print(matrix[j][i], end=' ')
#     print()
#
# # res = zip(*matrix)
# # [print(*res) for res in res]

# ---------------------------4---------------------------

# first = int(input())
# matrix = [['.' for _ in range(first)] for _ in range(first)]
# for i in range(first):
#     for j in range(first):
#         if (i == j or i == first - 1 - j) or i == first // 2 or j == first // 2:
#             matrix[i][j] = '*'
# [print(*res) for res in matrix]

# ---------------------------5---------------------------

# n = int(input())
#
# matrix = [[int(j) for j in input().split()] for _ in range(n)]
# res = True
# for i in range(n):
#     for j in range(n):
#         if matrix[i][j] != matrix[n - j - 1][n - i - 1]:
#             res = False
#             break
# print('YES' if res else 'NO')


# ---------------------------6---------------------------

# n = int(input())
#
# matrix = [[int(j) for j in input().split()] for _ in range(n)]
# flag = True
# for i in matrix:
#     if sorted(i) != list(range(1, n + 1)):
#         flag = False
# matrix_t = [[matrix[j][i] for j in range(n)] for i in range(n)]
# for i in matrix_t:
#     if sorted(i) != list(range(1, n + 1)):
#         flag = False
# print('YES' if flag else 'NO')

# ---------------------------7---------------------------

# place = input()
# matrix = [['.' for _ in range(8)] for _ in range(8)]
# letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# nums = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
# x = nums[place[1]]
# y = letters[place[0]]
# for i in range(8):
#     for j in range(8):
#         if i == x or j == y or abs(y - j) == abs(x - i):
#             matrix[i][j] = '*'
# matrix[nums[place[1]]][letters[place[0]]] = 'Q'
# [print(*res) for res in matrix]

# ---------------------------8---------------------------

a = int(input())
matrix = [[0 for _ in range(a)] for _ in range(a)]
iteration = 0
for i in range(a):
    for j in range(a):
        matrix[i][j] = abs(i - j)
[print(*res) for res in matrix]

