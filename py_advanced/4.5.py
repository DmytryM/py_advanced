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

a, b = int(input()), int(input())

res = [[input() for _ in range(b)] for _ in range(a)]

print(res)
# for i in range(a):
#     for j in range(b):