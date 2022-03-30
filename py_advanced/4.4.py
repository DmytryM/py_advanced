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

a = int(input())
res = [input().split() for _ in range(a)]
res1 = []
sum = 0
amount = 0
for i in range(a):
    for j in range(a):
        sum += int(res[i][j])
    res1.append(sum / len(res[i]))
    # print(sum/len(res[i]))
    sum = 0

for i in range(a):
    for j in range(a):
        if int(res[i][j]) > int(res1[i]):
            amount += 1
    print(amount)
    amount = 0
