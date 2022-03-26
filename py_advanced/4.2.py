# list1 = [[1] * 3] * 3
# list1[0][1] = 5
# print(*list1)


# ---------------- 1 --------------------

# n = int(input())
#
# lists = [[j for j in range(1, n+1)] for i in range(n)]
#
# for i in lists:
#     print(i)


# ---------------- 2 --------------------

# n = int(input())
#
# lists = [[j for j in range(1, i+1)] for i in range(1, n + 1)]
#
# for i in lists:
#     print(i)


# ---------------- 3 --------------------


# n = int(input())
# lists = []
#
# for i in range(n + 1):
#     row = [1] * (i + 1)
#     for j in range(1, i):
#         row[j] = lists[i - 1][j - 1] + lists[i - 1][j]
#     lists.append(row)
#
# for i in range(n):
#     print(*lists[i])


# ---------------- 4 --------------------

'''На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает
последовательности одинаковых символов заданной строки в подсписки.'''

# char_list = []
# elem = [i for i in input().split()]
# a = []
# for i in elem:
#     if not a:
#         a.append(i)
#     else:
#         if a[-1] == i:
#             a.append(i)
#         else:
#             char_list.append(a)
#             a = []
#             a.append(i)
# char_list.append(a)
# print(char_list)

# ---------------- 5 --------------------

'''На вход программе подаются две строки, на одной символы, на другой число nn. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает список из чанков указанной длины.'''

# my_list = []
# elem = [i for i in input().split()]
# my_list.extend(elem)
# res = []
# chunk = int(input())
#
# for i in range(len(elem)):
#     res.append()
