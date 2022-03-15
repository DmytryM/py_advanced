# ----- 3 task -----
# string = input()
#
# s1 = int(len(string) * 100)
# s1 = (s1 * 60) // 100
#
# s2 = s1//100
# s3 = s1%100
# print(s2,'р.',s3,'коп.')


# ---------- 4 task -----


# print(len(input().split()))


# ------- 5 -------

# year = int(input())
# animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
#
# res = year % 12
# print(animals[res])


# ------- 6 ------

# def rotate(a, x, y):
#     return int(a[x:y:-1])


# a = input()
#
# if len(a) == 6:
#     print(a[0] + f"{a[:-6:-1]}")
# elif len(a) == 5:
#     print(int(a[::-1]))


# ------ 7 -------

# a = input()
# iter = 0
# if len(a) < 4:
#     print(a)
# else:
#     b = []
#     a = a[::-1]
#     a = [i for i in a]
#     for i in range(3, len(a), 3):
#         a.insert(i + iter, ',')
#         iter += 1
#     print("".join(a[::-1]))


# ------ 8 -------

n = int(input())
k = int(input())


def joseph(n, k):
    if n == 1:
        return 1
    elif n > 1:
        return (joseph(n - 1, k) + k - 1) % n + 1


print(joseph(n, k))
