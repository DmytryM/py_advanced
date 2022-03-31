# ---------------- 1 --------------------

'''На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице.
Создайте матрицу mult размером n \times mn×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.'''

a, b = int(input()), int(input())

# for i in range(a):
#     mult = []
#     for j in range(b):
#         mult.append(str(i*j).ljust(3))
#     print(*mult)

mult = [[print(*[str(i * j).ljust(3) for j in range(b)]) for i in range(a)]]
