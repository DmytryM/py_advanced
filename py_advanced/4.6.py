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

# ---------------- 3--------------------

n, m = map(int, input().split())
iteration = 1
for i in range(n):
    matrix = []
    for j in range(m):
        matrix.append(str(iteration).ljust(3))
        iteration += 1
    print(*matrix)
