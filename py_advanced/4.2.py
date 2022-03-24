# list1 = [[1] * 3] * 3
# list1[0][1] = 5
# print(*list1)

n = int(input())

lists = [[j for j in range(1, n+1)] for i in range(n)]

for i in lists:
    print(i)