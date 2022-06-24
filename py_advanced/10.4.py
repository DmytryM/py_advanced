# ---------------- 1 --------------------

# dictionary = {}
# keys = []
# words = []
#
# for i in range(int(input())):
#     pair = input().split(': ')
#     keys.append(pair[0].lower())
#     words.append(pair[1].strip())
#
# dictionary = dict(zip(keys, words))
#
# for i in range(int(input())):
#     quest = input().lower()
#     final = dictionary.get(quest, "Не найдено")
#     print(final)

# ---------------- 2 --------------------

# result1 = {}
# result2 = {}
# for let in input():
#     result1[let] = result1.get(let, 0) + 1
# for let in input():
#     result2[let] = result2.get(let, 0) + 1
#
# print('YES' if result1 == result2 else 'NO')

# ---------------- 3 --------------------

# def compare(a, b):
#     result1 = {}
#     result2 = {}
#
#     for let in a:
#         if let.isalpha():
#             result1[let] = result1.get(let, 0) + 1
#     for let in b:
#         if let.isalpha():
#             result2[let] = result2.get(let, 0) + 1
#
#     print('YES' if result1 == result2 else 'NO')
#
#
# a = input().lower()
# b = input().lower()
# compare(a, b)

# ---------------- 4 --------------------

# res = {}
# for i in range(int(input())):
#     key, value = input().split()
#     res[key] = value
#     res[value] = key
#
# print(res[input()])

# ---------------- 5 --------------------

# res = {}
# for i in range(int(input())):
#     country, *city = input().split()
#     res[country] = city
# for i in range(int(input())):
#     find = input()
#     for key, values in res.items():
#         if find in values:
#             print(key)

# ---------------- 6 --------------------

# result = {}
# for i in range(int(input())):
#     number, name = input().split()
#     result.setdefault(name, []).append(number)
# for i in range(int(input())):
#     quest = input().capitalize()
#     print(*result.get(quest, ["абонент не найден"]))

# ---------------- 7 --------------------

# result = {}
# line = {}
# line1 = {}
# letters = input()
# for let in letters:
#     line[let] = line.get(let, 0) + 1
# for i in range(int(input())):
#     char, value = input().split(': ')
#     line1[int(value)] = char
# for i, j in line.items():
#     for i1, j1 in line1.items():
#         if j == i1:
#             result[i] = j1
#
# print(*(result[let] for let in letters), sep='')


# numbers = [34, 10, -4, 6, 10, 23, -90, 100, 21, -35, -95, 1, 36, -38, -19, 1, 6, 87]
#
# result = {i: numbers[i] ** 2 for i in range(len(numbers))}


# colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow', 'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black', 'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure', 'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac', 'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}
#
# result = {i: colors[i] for i in colors if colors[i]}
#
# print(result)

# favorite_numbers = {'timur': 17, 'ruslan': 7, 'larisa': 19, 'roman': 123, 'rebecca': 293, 'ronald': 76, 'dorothy': 62,
#                     'harold': 36, 'matt': 314, 'kim': 451, 'rosaly': 18, 'rustam': 89, 'soltan': 111, 'amir': 654,
#                     'dima': 390, 'amiran': 777, 'geor': 999, 'sveta': 75, 'rita': 909, 'kirill': 404, 'olga': 271,
#                     'anna': 55, 'madlen': 876}
#
# result = {key: value for key, value in favorite_numbers.items() if len(str(value)) == 2}
#
# print(result)


# months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
#
# result = {value: key for key, value in months.items()}

# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
#
# result = {int(key): value for key, value in [i.split(':') for i in s.split()]}
# print(result)

# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
#
# result = {key: [x for x in range(1, key + 1) if key % x == 0] for key in numbers}
# print(result)

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result = {key: [ord(x) for x in key] for key in words}
# print(result)

# letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 26: 'Z'}
#
# remove_keys = [1, 5, 7, 12, 17, 19, 21, 24]
#
# result = {key: value for key, value in letters.items() if key not in remove_keys}
#
# print(result)


# students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70), 'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87), 'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120), 'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100), 'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}
#
# result = {key: value for key, value in students.items() if value[0] > 167 and value[1] < 75}
# print(result)


# tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18), (19, 20, 21), (22, 23, 24), (25, 26, 27), (28, 29, 30), (31, 32, 33), (34, 35, 36)]
#
# result = {key[0]: key[1:] for key in tuples}
# print(result)


# student_ids = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010', 'S011', 'S012', 'S013']
# student_names = ['Camila Rodriguez', 'Juan Cruz', 'Dan Richards', 'Sam Boyle', 'Batista Cesare', 'Francesco Totti', 'Khalid Hussain', 'Ethan Hawke', 'David Bowman', 'James Milner', 'Michael Owen', 'Gary Oldman', 'Tom Hardy']
# student_grades = [86, 98, 89, 92, 45, 67, 89, 90, 100, 98, 10, 96, 93]
#
# result = [{student_ids[key]: {student_names[key]: student_grades[key]}} for key in range(len(student_ids))]
#
# print(result)
