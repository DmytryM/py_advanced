# ---------------- 1 --------------------

'''На вход программе подаются два натуральных числа nn и mm. Напишите программу для создания матрицы размером n \times
mn×m, заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка. Выведите полученную
матрицу на экран, разделяя элементы пробелами.'''

# n, m = map(int, input().split())
# for i in range(n):
#     row = ['.' if (i + j) % 2 == 0 else '*' for j in range(m)]
#     print(*row)

# ---------------- 2 --------------------

# a = int(input())
#
# for i in range(a):  # заполняем главную диагональ единицами, а побочную двойками
#     # matrix[i][a - i - 1] = 1
#     # for j in range(a):
#     #     if i > a - 1 - j:
#     #         matrix[i][j] = 2
#     matrix = [0 if i < a - 1 - j else 1 if i == a - 1 - j else 2 for j in range(a)]
#     print(*matrix)

# ---------------- 3 --------------------

# n, m = map(int, input().split())
# iteration = 1
# for i in range(n):
#     matrix = []
#     for j in range(m):
#         matrix.append(str(iteration).ljust(3))
#         iteration += 1
#     print(*matrix)

# ---------------- 4 --------------------

# n, m = map(int, input().split())
# iteration = 0
# for i in range(n):
#     matrix = []
#     iteration = i + 1
#     for j in range(m):
#         matrix.append(str(iteration).ljust(3))
#         iteration += n
#     print(*matrix)

# ---------------- 5 --------------------

# n = int(input())
# for i in range(n):
#     matrix = [1 if i == j or i == n - 1 - j else 0 for j in range(n)]
#     print(*matrix)

# ---------------- 6 --------------------

# n = int(input())
# for i in range(n):
#     matrix = [1 if (i <= j and i <= n - 1 - j) or (i >= j and i >= n - 1 - j) else 0 for j in range(n)]
#     print(*matrix)

# ---------------- 7 --------------------

# n, m = map(int, input().split())
# mat = [[0 for _ in range(m)] for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         mat[i][j] = (i + j) % m + 1
# [print(*res) for res in mat]

# ---------------- 8 --------------------

# n, m = map(int, input().split())
# count = 1
# matrix = [[0 for _ in range(m)] for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         if i % 2 != 0:
#             matrix[i][m - 1 - j] = count
#             count += 1
#         else:
#             matrix[i][j] = count
#             count += 1
#
# [print(*res) for res in matrix]

# ---------------- 9 --------------------

# n, m = map(int, input().split())
# mat = [[0 for _ in range(m)] for _ in range(n)]
# count = 1
# for x in range(n + m):
#     for i in range(n):
#         for j in range(m):
#             if i + j == x:
#                 mat[i][j] = count
#                 count += 1
# [print(*res) for res in mat]

# ---------------- 10 --------------------

n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]
count = 1
i, j = 0, -1
max_j, max_i = m - 1, n - 1
min_j, min_i = 0, 1
for iteration in range(n * m):
    while j < max_j:
        j += 1
        matrix[i][j] = count
        count += 1
    max_j -= 1

    while i < max_i:
        i += 1
        matrix[i][j] = count
        count += 1
    max_i -= 1

    while j > min_j:
        j -= 1
        matrix[i][j] = count
        count += 1
    min_j += 1

    while i > min_i:
        i -= 1
        matrix[i][j] = count
        count += 1
    min_i += 1

    if j == (n - 1) // 2 and i == n // 2:
        break
for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=' ')
    print()
