# ---------------- 1 --------------------

# a, b = map(int, input().split())
# res1 = [[int(j) for j in input().split()] for i in range(a)]
# input()
# res2 = [[int(j) for j in input().split()] for i in range(a)]
#
# for i in range(a):
#     row = [res1[i][j] + res2[i][j] for j in range(b)]
#     print(*row)

# ---------------- 2 --------------------

# a, b = map(int, input().split())
# res1 = [[int(j) for j in input().split()] for i in range(a)]
# input()
# a1, b1 = map(int, input().split())
# res2 = [[int(j) for j in input().split()] for i in range(a1)]
# res3 = [[0 for _ in range(a)] for _ in range(b1)]
# result = 1
# for i in range(a):
#     for j in range(b1):
#         for x in range(a1):
#             res3[i][j] += res1[i][x] * res2[x][j]
# for i in range(a):
#     for j in range(b1):
#         print(res3[i][j], end=' ')
#     print()

# ---------------- 3 --------------------

a = int(input())
res1 = [[int(j) for j in input().split()] for i in range(a)]
degree = int(input())
res2 = res1.copy()
res3 = 0
for s in range(degree - 1):
    res3 = [[0 for _ in range(a)] for _ in range(a)]
    for i in range(a):
        for j in range(a):
            for x in range(a):
                res3[i][j] += res1[i][x] * res2[x][j]
    res2 = res3.copy()

[print(*res) for res in res3]