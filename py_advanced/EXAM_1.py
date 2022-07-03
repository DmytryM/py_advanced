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