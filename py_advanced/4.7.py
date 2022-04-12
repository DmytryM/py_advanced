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

a, b = map(int, input().split())
res1 = [[int(j) for j in input().split()] for i in range(a)]

a1, b1 = map(int, input().split())
res2 = [[int(j) for j in input().split()] for i in range(a1)]

res3 = []
result = 0
for i in range(a):
    result = i
    for j in range(b):
        result *= j
    res3.append(result)

[print(mat) for mat in res3]