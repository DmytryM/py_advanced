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

# n = int(input())
#
# matrix = [[int(j) for j in input().split()] for _ in range(n)]
#
# for i in range(n - 1, -1, -1):
#     print(*matrix[i])

# ---------------- 7 --------------------

'''Напишите программу, которая поворачивает квадратную матрицу чисел на 90^{\circ}90 
  по часовой стрелке.'''

# n = int(input())
#
# matrix = [[int(j) for j in input().split()] for _ in range(n)]
#
# for i in range(n):
#     for j in range(n - 1, -1, -1):
#         print(matrix[j][i], end=' ')
#     print()

# ---------------- 8 --------------------

'''На шахматной доске 8 times 88×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все 
клетки, которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, отметьте 
символами *, остальные клетки заполните точками.'''

# place = input()
# matrix = [['.' for _ in range(8)] for _ in range(8)]
# letters = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# nums = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
# matrix[nums[place[1]]][letters[place[0]]] = 'N'
# for i in range(8):
#     for j in range(8):
#         if (i - nums[place[1]]) ** 2 + (j - letters[place[0]]) ** 2 == 5:
#             matrix[i][j] = '*'
# [print(*res) for res in matrix]

# ---------------- 9 --------------------

'''Магическим квадратом порядка nn называется квадратная таблица размера n \times nn×n, составленная из всех чисел 1, 
2, 3, \ldots, n^21,2,3,…,n 2 так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между 
собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.'''


def magic_square():
    n = int(input())
    matrix = [[int(j) for j in input().split()] for _ in range(n)]
    check = []
    res = "YES"
    for i in range(n):  # заполняем проверочный список всеми элементами матрицы
        check += matrix[i]

    for i in range(1, len(check) + 1):  # проверяем проверочный список на наличие всех чисел в промежутке от 1 до n ** 2
        if i not in check:
            return print(
                "NO")  # если нет какого-то числа, то значит дальше нет смысла проверять равенство, завершаем с NO
    print(matrix)
    print(res)
    print(check)


magic_square()
# def is_magic_square(matrix, S, N):
#     return (all(sum(row) == S for row in matrix)
#             and all(sum(column) == S for column in zip(*matrix))
#             and sum(matrix[i][i] for i in range(N)) == S
#             and sum(matrix[i][N-1-i] for i in range(N)) == S
#             and set(x for row in matrix for x in row) == set(range(1, N**2 + 1)))
#
# N = int(input())  # it is guaranteed to be integer
# try:
#     matrix = [list(map(int, input().split())) for _ in range(N)]
# except ValueError:  # non integer
#     print('NO')
# else:
#     print('YES' if N == 0 or is_magic_square(matrix, sum(matrix[0]), N) else 'NO')
