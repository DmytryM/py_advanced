# ---------------- 1 --------------------

'''На вход программе подаются два натуральных числа nn и mm, каждое на отдельной строке — количество строк и столбцов в
матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала первой
строки, затем второй, и т.д.Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит
их в виде матрицы.'''

# a, b = int(input()), int(input())
#
# res = [[input() for _ in range(b)] for _ in range(a)]
#
# for row in res:            # делаем перебор всех строк матрицы A
#     for elem in row:     # перебираем все элементы в строке row
#         print(elem, end = ' ')
#     print()


# ---------------- 2 --------------------


# def matrix():  # matrix() обрабатывает вводимые данные и преобразует их в матрицу
#     matrix, rows, cols = [], int(input()), int(input())
#     matrix = [[input() for _ in range(cols)] for _ in range(rows)]
#     return matrix, rows, cols
#
#
# def print_matrix(matrix, rows, cols):  # вывод матрицы
#     for i in range(rows):
#         for j in range(cols):
#             print(matrix[i][j], end=" ")
#         print()
#
#
# def print_matrix_t(matrix, rows, cols):  # вывод транспонирования матрицы
#     for j in range(cols):
#         for i in range(rows):
#             print(matrix[i][j], end=" ")
#         print()
#
#
# matrix, rows, cols = matrix()
# print_matrix(matrix, rows, cols)
# print()
# print_matrix_t(matrix, rows, cols)


# ---------------- 3 --------------------

'''Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, которая выводит след 
заданной квадратной матрицы'''

# a = int(input())
# # res = []
# # res1 = 0
# # res2 = 0
# # for i in range(a):
# #     res.append(input().split())
# #     res2 += int(res[i][i])
# #
# # print(res2)
#
# res = [input().split() for _ in range(a)]
# print(sum([int(res[i][i]) for i in range(a)]))


# ---------------- 4 --------------------

'''Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего 
арифметического элементов данной строки.'''

# a = int(input())
# res = [input().split() for _ in range(a)]
# res1 = []
# sum = 0
# amount = 0
# for i in range(a):
#     for j in range(a):
#         sum += int(res[i][j])
#     res1.append(sum / len(res[i]))
#     # print(sum/len(res[i]))
#     sum = 0
#
# for i in range(a):
#     for j in range(a):
#         if int(res[i][j]) > int(res1[i]):
#             amount += 1
#     print(amount)
#     amount = 0

# ---------------- 5 --------------------

'''Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.'''

# a = int(input())
# res = [input().split() for _ in range(a)]
# res2 = []
#
# for i in range(a):
#     for j in range(0, i + 1):
#         res2.append(int(res[i][j]))
# print(max(res2))

# ---------------- 6 --------------------

'''Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.'''

# a = int(input())
# res = [input().split() for _ in range(a)]
# res2 = []
#
# for i in range(a):
#     for j in range(a):
#         if(i < j and i < a - 1 - j) or (i > j and i > a - 1 - j):
#             pass
#         else:
#             res2.append(int(res[i][j]))
#
# print(max(res2))

# ---------------- 7 --------------------

'''Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, 
нижнюю, левую и правую'''

# n = int(input())
# matrix = []
# quadrants = [['Верхняя четверть:', 0],
#              ['Правая четверть:', 0],
#              ['Нижняя четверть:', 0],
#              ['Левая четверть:', 0]]
#
# for _ in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)
#
# for i in range(n):
#     for j in range(n):
#         if i < j and i + j + 1 < n :
#             quadrants[0][1] += matrix[i][j]
#         elif i < j and i + j + 1 > n:
#             quadrants[1][1] += matrix[i][j]
#         elif i > j and i + j + 1 > n:
#             quadrants[2][1] += matrix[i][j]
#         elif i > j and i + j + 1 < n:
#             quadrants[3][1] += matrix[i][j]
#
# for i in range(4):
#     print(quadrants[i][0], quadrants[i][1])

