# ---------------- 1 --------------------

'''На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.
Создайте матрицу mult размером n \times mn×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.'''

# a, b = int(input()), int(input())
# 
# # for i in range(a):
# #     mult = []
# #     for j in range(b):
# #         mult.append(str(i*j).ljust(3))
# #     print(*mult)
# 
# mult = [[print(*[str(i * j).ljust(3) for j in range(b)]) for i in range(a)]]

'''Поиск через рекурсию'''

# def bsearch(list, idx0, idxn, val):
#     if idxn < idx0:
#         return None
#     else:
#         midval = idx0 + ((idxn - idx0) // 2)
#         # Compare the search item with middle most value
#
#         if list[midval] > val:
#             return bsearch(list, idx0, midval - 1, val)
#         elif list[midval] < val:
#             return bsearch(list, midval + 1, idxn, val)
#         else:
#             return midval
#
#
# list = [8, 11, 24, 56, 88, 131]
# print(bsearch(list, 0, 5, 24))
# print(bsearch(list, 0, 5, 51))


# ---------------- 2 --------------------

'''На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице, затем nn строк по 
mm целых чисел в каждой, отделенных символом пробела.'''

# a, b = int(input()), int(input())
#
# # в первой строке ввода идёт количество строк массива
# res = [[int(j) for j in input().split()] for i in range(a)]
#
# maxRes = res[0][0]
# maxX, maxY = 0, 0
#
# for i in range(a):
#     for j in range(b):
#         if maxRes < res[i][j]:
#             maxX, maxY = i, j
#
# print(maxX, maxY)

# class matrix:
#     def __init__(self, n=0, m=0):
#         self.n = n
#         self.m = m
#         self.matrix = []
#
#     def minput(self):
#         self.n = int(input())
#         self.m = int(input())
#         for i in range(self.n):
#             self.matrix.append([int(elem) for elem in input().split()])
#
#     def maximum_in_the_table(self):
#         maximum = self.matrix[0][0]
#         max_i, max_j = 0, 0
#         for i in range(self.n):
#             for j in range(self.m):
#                 if maximum < self.matrix[i][j]:
#                     maximum = self.matrix[i][j]
#                     max_i, max_j = i, j
#         return max_i, max_j
#
#
# if __name__ == "__main__":
#     mult = matrix()
#     mult.minput()
#     print(*mult.maximum_in_the_table())


# ---------------- 3 --------------------

'''Напишите программу, которая меняет местами столбцы в матрице.'''

# a, b = int(input()), int(input())
#
# res = [[int(j) for j in input().split()] for i in range(a)]
#
# first, second = [int(_) for _ in input().split()]  # '0 1'  =>  [0, 1]
#
# for j in range(a):
#     res[j][first], res[j][second] = res[j][second], res[j][first]
#
# for line in res:
#     print(*line)


# ---------------- 4 --------------------

'''Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.'''

# n = int(input())
# matrix = [[int(j) for j in input().split()] for _ in range(n)]
# print('YES' if all([matrix[i][j] == matrix[j][i] for j in range(n) for i in range(n)]) else 'NO')

# ---------------- 5 --------------------

'''Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной 
диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами 
элемент на главной диагонали и на побочной диагонали).'''

# n = int(input())
# matrix = [[int(j) for j in input().split()] for _ in range(n)]
#
# for i in range(n):
#     matrix[i][i], matrix[n - i - 1][i] = matrix[n - i - 1][i], matrix[i][i]
#
# [print(*res) for res in matrix]

# ---------------- 6 --------------------

'''Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её 
элементы относительно горизонтальной оси симметрии.'''

n = int(input())

matrix = [[int(j) for j in input().split()] for _ in range(n)]

for i in range(n - 1, -1, -1):
    print(*matrix[i])


