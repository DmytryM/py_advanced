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


my_list = []
a = []

elem = [i for i in input().split()]
my_list.extend(elem)

print(my_list)