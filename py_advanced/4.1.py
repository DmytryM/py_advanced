# ---------------- 1 --------------------

'''Дополните приведенный код, используя списочный метод append(), чтобы список list1 имел вид:

list1 = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]'''


# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#
# list1[2][2].append(7000)
# print(list1)


# ---------------- 2 --------------------

'''Дополните приведенный код, используя списочный метод extend(), чтобы список list1 имел вид:

list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
Подсписок для расширения  sub_list = ['h', 'i', 'j'].'''


# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# sub_list = ['h', 'i', 'j']
# list1[2][1][2].extend(sub_list)
# print(list1)


# ---------------- 3 --------------------

'''Дополните приведенный код, используя цикл for и встроенную функцию max(), чтобы он выводил один 
общий максимальный элемент среди всех элементов вложенных списков list1.'''

# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for i in list1:
#     if maximum < max(i):
#         maximum = max(i)
#
#
# print(maximum)



# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# for i in list1:
#     i.reverse()
#
# print(list1)


list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
total = 0
counter = 0
for i in list1:
    counter += len((i))
    total+=sum(i)
print(total/counter)