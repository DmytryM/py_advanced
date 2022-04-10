# ---------------- 1 --------------------

a, b = map(int, input().split())
res1 = [[int(j) for j in input().split()] for i in range(a)]
input()
res2 = [[int(j) for j in input().split()] for i in range(a)]

for i in range(a):
    row = [res1[i][j] + res2[i][j] for j in range(b)]
    print(*row)